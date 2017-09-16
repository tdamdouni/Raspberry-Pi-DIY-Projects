#!/bin/bash -x

IN=2017-03-02-raspbian-jessie-lite.img
VER=2017-03-02-lite-1

CONFIGDIR="/usr/share/clusterhat"

cd <setup-dir>

# build - directory containing modified images
# files - directory containing unmodified Raspbian images

if [ ! -f build/ClusterHAT-${VER}-controller.img ];then
 cp files/$IN build/ClusterHAT-${VER}-controller.img
fi

# Make sure we have kpartx
which kpartx >/dev/null 2>&1
if [ $? -eq 1 ];then
 apt-get install -u kpartx
fi

LOOP=`losetup -f --show $LOOP build/ClusterHAT-${VER}-controller.img`
sleep 5
kpartx -av $LOOP
sleep 5

mount `echo $LOOP|sed s#dev#dev/mapper#`p2 mnt
mount `echo $LOOP|sed s#dev#dev/mapper#`p1 mnt/boot

# Get any updates / install and remove pacakges
chroot mnt apt-get update
chroot mnt apt-get -y purge wolfram-engine # PIXEL only
chroot mnt /bin/bash -c 'APT_LISTCHANGES_FRONTEND=none apt-get -y dist-upgrade'
chroot mnt apt-get -y install bridge-utils wiringpi screen minicom

# Disable APIPA addresses on ethpiX and eth0
echo -e "# ClusterHAT\ndenyinterfaces eth0 ethpi1 ethpi2 ethpi3 ethpi4" >> mnt/etc/dhcpcd.conf

# Ensure we're going to do a text boot (on LITE only)
chroot mnt systemctl set-default multi-user.target

# Enable uart (needed for Pi Zero W)
lua - enable_uart 1 mnt/boot/config.txt <<EOF > mnt/boot/config.txt.bak
local key=assert(arg[1])
local value=assert(arg[2])
local fn=assert(arg[3])
local file=assert(io.open(fn))
local made_change=false
for line in file:lines() do
  if line:match("^#?%s*"..key.."=.*$") then
    line=key.."="..value
    made_change=true
  end
  print(line)
end

if not made_change then
  print(key.."="..value)
end
EOF
mv mnt/boot/config.txt.bak mnt/boot/config.txt

# Setup a getty on the gadget serial port
chroot mnt ln -fs /lib/systemd/system/getty@.service \
/etc/systemd/system/getty.target.wants/getty@ttyGS0.service

# Change the hostname to "controller"
sed -i "s#^127.0.1.1.*#127.0.1.1\tcontroller#g" mnt/etc/hosts
echo "controller" > mnt/etc/hostname

# Get the cluster HAT software/config files
wget -O - --quiet http://dist.8086.net/clusterhat/clusterhat-files-latest.tgz | chroot mnt tar -zxvC /

# Copy network config files
cp -f mnt/$CONFIGDIR/interfaces.c mnt/etc/network/interfaces

# Disable the auto filesystem resize
sed -i 's/ quiet init=.*$//' mnt/boot/cmdline.txt

# Setup config.txt file
C=`grep -c "dtoverlay=dwc2" mnt/boot/config.txt`
if [ "x$C" = "x0" ];then
 echo -e "# Load overlay to allow USB Gadget devices\n#dtoverlay=dwc2" >> mnt/boot/config.txt
fi

rm -f mnt/etc/ssh/*key*
chroot mnt apt-get -y autoremove --purge
chroot mnt apt-get clean


umount mnt/boot
umount mnt

kpartx -dv $LOOP
losetup -d $LOOP

