#!/usr/bin/env bash

# Script to build Ubuntu bootable SD card from file

DEBUGMODE=0

# Functions

# Check required commands
function check_command {
	type -P $1 &>/dev/null || fail "Unable to find $1, please install it and run this script again."
}

# Fail
function fail(){
	tput setaf 1; echo "Failure: $*" && tput sgr0
	exit 1
}

# Success
function success(){
	tput setaf 2; echo "$*" && tput sgr0
}

# Pause
function pause(){
	read -p "Press any key to continue..."
	echo
}

# Select Ubuntu Image
function image(){
	# clear
	echo	"======================================================================================="
	success "This tool will build an Ubuntu bootable SD card from img file in your Downloads folder."
	echo	"======================================================================================="
	pause


	Ubuntu=$(find ~/Downloads -type f -name "*ubuntu*.img" | sort -r)

	if [ -z "$Ubuntu" ]; then
		ZIPPED=$(find ~/Downloads -type f -name "*ubuntu*.zip")
		if [ -z "$ZIPPED" ]; then
			fail "Could not find any Ubuntu images in your Downloads folder."
		else
			echo "List of compressed Ubuntu images"
			echo "$ZIPPED"
			fail "Must uncompress image first."
		fi
	else
		NUMIMAGES=$(echo "$Ubuntu" | wc -l)
		success Found $NUMIMAGES Ubuntu images found in Downloads.
		echo
		echo "$Ubuntu"
		# echo "List of Ubuntu images found in Downloads:"
		success "$Ubuntu"
		echo

		if [ "$NUMIMAGES" -gt "1" ]; then
			START=1
			for (( COUNT=$START; COUNT<=$NUMIMAGES; COUNT++ ))
			do
				# echo "====================================================="
				# echo \#$COUNT
				IMAGE=$(echo "$Ubuntu" | nl | grep -w $COUNT | cut -f2)
				echo "Image: "$IMAGE
				read -rp "Use this Ubuntu image? (y/n) " REPLY
				echo
				if [[ $REPLY =~ ^[Yy]$ ]]; then
					SELECTED="Y"
					Ubuntu=$IMAGE
					if [[ $DEBUGMODE = "1" ]]; then
						echo Image: $IMAGE
						echo Ubuntu: $Ubuntu
					fi
					break
				fi

				# if [[ $REPLY =~ ^[Nn]$ ]]; then
				# 	echo
				# 	read -rp "Enter full path to Ubuntu image: " REPLY
				# 	Ubuntu=$REPLY
				# fi
			done

			if ! [[ $SELECTED =~ "Y" ]]; then
				fail "Must select at least one Ubuntu image!"
			fi
		fi
	fi
}

# Select Mounted Disk
function disk(){
	echo
	echo	"================================================================================================="
	success "List of mounted disks:"
	echo
	df -lH
	success "(The Filesystem column is the path to the disk.)"
	echo	"================================================================================================="
	# ls -fl /Volumes/
	echo
	echo "Type the full Filesystem path to disk for your Raspberry Pi MicroSD Card:"
	echo "Example: /dev/disk5"
	read DISK
	if [ -z "$DISK" ]; then
		fail "Must enter full path to disk to format!"
	fi
	echo	"================================================================================================="
	tput setaf 1; echo "WARNING THE NEXT STEP WILL ERASE THE DISK!!!"
	echo	"================================================================================================="
	read -rp "Proceed to erase and format \"$DISK\" with Ubuntu image? (y/n) " REPLY && tput sgr0
	echo
	if [[ $REPLY =~ ^[Yy]$ ]]; then
		echo "Unmounting" $DISK
		UNMOUNT=$(diskutil unmountDisk $DISK 2>&1)
		if echo "$UNMOUNT" | grep -q "fail"; then
			fail "$UNMOUNT"
			exit 1
		fi
		echo "Formatting with FAT32"
		FORMAT=$(sudo diskutil eraseDisk FAT32 RASPBERRYPI MBRFormat $DISK 2>&1)
		if echo "$FORMAT" | grep -q "fail"; then
			fail "$FORMAT"
			exit 1
		fi
		UNMOUNT=$(diskutil unmountDisk $DISK 2>&1)
		if echo "$UNMOUNT" | grep -q "fail"; then
			fail "$UNMOUNT"
			exit 1
		fi
		if [[ $UNMOUNT = "dd: $DISK: Resource busy" ]]; then
			UNMOUNT=$(diskutil unmountDisk $DISK)
		fi
		if [[ $DEBUGMODE = "1" ]]; then
			echo
			echo "Ubuntu Image: "; success "$Ubuntu"
			echo
			echo "Filesystem path: "; success "$DISK"
		fi
		echo
		# tput setaf 1; echo "CONFIRM AND FORMAT DISK?"
		# pause
		echo "================================================================================================="
		echo "Installing the Raspberry Pi image... (this may take some time)"
		echo "================================================================================================="

		start=$(date +%s)
		pause
		DD=$(eval sudo dd bs=1m if="$Ubuntu" of="$DISK" 2>&1)
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
	echo "Done!"
}

check_command "dd"
check_command "diskutil"
image
disk
