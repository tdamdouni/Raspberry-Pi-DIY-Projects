# How to Set Up a File-Syncing Dropbox Clone You Control

_Captured: 2016-12-30 at 00:57 from [lifehacker.com](http://lifehacker.com/5821145/how-to-set-up-a-file-syncing-dropbox-clone-you-control)_

File syncing is a godsend when you work on multiple computers or devices and want to make sure you have the most up-to-date files wherever you log in. While [online services like Dropbox](http://lifehacker.com/5818908/dropbox-vs-the-alternatives-which-online-syncing-service-is-right-for-you) may be the most convenient options, there are plenty of reasons you may want to "roll your own cloud" and sync your files to your own web server or just on your local network. Below, we'll detail how to set up a Dropbox clone, complete with instantaneous, encrypted syncs, cloud backups, and file versioning, using cross-platform software [GoodSync](http://goodsync.com).

### Why Set Up Your Own Syncing System?

**Control**. The biggest reason many of us might go looking for Dropbox alternatives is lack of control or a feeling of uncertainty with things like [odd changes in terms of service](http://lifehacker.com/5819430/should-i-be-worried-about-the-change-to-dropboxs-terms-of-service) implying the syncing service "owns" our files. A self-hosted solution will give you more control and peace of mind than most sign-up-and-forget online services can offer.

**Flexibility and precision**. Instead of selecting just one folder to keep up to date, you can, if you choose, select several with GoodSync. You can schedule multiple syncing jobs for different purposes: sync your work and home documents folders every time a file changes, for example, while syncing the music folder on your laptop with your home server every Wednesday at 5pm in another.

**Space and savings**. Finally, if you're paying for web hosting service already, you can make better use of available free space by using it to store your own files. (Note: not all web hosts approve of you using their web space for just backups or file storage, so check with yours first; [Dreamhost](http://www.dreamhost.com/unlimited.html) is one provider that offers dedicated space for personal storage as well as hosting). You could also rent cheap server space from somewhere like Amazon S3.

### Why GoodSync?

We're going to use GoodSync to sync files to your web host via SFTP (SFTP is a file transfer protocol like FTP except it's secure, since it encrypts all your data and commands during the transfers). It works on Windows and Mac (and can be run off a portable drive) and has a variety of types of devices you can sync to (including network shares, SFTP, WebDAV, Amazon S3, Google Docs if you're a paid account user, SkyDrive, and Windows Mobile). GoodSync is also developed by the makers of Roboform, one of our [favorite password managers](http://lifehacker.com/5042616/five-best-password-managers). You can find other alternatives to create a Dropbox clone (see the end of the post), but GoodSync is my preferred option.

The free version of GoodSync (for personal use) allows up to three sync jobs after the trial period (a "job" in GoodSync includes a folder and a specific sync type; for our Dropbox clone, you'll just need to set up one job) and up to 100 files/folders in each sync job, while the pro version removes these limitations and costs $29.95 (one time fee for the application). You might not need more than the free version if you don't have a lot of files to sync. One sync job can keep your local and remote folders in sync instantaneously. Realistically, if you're building a Dropbox clone, the $30 the paid version is a good investment, especially compared to paying a monthly fee for more than 2GB on Dropbox.

### How to Set Up Your Dropbox Clone with GoodSync

The first thing you'll need to do, besides [downloading](http://www.goodsync.com/download) and installing GoodSync, is to make sure you have access to the locations you want to sync with.

**SFTP on your web host:** In this example, we're using [SFTP](http://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) to transfer our files to a web host because it's commonly available as an option on most web hosts; it works just like FTP except the transfer is run over SSH. Some hosts require you to request SFTP or SSH access or use a different port than the typical port 22, so you may need to contact your web host if you run into errors connecting to your server with your usual FTP login information. If you can't get SFTP access, see if your host offers WebDAV (check your hosting control panel for the option), which also has more security than plain FTP, but SFTP may be quicker. If you don't already have a web host, take a look at [these five popular options](http://lifehacker.com/5545568/five-best-personal-web-hosts).

**SFTP on your home server:** If you'd prefer to keep your files on your own computers at all times, you can set up SFTP on your own computer--like a home server. Our [guide to turning your computer into a remote access media server](http://lifehacker.com/5797582/how-to-turn-your-computer-into-the-ultimate-remote-access-media-server) details enabling SFTP on Windows and Mac.

### Step 1. Create a Job

When you first run GoodSync, you'll be prompted to create a new job. As mentioned above, this is simply the sync task (e.g., sync office folder to home folder instantaneously). Give the job a name (e.g., Sync home docs to SFTP backup folder) and select two-way synchronization (backup will just copy the files to your remote folder, not keep your local files updated).

### Step 2. Select Left and Right Folders for Your New Job

In this step, we're going to point our local folder to the SFTP server that's acting as our cloud server. So, for your Dropbox clone, create a new folder, perhaps called GoodSync, that's going to act as the equivalent of your old Dropbox folder. On the left panel, browse to and select that folder. Then click on the right panel to select the SFTP server you wish to sync to.

For SFTP, enter in the address of your web site (or your local SFTP server) as well as your username and password. If your SFTP server uses a non-standard port, enter it at the end of the url address, e.g.: `sftp://mywebsite:2222`.

Once GoodSync connects to your SFTP server, navigate to the folder that you want to sync to or create a new one. For first time setup on your web host, I recommend creating a folder above the "www" folder so it's not accessible from the web.

Note: There's very little difference in this process if you wanted to sync to a different device/location, but that's beyond our scope here.

### Step 3. Click Analyze to Compare the Changes

After your two folder locations are selected, click the Analyze button and GoodSync will compare the files in both locations to see the differences. Once you get a list of all your folders and files in both locations, you can choose to exclude specific files or folders from the syncing process. Although it only took a few minutes for me, it can feel very slow, so be prepared to get up for some coffee or something while the program does its thing.

### Step 4. Finalize Your Sync Job and Get Syncing

Finally, GoodSync will offer you a proposed, detailed syncing solution, indicating which files will be copied to which location. Here's an illustration of what the symbols mean:

![](https://i.kinja-img.com/gawker-media/image/upload/s--qE9xVLEQ--/c_fit,fl_progressive,q_80,w_320/18rt97kau6le4gif.jpg) ![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

Since we're setting up an instant, automated system, click Auto to sync files as soon as they change, a la Dropbox. Options you may want to enable here include:

**General**: Here you can set file versioning (default is 30) to keep deleted or overwritten files for file versioning in a saved folder--this is enabled by default.

**Auto**: This is the main scheduling tab. Check the Sync checkbox beside "on file change" to make syncing happen immediately when files or folders change, like Dropbox does. GoodSync says that it automatically detects changes in files by comparing current file status to the stored file status, so no system-based monitoring is required.

**Filters**: Set preferences for files you don't want included in the job based on name, size, or modification time.

Once your options are set and you hit OK, GoodSync will sync your files according to your settings. Keep in mind that the initial syncing/backup can take a while, but after that you should have GoodSync working like a legit, solid alternative to Dropbox and other online syncing services--with even more flexibility and capabilities.

### Disadvantages

There are a few downsides to this approach. As you can see, the program is more complex and the many options might feel overwhelming (or freeing, depending on your perspective).

The main issue is there's no built-in sharing or collaboration features built-in, like Dropbox and other online syncing services have. Although you can certainly share files you've stored on a cloud server with a friend, it's not as convenient as, say, right-clicking on a file and generating sharable public links or adding people who can access a folder.

Finally, depending on the service and programs you use, file syncing performance can also differ greatly. SpiderOak uses a compression technology for faster syncing, and Dropbox only syncs bit-level file changes. While GoodSync is very fast, its [block level sychronization](http://www.goodsync.com/enterprise/block-level) (which only updates file changes) is only available for local networks syncing in the enterprise version of the software.

### Other Options Besides GoodSync

[Jungle Disk](https://www.jungledisk.com/) is a great option if you don't have web hosting space or would like to use Amazon S3's servers or Rackspace. It has strong encryption (you control the security key). Pricing is $2-3/month plus storage fees from Amazon/Rackspace.

For just local network syncing, you could use [Windows Live Mesh](http://explore.live.com/windows-live-mesh?os=other), which is very easy to use and works great, [SyncMate](http://mac.eltima.com/sync-mac.html) which syncs between Macs and Windows, plus mobile devices (Android, iOS, more), or several other local syncing tools. But you'd lose the benefits of cloud storage.

Finally, [SparkleShare](http://www.sparkleshare.org/) is an open-source project aiming specifically at creating a Dropbox clone. We're watching it closely and plan on covering in more detail in the future. The program lets you set up your own host to share files with others and keep everything in sync. It's currently only available for Linux and Mac, with Windows, Android, and iOS support slated for development.

Rolled your own Dropbox clone? Let's hear how and why you did it in the comments.

You can follow or contact Melanie Pinola, the author of this post, on [Twitter](http://twitter.com/melaniepinola).
