#!/bin/sh -x
# Cluster HAT example create-pX.sh file
# http://clusterhat.com/

IN=2016-05-27-raspbian-jessie-lite.img
VER=2016-05-27-1
CONFIGDIR="/usr/share/clusterhat"

cd <setup-dir>

cp build/ClusterHAT-${VER}-controller.img build/ClusterHAT-${VER}-p1.img
cp build/ClusterHAT-${VER}-controller.img build/ClusterHAT-${VER}-p2.img
cp build/ClusterHAT-${VER}-controller.img build/ClusterHAT-${VER}-p3.img
cp build/ClusterHAT-${VER}-controller.img build/ClusterHAT-${VER}-p4.img


LOOP=`losetup -f`
losetup $LOOP build/ClusterHAT-${VER}-p1.img
sleep 5
kpartx -av $LOOP
sleep 5
mount `echo $LOOP|sed s#dev#dev/mapper#`p2 mnt
mount `echo $LOOP|sed s#dev#dev/mapper#`p1 mnt/boot
echo -n "dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet init=/sbin/reconfig-clusterhat p1" > mnt/boot/cmdline.txt
umount mnt/boot
umount mnt
kpartx -dv $LOOP
losetup -d $LOOP

LOOP=`losetup -f`
losetup $LOOP build/ClusterHAT-${VER}-p2.img
sleep 5
kpartx -av $LOOP
sleep 5
mount `echo $LOOP|sed s#dev#dev/mapper#`p2 mnt
mount `echo $LOOP|sed s#dev#dev/mapper#`p1 mnt/boot
echo -n "dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet init=/sbin/reconfig-clusterhat p2" > mnt/boot/cmdline.txt
umount mnt/boot
umount mnt
kpartx -dv $LOOP
losetup -d $LOOP

LOOP=`losetup -f`
losetup $LOOP build/ClusterHAT-${VER}-p3.img
sleep 5
kpartx -av $LOOP
sleep 5
mount `echo $LOOP|sed s#dev#dev/mapper#`p2 mnt
mount `echo $LOOP|sed s#dev#dev/mapper#`p1 mnt/boot
echo -n "dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet init=/sbin/reconfig-clusterhat p3" > mnt/boot/cmdline.txt
umount mnt/boot
umount mnt
kpartx -dv $LOOP
losetup -d $LOOP

LOOP=`losetup -f`
losetup $LOOP build/ClusterHAT-${VER}-p4.img
sleep 5
kpartx -av $LOOP
sleep 5
mount `echo $LOOP|sed s#dev#dev/mapper#`p2 mnt
mount `echo $LOOP|sed s#dev#dev/mapper#`p1 mnt/boot
echo -n "dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet init=/sbin/reconfig-clusterhat p4" > mnt/boot/cmdline.txt
umount mnt/boot
umount mnt
kpartx -dv $LOOP
losetup -d $LOOP

