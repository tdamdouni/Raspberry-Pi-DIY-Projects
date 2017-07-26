#!/usr/bin/env bash

# Script to build Raspbian bootable SD card from Raspbian img file

DEBUGMODE=0

# Functions

# Check required commands
function check_command {
	type -P $1 &>/dev/null || fail "Unable to find $1, please install it and run this script again."
}

# Alert
function alert(){
	tput setaf 1; echo "$*" && tput sgr0
}

# Fail
function fail(){
	tput setaf 1; echo "Failure: $*" && tput sgr0
	exit 1
}

# Pause
function pause(){
	read -p "Press any key to continue..."
	echo
}

# Success
function success(){
	tput setaf 2; echo "$*" && tput sgr0
}

# Unmount
function unmount(){
	echo "Unmounting" $DISK "..."
	UNMOUNT=$(diskutil unmountDisk $DISK 2>&1)
	if echo "$UNMOUNT" | grep -q "fail"; then
		fail "$UNMOUNT"
		exit 1
	fi
}


# Select Raspian Image
function image(){
	# clear
	echo	"================================================================================================================="
	success "This tool will build a Raspbian bootable SD card from an uncompressed Raspbian img file in your Downloads folder."
	echo	"================================================================================================================="
	pause

	RASPBIAN=$(find ~/Downloads -type f -name "*raspbian*.img" | sort -r)

	if [ -z "$RASPBIAN" ]; then
		ZIPPED=$(find ~/Downloads -type f -name "*raspbian*.zip")
		if [ -z "$ZIPPED" ]; then
			fail "Could not find any Raspbian img files in your Downloads folder."
		else
			echo "Found compressed Raspbian img:"
			echo "$ZIPPED"
			fail "Must uncompress img first."
		fi
	else
		NUMIMAGES=$(echo "$RASPBIAN" | wc -l)
		success Found $NUMIMAGES Raspbian img files in Downloads.
		echo
		# echo "List of Raspbian images found in Downloads:"
		success "$RASPBIAN"
		echo
		# echo Number of images found: $NUMIMAGES

		if [ "$NUMIMAGES" -gt "1" ]; then
			START=1
			for (( COUNT=$START; COUNT<=$NUMIMAGES; COUNT++ ))
			do
				# echo "====================================================="
				# echo \#$COUNT
				IMAGE=$(echo "$RASPBIAN" | nl | grep -w $COUNT | cut -f2)
				echo "Image: "$IMAGE
				read -rp "Use this Raspbian img file? (y/n) " REPLY
				echo
				if [[ $REPLY =~ ^[Yy]$ ]]; then
					SELECTED="Y"
					RASPBIAN=$IMAGE
					if [[ $DEBUGMODE = "1" ]]; then
						echo Image: $IMAGE
						echo Raspbian: $RASPBIAN
					fi
					break
				fi

				# if [[ $REPLY =~ ^[Nn]$ ]]; then
				# 	echo
				# 	read -rp "Enter full path to Raspbian image: " REPLY
				# 	RASPBIAN=$REPLY
				# fi
			done

			if ! [[ $SELECTED =~ "Y" ]]; then
				fail "Must select at least one Raspbian img file!"
			fi
		fi
	fi
}

# Select Mounted Disk
function disk(){
	echo
	echo "================================================================================================="
	success "List of mounted disks:"
	echo
	df -lH
	success "(The Filesystem column is the path to the disk.)"
	echo "================================================================================================="
	# ls -fl /Volumes/
	echo
	echo "Type the full Filesystem path to disk for your Raspberry Pi MicroSD Card:"
	echo "Example: /dev/disk5"
	read DISK
	if [ -z "$DISK" ]; then
		alert "Must enter full path to disk to format!"
		echo
		echo "Type the full Filesystem path to disk for your Raspberry Pi MicroSD Card:"
		echo "Example: /dev/disk5"
		read DISK
	fi
	if [ -z "$DISK" ]; then
		fail "Must enter full path to disk to format!"
	fi
	alert "================================================================================================="
	alert "WARNING THE NEXT STEP WILL ERASE THE SD CARD!!!"
	alert "================================================================================================="
	tput setaf 1; read -rp "Proceed to erase and format \"$DISK\" with Raspbian image? (y/n) " REPLY && tput sgr0
	echo
	if [[ $REPLY =~ ^[Yy]$ ]]; then
		unmount
		echo "Formatting with FAT32..."
		FORMAT=$(sudo diskutil eraseDisk FAT32 RASPBERRYPI MBRFormat $DISK 2>&1)
		if echo "$FORMAT" | grep -q "fail"; then
			fail "$FORMAT"
			exit 1
		fi
		unmount
		if [[ $UNMOUNT = "dd: $DISK: Resource busy" ]]; then
			UNMOUNT=$(sudo diskutil unmountDisk $DISK)
		fi
		if [[ $DEBUGMODE = "1" ]]; then
			echo
			echo "Raspbian Image: "; success "$RASPBIAN"
			echo
			echo "Filesystem path: "; success "$DISK"
		fi
		echo
		# tput setaf 1; echo "CONFIRM AND FORMAT DISK?"
		# pause
		echo "================================================================================================="
		success "Installing the Raspberry Pi image to SD Card... (this may take some time)"
		alert "DO NOT REMOVE THE SD CARD!!!"
		echo "================================================================================================="
		start=$(date +%s)
		if [[ $DEBUGMODE = "1" ]]; then
			echo $start
			pause
		fi
		DD=$(eval sudo dd bs=1m if="$RASPBIAN" of="$DISK" 2>&1)
		if [[ $DEBUGMODE = "1" ]]; then
			echo "DD is done..."
		fi
		if echo "$DD" | grep -q "unknown"; then
			fail "$DD"
			exit 1
		fi
		dur=$(echo "$(date +%s) - $start" | bc)
		printf "Execution time: %.2f seconds\n" $dur
		echo "$DD"
	else
		fail "Cancelled."
	fi
	success "Done!"
	osascript -e 'tell app "Terminal" to display dialog "Raspbian bootable SD card ready!"'
	unmount
}

check_command "dd"
check_command "diskutil"
image
disk
