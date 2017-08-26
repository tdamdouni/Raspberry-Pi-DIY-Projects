#!/bin/bash

: <<'DISCLAIMER'

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

This script is licensed under the terms of the MIT license.
Unless otherwise noted, code reproduced herein
was written for this script.

- The Pimoroni Crew -

DISCLAIMER

# script control variables

productname="VLC Radio" # the name of the product to install
scriptname="vlcradio-setup.sh" # the name of this script
spacereq=200 # minimum size required on root partition in MB
debugmode="no" # whether the script should use debug routines
debuguser="none" # optional test git user to use in debug mode
debugpoint="none" # optional git repo branch or tag to checkout
forcesudo="no" # whether the script requires to be ran with root privileges
promptreboot="yes" # whether the script should always prompt user to reboot
mininstall="no" # whether the script enforces minimum install routine
customcmd="yes" # whether to execute commands specified before exit
armhfonly="yes" # whether the script is allowed to run on other arch
armv6="yes" # whether armv6 processors are supported
armv7="yes" # whether armv7 processors are supported
armv8="yes" # whether armv8 processors are supported
raspbianonly="no" # whether the script is allowed to run on other OSes
osreleases=( "Raspbian" ) # list os-releases supported
oswarning=() # list experimental os-releases
osdeny=( "Darwin" "Debian" "Kali" "Kano" "Mate" "PiTop" "RetroPie" "Ubuntu" "Volumio" ) # list os-releases specifically disallowed
pkgdeplist=( "vlc-nox" ) # list of dependencies

FORCE=$1
ASK_TO_REBOOT=false
CURRENT_SETTING=false
MIN_INSTALL=false
FAILED_PKG=false
REMOVE_PKG=false
UPDATE_DB=false

AUTOSTART=~/.config/lxsession/LXDE-pi/autostart
BOOTCMD=/boot/cmdline.txt
CONFIG=/boot/config.txt
APTSRC=/etc/apt/sources.list
INITABCONF=/etc/inittab
BLACKLIST=/etc/modprobe.d/raspi-blacklist.conf
LOADMOD=/etc/modules

# function define

confirm() {
    if [ "$FORCE" == '-y' ]; then
        true
    else
        read -r -p "$1 [y/N] " response < /dev/tty
        if [[ $response =~ ^(yes|y|Y)$ ]]; then
            true
        else
            false
        fi
    fi
}

prompt() {
        read -r -p "$1 [y/N] " response < /dev/tty
        if [[ $response =~ ^(yes|y|Y)$ ]]; then
            true
        else
            false
        fi
}

success() {
    echo -e "$(tput setaf 2)$1$(tput sgr0)"
}

inform() {
    echo -e "$(tput setaf 6)$1$(tput sgr0)"
}

warning() {
    echo -e "$(tput setaf 1)$1$(tput sgr0)"
}

newline() {
    echo ""
}

progress() {
    count=0
    until [ $count -eq $1 ]; do
        echo -n "..." && sleep 1
        ((count++))
    done
    echo
}
sudocheck() {
    if [ $(id -u) -ne 0 ]; then
        echo -e "Install must be run as root. Try 'sudo ./$scriptname'\n"
        exit 1
    fi
}

sysclean() {
    sudo apt-get clean && sudo apt-get autoclean
    sudo apt-get -y autoremove &> /dev/null
}

sysupdate() {
    if ! $UPDATE_DB; then
        echo "Updating apt indexes..." && progress 3 &
        sudo apt-get update 1> /dev/null || { warning "Apt failed to update indexes!" && exit 1; }
        echo "Reading package lists..."
        progress 3 && UPDATE_DB=true
    fi
}

sysupgrade() {
    sudo apt-get upgrade
    sudo apt-get clean && sudo apt-get autoclean
    sudo apt-get -y autoremove &> /dev/null
}

sysreboot() {
    warning "Some changes made to your system require"
    warning "your computer to reboot to take effect."
    echo
    if prompt "Would you like to reboot now?"; then
        sync && sudo reboot
    fi
}

arch_check() {
    IS_ARMHF=false
    IS_ARMv6=false

    if uname -m | grep -q "armv.l"; then
        IS_ARMHF=true
        if uname -m | grep -q "armv6l"; then
            IS_ARMv6=true
        fi
    fi
}

os_check() {
    IS_MACOSX=false
    IS_RASPBIAN=false
    IS_SUPPORTED=false
    IS_EXPERIMENTAL=false
    OS_NAME="Unknown"

    if uname -s | grep -q "Darwin"; then
        OS_NAME="Darwin" && IS_MACOSX=true
    elif cat /etc/os-release | grep -q "Kali"; then
        OS_NAME="Kali"
    elif [ -d ~/.kano-settings ] || [ -d ~/.kanoprofile ]; then
        OS_NAME="Kano"
    elif whoami | grep -q "linaro"; then
        OS_NAME="Linaro"
    elif [ -d ~/.config/ubuntu-mate ];then
        OS_NAME="Mate"
    elif [ -d ~/.pt-os-dashboard ] || [ -d ~/.pt-dashboard ] || [ -f ~/.pt-dashboard-config ]; then
        OS_NAME="PiTop"
    elif command -v emulationstation > /dev/null; then
        OS_NAME="RetroPie"
    elif cat /etc/os-release | grep -q "volumio"; then
        OS_NAME="Volumio"
    elif cat /etc/os-release | grep -q "Raspbian"; then
        OS_NAME="Raspbian" && IS_RASPBIAN=true
    elif cat /etc/os-release | grep -q "Debian"; then
        OS_NAME="Debian"
    elif cat /etc/os-release | grep -q "Ubuntu"; then
        OS_NAME="Ubuntu"
    fi

    if [[ " ${osreleases[@]} " =~ " ${OS_NAME} " ]]; then
        IS_SUPPORTED=true
    fi
    if [[ " ${oswarning[@]} " =~ " ${OS_NAME} " ]]; then
        IS_EXPERIMENTAL=true
    fi
}

raspbian_check() {
    IS_SUPPORTED=false
    IS_EXPERIMENTAL=false

    if [ -f /etc/os-release ]; then
        if cat /etc/os-release | grep -q "/sid"; then
            IS_SUPPORTED=false && IS_EXPERIMENTAL=true
        elif cat /etc/os-release | grep -q "stretch"; then
            IS_SUPPORTED=false && IS_EXPERIMENTAL=true
        elif cat /etc/os-release | grep -q "jessie"; then
            IS_SUPPORTED=true && IS_EXPERIMENTAL=false
        elif cat /etc/os-release | grep -q "wheezy"; then
            IS_SUPPORTED=true && IS_EXPERIMENTAL=false
        else
            IS_SUPPORTED=false && IS_EXPERIMENTAL=false
        fi
    fi
}

apt_pkg_req() {
    APT_CHK=$(dpkg-query -W -f='${Status}\n' "$1" 2> /dev/null | grep "install ok installed")

    if [ "" == "$APT_CHK" ]; then
        echo "$1 is required"
        true
    else
        echo "$1 is already installed"
        false
    fi
}

apt_pkg_install() {
    echo "Installing $1..."
    sudo apt-get --yes install "$1" 1> /dev/null || { inform "Apt failed to install $1!\nFalling back on pypi..." && return 1; }
}

: <<'MAINSTART'

Perform all global variables declarations as well as function definition
above this section for clarity, thanks!

MAINSTART

# checks and init

arch_check
os_check

if [ $debugmode != "no" ]; then
    echo "USER_HOME is $USER_HOME" && newline
    echo "IS_RASPBIAN is $IS_RASPBIAN"
    echo "IS_MACOSX is $IS_MACOSX"
    echo "IS_SUPPORTED is $IS_SUPPORTED"
    echo "IS_EXPERIMENTAL is $IS_EXPERIMENTAL"
    newline
fi

if ! $IS_ARMHF; then
    warning "This hardware is not supported, sorry!"
    warning "Config files have been left untouched"
    newline && exit 1
fi

if $IS_ARMv8 && [ $armv8 == "no" ]; then
    warning "Sorry, your CPU is not supported by this installer"
    newline && exit 1
elif $IS_ARMv7 && [ $armv7 == "no" ]; then
    warning "Sorry, your CPU is not supported by this installer"
    newline && exit 1
elif $IS_ARMv6 && [ $armv6 == "no" ]; then
    warning "Sorry, your CPU is not supported by this installer"
    newline && exit 1
fi

if [ $raspbianonly == "yes" ] && ! $IS_RASPBIAN;then
        warning "This script is intended for Raspbian on a Raspberry Pi!"
        newline && exit 1
fi

if $IS_RASPBIAN; then
    raspbian_check
    if ! $IS_SUPPORTED && ! $IS_EXPERIMENTAL; then
        newline && warning "--- Warning ---" && newline
        echo "The $productname installer"
        echo "does not work on this version of Raspbian."
        echo "Check https://github.com/$gitusername/$gitreponame"
        echo "for additional information and support"
        newline && exit 1
    fi
fi

if ! $IS_SUPPORTED && ! $IS_EXPERIMENTAL; then
        warning "Your operating system is not supported, sorry!"
        newline && exit 1
fi

if $IS_EXPERIMENTAL; then
    warning "Support for your operating system is experimental. Please visit"
    warning "forums.pimoroni.com if you experience issues with this product."
    newline
fi

if [ $forcesudo == "yes" ]; then
    sudocheck
fi

newline
echo "This script will install everything needed to use"
echo "$productname"
newline
warning "--- Warning ---"
newline
echo "Always be careful when running scripts and commands"
echo "copied from the internet. Ensure they are from a"
echo "trusted source."
newline

echo -e "Installing dependencies..."

for pkgdep in ${pkgdeplist[@]}; do
    if apt_pkg_req "$pkgdep"; then
        sysupdate && apt_pkg_install "$pkgdep"
    fi
done

echo -e "\nInstalling daemon..."

sudo cp ./phatbeatd/etc/init.d/phatbeatd /etc/init.d/
sudo cp ./phatbeatd/usr/bin/phatbeatd /usr/bin/
sudo chmod +x /usr/bin/phatbeatd

sudo cp ./vlcd/etc/init.d/vlcd /etc/init.d/
sudo cp ./vlcd/usr/bin/vlcd /usr/bin/
sudo chmod +x /usr/bin/vlcd

sudo systemctl daemon-reload
sudo systemctl enable vlcd
sudo systemctl enable phatbeatd

echo -e "\nCopying default playlist to /etc/vlcd/"
sudo mkdir /etc/vlcd &> /dev/null
sudo cp ./vlcd/etc/vlcd/default.m3u /etc/vlcd/
sleep 1

success "\nAll done!\n"
echo -e "Enjoy your new $productname!\n"

if [ $promptreboot == "yes" ] || $ASK_TO_REBOOT; then
    sysreboot
fi

exit 0
