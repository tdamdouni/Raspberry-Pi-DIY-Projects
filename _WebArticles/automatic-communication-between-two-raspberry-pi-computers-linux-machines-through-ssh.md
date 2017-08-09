# Automatic communication between two Raspberry Pi computers (Linux machines) through SSH

_Captured: 2017-08-04 at 22:35 from [iqjar.com](http://iqjar.com/jar/automatic-communication-between-two-raspberry-pi-computers-linux-machines-through-ssh/)_

#### ![Raspberry Pis communicating via SSH](http://iqjar.com/jar/wp-content/uploads/2014/02/RPI_SSH_RPI_450.jpg)

#### Introduction

This article describes how two [Raspberry Pi](http://iqjar.com/jar/what-is-raspberry-pi/) computers can communicate with each other automatically through the [SSH (Secure Shell)](http://en.wikipedia.org/wiki/Secure_Shell) protocol. Although throughout the article we'll talk about two [Raspberry Pi](http://iqjar.com/jar/what-is-raspberry-pi/) computers, the method should work just as well for any two [Linux](http://en.wikipedia.org/wiki/Linux) machines (perhaps with minor modifications). However, it has been tested with two [Raspberry Pi](http://iqjar.com/jar/what-is-raspberry-pi/) computers running the [Raspbian](http://en.wikipedia.org/wiki/Raspbian#Raspbian) flavor of the [Debian](http://en.wikipedia.org/wiki/Debian) operating system.

Those who like to use their Pis (or Linux machines in general) in [headless mode](http://en.wikipedia.org/wiki/Headless_system) (without any screen, keyboard or mouse attached) are familiar with [SSH](http://en.wikipedia.org/wiki/Secure_Shell) because they use it to log into their system and execute commands on it. The Raspberry Pi installations come with an [SSH server](http://en.wikipedia.org/wiki/SSH_server) running on them by default. This means that users can log in by opening an [SSH client](http://en.wikipedia.org/wiki/Ssh_client) software (for example [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) on [Windows](http://en.wikipedia.org/wiki/Windows) or [Juice SSH](https://play.google.com/store/apps/details?id=com.sonelli.juicessh&hl=ro) on [Android](http://en.wikipedia.org/wiki/Android_\(operating_system\))) and entering a user name and a password. For an SSH connection to be initiated, 4 pieces of data are needed:

    * The [port number](http://en.wikipedia.org/wiki/Port_\(computer_networking\)) of the target machine on which the SSH server is listening
    * The user name of the user who is logging in
    * The password of the user who is logging in

After a user has supplied all these 4 pieces of data correctly, if everything goes well, he will be able to access the terminal of the target Linux system and execute commands. For example he might run the "**df -h**" command to check the free disk space on each partition. We will use this command throughout this article as an example, to explain different ways of running commands via SSH.

#### From one Pi to another

If you have more than one Raspberry Pi (or any Linux computer), you can log in via SSH from one to the other by calling the Linux SSH client from command line.

In our examples we will assume that user "**local_user**", who is currently logged into the machine with [host name](http://en.wikipedia.org/wiki/Host_name) "**local_machine**" (reachable at the [domain name](http://en.wikipedia.org/wiki/Domain_name) **localhost**) is trying to log into the machine "**remote_machine**" (reachable at **remote.com**) as user "**remote_user**".

After you are logged in on machine **local_machine** as user **local_user**, type the following command line into the terminal:

**local_user@local_machine $ ssh remote_user@remote.com -p22**

This means that you are now trying to log onto the machine **remote_machine** (reachable at **remote.com**) as user **remote_user** on port number **22** (22 is the default SSH port). As you can see, the command contains only 3 out of the 4 pieces of data needed to initiate an SSH connection: the user name, the destination machine address and the destination SSH port number. The password is not present. This is because the destination machine will ask for the password in a separate line. If you enter that too correctly, you will successfully log onto the machine **remote_machine** as user **remote_user**.

If you wish to execute a remote command from one Raspberry Pi on the other Raspberry Pi (for example the "**df-h**" command), then you can execute the following on the Pi on which you are already logged in (on **local_machine**):

**local_user@local_machine $ ssh remote_user@remote.com -p22 'df -h'**

The disk free information from **remote_machine** will be returned and displayed on **local_machine**.

#### Communication between two Linux computers via SSH

If things are so simple, if a command can be executed on a remote machine through SSH, simply by calling the SSH command on the local machine and specifying the remote command to run on the destination machine, then the local machine should be able to execute such remote commands automatically, perhaps at specified time intervals (as a [cron](http://en.wikipedia.org/wiki/Cron) job), or as a response to some event that occurs on the local machine (for example if a temperature sensor's reading exceeds a threshold on the local machine, it could execute a command on a remote machine attached to the heating system and could turn off the heating). The idea is that the two computers could communicate between each other through SSH without any human intervention, automatically.

Unfortunately things are not quite as simple. Remember that the SSH command line does not have the remote user's password in it and that the remote machine will ask for the password in a separate line? That complicates things because it means that the remote command cannot be executed as a single line. Well, at least not without some preparation…

The simplest way to get around this is by using the **sshpass** utility to pass the password to the remote machine. First of all, it must be installed on the local machine which is trying to execute the remote command. If it is not, you can install it like this:

**sudo apt-get install sshpass**

Once installed, you can prepend the ssh command lines with "sshpass password", like this:

**local_user@local_machine $ sshpass remote_password ssh remote_user@remote.com -p22 'df -h'**

This method is quite easy and convenient, but it has one major flaw: if such a command were to be executed automatically by the local machine, then the remote user's password would have to be stored somewhere in a file on the local machine. This would be a security weakness because if the local machine were hacked, then the remote machine would also become exposed to attacks, especially if the user trying to log onto the remote machine has root privileges, which is often the case.

#### Setting up SSH login without a password

A more clean and secure way for the local machine to be able to execute commands via SSH on the remote machine is to somehow add the local user to a white list on the remote machine and have the remote machine accept login attempts from the local machine without asking for a password. This only has to be done once, after which the user from the local machine will be able to log onto the remote machine without password and execute remote commands through SSH, just as we wanted in the beginning:

**local_user@local_machine $ ssh remote_user@remote.com -p22 'df -h'**

Actually, the white list on the remote machine is kept separately for each user on the remote machine and the entries in these white lists are users from the local machine. In other words, we need to add **local_user** from **local_machine** to the white list of **remote_user** on **remote_machine**. This is done by generating a unique SSH key for the **local_user** on **local_machine** and adding this key to the **remote_user**'s list of accepted keys on **remote_machine**.

#### Steps to execute on the local machine

**1.** Log into **local_machine** as **local_user**.

Let's assume that the home directory of **local_user** is **/home/local_user**.

**2.** Check if the directory **/home/local_user/.ssh** exists:

**ls /home/local_user/.ssh**

**3.** If it does not exist, create it:

**mkdir /home/local_user/.ssh**

**4.** Make sure that the newly created directory is owned by the local user:

**chown local_user:local_user /home/local_user/.ssh**

**5.** Change the permissions of the newly created directory, so that only the local user can access it in any way:

**chmod 700 /home/local_user/.ssh**

**6.** Generate the SSH key for the **local_user**:

**ssh-keygen**

The utility will now ask for 3 things: a file where to save the key, a password for the local user and the confirmation of the password. Give blank answers to all 3 questions (just hit Enter).

**7.** Copy the generated public key:

**cat /home/local_user/.ssh/id_rsa.pub**

This will output a long string, which is the public SSH key. Select it to copy it. The key looks something like this:

_ssh-rsa ACAB3NzaC8zc2EAABKDAQABAAYBAQDmnAoq7lh12FT4u1WtZhmZs6pGoPkLXV+5iwOMETLgCF4HwTK4Qcj0feWZ1XnmngkGeAVLFhlTL8HBbYyQfgwZtCq2vJzODZ0FVY667eadgqTwXFGfA3CoL4PPwRTz3UxDZu78G+ZgoAwKLXczAqJumKvKutRmwBqnHcyqwwzt00Qwj64W9In+HBZaeH9F5xkhoLYt1L5wuyGcb3dmTKJ5zJh2WRloVuMR3W96k2A/dewQuL8TFsu8cwS72+bi0LVappeMONHcA/NNsBh1234gwoCwuoJGS+0DYL77M4Aj0v3hPT8nn5j5ksrcUUKR2OxHZK2r3boYecMmGRX0MA1u local_user@local_machine_

#### Steps to execute on the remote machine

**1.** Log into **remote_machine** as user **remote_user**.

Let's assume that the home directory of **remote_user** is **/home/remote_user**.

**2.** Check if the directory **/home/local_user/.ssh** exists:

**ls /home/remote_user/.ssh**

**3.** If it does not exist, create it:

**mkdir /home/remote_user/.ssh**

**4.** Make sure that the newly created directory is owned by the remote user:

**chown remote_user:remote_user /home/remote_user/.ssh**

**5.** Change the permissions of the newly created directory, so that only the remote user can access it in any way:

**chmod 700 /home/remote_user/.ssh**

**6.** Add the copied key into the white list of the remote user:

With your favorite text editor (we will use nano) open the file **/home/remote_user/.ssh/authorized_keys**. Don't worry if it does not exist yet, in that case we'll create it now when we save it. Paste into this file the key copied from the local machine. Make sure that the pasted key is on a single line. If the **authorized_keys** file existed before and already contains some keys, just add this new key in a new line. Finally save the file (CTRL+o in nano).

**7.** Change the file permissions of the **authorized_keys** file:

**chmod 600 /home/remote_user/.ssh/authorized_keys**

This eliminates any security hazard by making sure that only **remote_user** can read/write the white list file.

Executing some of the above commands, both on the local and remote machine, may require the logged in user (**local_user**/**remote_user**) to have root privileges or at least to be able to execute command as root (use **sudo**).

If on the local machine the ssh command is called as root (for example, if called by crontab or if called with **sudo**), then you must also generate a key for the root user on the local machine and add it to the white list file of the remote user.

#### Testing

To test that local_user can really execute remote commands as remote_user on the remote computer, log in as **local_user** onto **local_machine** and type this into the command line:

**local_user@local_machine $ ssh remote_user@remote.com -p22 'df -h'**

If you are not asked for a password and the disk free information from the remote machine is returned correctly, then it works. Note that the first time you execute this, the remote machine will ask you about adding an entry to its key cache. Answer "yes" and the next time the remote command should run without asking any questions, which means that the local machine will be able to execute remote commands on the remote machine via SSH in a fully automatic manner.

  * 
