# How to build your own Raspberry Pi NAS

_Captured: 2017-05-06 at 17:00 from [www.techradar.com](http://www.techradar.com/how-to/computing/how-to-build-your-own-raspberry-pi-nas-1315968)_

![](http://cdn.mos.cms.futurecdn.net/17ce70940ce402b09655c88585ca06c3-320-80.jpg)

Do you have a bunch of USB disks that you juggle between your various computers? Did you know that you can plug all of them into a Raspberry Pi, which you can then use as a network attached storage (NAS) box?

Using the Raspberry Pi as an always-on NAS box sounds like a wonderful use of the silent little device. However, setting it up as one used to be an involved process. That's until the Debian-based OpenMediaVault (OMV) distro decided to roll out a version specifically tuned to the Raspberry Pi.

Once it's up and running, you can configure and manage the distro using its browser-based administration interface.

You can then use the USB ports on the Raspberry Pi to attach USB disks, which are then made available to your entire network for storage. Remember that for best performance, make sure you use self-powered removable disks. You can use the disks attached to the OpenMediaVault NAS individually, or assemble them in a software RAID array.

The distro has ample options to manage other advanced aspects of a NAS distro.

![Build NAS](http://cdn.mos.cms.futurecdn.net/7a18961e49f06a77d75fea54db7da01b-320-80.jpg)

### Get installed

To get started, download the [Raspberry Pi version of OpenMediaVault](http://www.openmediavault.org). The distro has separate releases for the Raspberry Pi 2 and the original B/B+ models, so ensure you grab the correct one. Then extract the .img file from the download and transfer it on to an SD card with

**sudo dd if= /omv_1.17_rpi_rpi2.img of=/dev/sdb**

replacing /dev/sdb with the location of your SD card. Now boot the Raspberry Pi with the freshly baked SD card. There's no installation involved and you can start configuring the distro as soon as it boots up. You can access its browser-based interface on the IP address of the Raspberry Pi - such as 192.168.3.111.

You're asked to authenticate yourself, which you can do using the default credentials for the administrator - admin:openmediavault. However, you should change this default as soon as you log in. Head to System > General Settings in the navigation bar on the left, switch to the Web Administrator Password tab and enter the new password in the appropriate text boxes.

You can also use the System menu to configure several aspects of the NAS server, such as the server's date and time, enable plugins and keep the system updated.

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/03cbe60908fbcee94e17a981194a50b0-320-80.jpg)

### Add storage

Once it's up and running, plug one or multiple USB disks into the Raspberry Pi. Head to Storage > Physical Disks and click the Scan button to make OpenMediaVault aware of the disks.

Then use the Wipe button to clean the disks individually. If you've inserted multiple disks, OpenMediaVault can even tie them into a software RAID (see walkthrough over the page). OpenMediaVault supports multiple RAID levels and each requires a different number of disks.

For example, the default RAID level 5 requires a minimum of three disks, while RAID 1, which mirrors data across drives, only needs a minimum of two. If you don't plan to use the inserted USB disk inside a RAID array, then after you've erased a drive, head to Storage > File Systems to create a filesystem on the drive.

Here click the Create button and use the pull-down menu to select the device you wish to format. By default, the drives are formatted as Ext4 but you can select a different filesystem using the pull-down menu. Besides Ext4, OpenMediaVault supports the Ext3, XFS and JFS filesystems.

Repeat the process to create a filesystem on all of the attached USB disks. After creating the filesystem, select a drive and then click the Mount button to bring them online.

### Adding Users

Before you can store data on the NAS device, you have to create one or more users. To do this, head to Access Rights Management > User. The Add button on this page is a pulldown menu that enables you to either add individual users or import a bunch of users by adding them in the specified format.

When adding an individual user, you can also add them to an existing group. By default, all users are added to the Users group. If you want users to have their own home directories in the OpenMediaVault server, switch to the Settings tab and tick the box to enable the home directory for the user.

You must also specify the location for the home directory by selecting an existing shared folder on the NAS server or creating a new one.

### Shares and permissions

The next step is to define a shared folder. The chief consideration while adding one is whether the NAS will be used by multiple users or a single individual. In case you're going to be sharing the NAS storage space with multiple users, you can define several folders, each with different user permissions.

To add a folder, head to Access Rights Management > Shared Folders and click the Add button. In the dialog box that pops up, select the volume that'll house the folder from the pull-down list. Then give the shared folder a name, such as Backup, and enter the path of the folder you wish to share, such as backup/.

OpenMediaVault creates the folder if it doesn't already exist. You can also optionally add a comment to describe the type of content the folder will hold.

Pay close attention to the Permissions setting. By default, OpenMediaVault only allows the administrator and any users you've added to read and write data to this folder, while others can only read its contents.

This is a pretty safe default for most installations, but the distro offers several permutations and combinations of permissions that you can select from the pull-down menu.

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/a939d07e62fc4d77ad0cab7db9c346b7-320-80.jpg)

> _Fine-tune permissions_

Even if you select the default Permissions setting when creating folders, which lets all users read and write data to the folder, you can fine-tune the access permissions and disable certain users from accessing or modifying the contents of a particular folder.

For this, after adding a user, head to the Shared Folders section, select the folder you want to control access to and click the Privileges button.

This opens a window with a list of the users you've added, along with tickboxes for controlling their access to that folder, so for example you can allow read-only access. With the users and shared folders set up, you're now ready to share the NAS storage with your network.

Follow the walkthrough to enable a network service that people can use to access the shared folders on the NAS. OpenMediaVault supports various popular protocols and services, including NFS, SMB/CIFS, FTP, TFTP, SSH, rsync and more.

Once you've created a network share, you can access the shared folders from anywhere on the network, irrespective of whether they reside on an individual disk or a RAID array.

You can either use your file manager's built-in Network feature to access the network shares, or enter the IP address of the NAS device in the location area, such as smb://192.168.3.111. You're prompted for a username and password before you can access the folders - unless, of course, you have marked them as public when adding them via Samba.

Enter the credentials of a user who has the appropriate permission to access the folder. After they've been verified, OMV mounts the shared folder. You can now upload files into the shared folder or delete them, if you have the permission, just as in the case of a regular folder.

It might take a little getting used to, but OpenMediaVault is a wonderfully versatile NAS option that helps you exploit the true potential of the Raspberry Pi.

  


You can flesh out OpenMediaVault and add a bunch of features to make it more usable. The distribution supports quite a handful of official and third-party plugins, which you can install and enable according to your needs and requirements.

To browse a list of all the officially supported plugins, head to System > Plugins. The page lists over 40 plugins, which are divided into categories such as Administration, Backup, Downloaders, Filesystems, Network and so on. One useful option is the downloader plugin, which can download files into the NAS, and includes several downloaders such as Aria2 and Youtube-DL.

This plugin is well complemented by the transmission plugin, which downloads torrents via the Transmission app. You should also enable the clamav plugin, which gives you the ability to scan your NAS for viruses.

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/524e87e4debf6419c8eca1b5f3f5bce7-320-80.jpg)

To enable a plugin, simply click on the corresponding checkbox. You can even toggle multiple plugins in one go. After selecting the plugins you wish to enable, click the Install button. OpenMediaVault then downloads the plugins from the Raspbian repositories via the APT package management system and enables you to track its progress.

Depending on the number of plugins you're installing and their size, this process could take some time to complete.

Once the plugins have been downloaded and installed, they append the OpenMediaVault administration interface and create an entry for themselves.

For example, the downloader plugin installs itself under Server > Downloader. Switch to the new section when you want to configure different aspects of the plugin. Each plugin has its own configurable elements.

### Stream music

If you've stored music on the NAS, wouldn't it be really cool if you could stream it across the network straight from the NAS itself? Using the forked-daapd plugin, you can do just that. To use the plugin, just install it like any other; this adds a new entry under the Services section, labelled iTunes/DAAP.

Before you can stream music, you need to configure the plugin by pointing it to the shared folder on the NAS that contains the music files. Head to the plugin's page and use the Shared Folder drop-down menu to select the folder that houses the music.

Once you've saved the changes, use a player such as Rhythmbox, Amarok, Banshee and so on, which will automatically pick up the DAAP server running on your NAS and enable you to listen to the tracks on the NAS.

Use the DAAP Media Player app to listen to the music on an Android device. In addition, you can also install the MiniDLNA plugin to connect to your NAS from DLNA clients. Just as with DAAP, after installing the MiniDLNA plugin, you have to head to Services > DLNA > Shares, and click on Add to point to the shared folder that contains the music.

You can then use the BubbleUPnP app to convert your Android phone into a DLNA compatible device, so that it can browse the library and stream music to and from your now-DLNA-compatible NAS.

### Set up a RAID

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/b6f46c01445512264aa8fd0dd9b6962d-320-80.jpg)

### 1\. Select RAID Level

If you wish to arrange the disks into a RAID device, head to Storage > RAID Management and click the 'Create' button. In the dialog box that pops up, select the devices you want to use in the RAID, as well as the RAID level. Then enter the name you wish to use for the RAID device in the space provided, and click the 'Save' button.

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/f984ad4e1921dccd32ea3365c62f08e0-320-80.jpg)

### 2\. Initialise the RAID

After you've created a RAID, OMV asks you to wait until the RAID has been initialised before you proceed to the next step and create a filesystem. You also get a notification to save the changes in order for them to take effect. The RAID Management page now lists the newly created RAID device.

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/f9a6699c315d17a557d009551fe6f14c-320-80.jpg)

> _3. Create a filesystem_

To use the RAID array, you need to create a filesystem. Head to Storage > Filesystems and click the 'Create' button. In the dialog box that pops up, select the device you want to format using the pull-down menu, which will have the RAID device you've just created in the list. Then label it and select one of the supported filesystems.

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/9197df666fcf4b30522a4fcdf780a704-320-80.jpg)

### 4\. Mount the device

After the filesystem has been created and the disk has been initialised, the RAID device will be listed with other devices in the Storage > Filesystems page. To use the drive, select it, then click the 'Mount' button to bring the disk online. You can add new disks to a RAID device by selecting the Storage > RAID Management > Grow option.

### Enable shares

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/f9add19f79e787945a41538cf76e27a2-320-80.jpg)

### 1\. Enable Samba

OpenMediaVault supports several sharing protocols but we'll use the popular SMB protocol commonly known as Samba, which works across devices. To activate the service, head to Services > SMB/CIFS and click the 'Enable'. The other settings mentioned on the page are optional, so leave them for now. When you're done, click the 'Save' button.

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/2364a0dfa24144f50de359f783113da2-320-80.jpg)

### 2\. Add folders

Next, you have to add the shared folders as Samba shares. To do this, switch to the Shares tab and click the 'Add' button. In the window that pops up, select a shared folder from the pull-down list or click on the '+' button to create a new one. You also have to give the folder a name, which identifies the folder on the network.

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/8e2572870cf70cfbdf9374b1d22e9dd5-320-80.jpg)

### 3\. Define permissions

When adding a Samba folder, OpenMediaVault makes sure it follows the permissions defined when you created the shared folder. Select the Guests Allowed option from the Public pull-down menu to make the folders public. Also, if you click the 'Set Read Only' checkbox, OpenMediaVault ensures that no user can modify the contents of the folder.

![How to build your own Raspberry Pi NAS](http://cdn.mos.cms.futurecdn.net/743bbca4a9b50c827b70ddecdc12950a-320-80.jpg)

### 4\. Other settings

Take some time to review the other settings on the page. One useful option that isn't enabled by default is the Recycle Bin. When this is enabled, any file that's deleted from the NAS is moved into a virtual Recycle Bin inside the shared folder. Save the configuration when you've added them all to restart the Samba service.

  * Enjoyed this article? Expand your knowledge of Linux, get more from your code, and discover the latest open source developments inside Linux Format. [Read our sampler today and take advantage of the offer inside.](http://issuu.com/futurepublishing/docs/lxf204.sampler_tr?e=1191357/31271343)
