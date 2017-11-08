#!/bin/bash

printMsg(){
echo "===================================================="
echo "= " $1
echo "===================================================="
}

# Set up a ramdrive for temp files/inter process comms
printMsg "Enabling ram disk in fstab."
if [ ! -d "/mnt/ramdisk" ]; then
        mkdir /mnt/ramdisk
        chown pi:pi /mnt/fstab
fi

if grep -q "/mnt/ramdisk" /etc/fstab; then
echo "/mnt/ramdisk already in fstab"
else
cat >> /etc/fstab << EOF
tmpfs       /mnt/ramdisk tmpfs   nodev,nosuid,noexec,nodiratime,size=1M   0 0
EOF
fi
