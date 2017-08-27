# Raspberry Pi System Logging and Loggly

_Captured: 2017-08-26 at 10:14 from [blog.scphillips.com](http://blog.scphillips.com/posts/2015/05/raspberry-pi-system-logging-and-loggly/)_

I've already written about how useful Loggly is to log data from a Raspberry Pi, but like me, you may want to know more about how system logging actually works and what the extra configuration added by the Loggly setup script means.

This post explains how system logging works and how Loggly fits into it. It describes how the log files are rotated to avoid them filling up the disc and it also goes into a lengthy detour regarding how to encrypt the log traffic between your computer and Loggly, how all the encryption actually works and how you know you can trust it.

## The default Raspberry Pi logging configuration

The recommended "raspbian" operating system for the Raspberry Pi is a derivative of Debian and uses rsyslog to do system and kernel logging. The configuration of rsyslog can be quite complex, partly because it supports configuration directives from 3 different systems. The configuration file that comes with raspbian is in /etc/rsyslog.conf and uses a mixture of legacy (i.e. old) rsyslog directives which begin with $, directives from sysklog (which rsyslog is based upon) and some newer ones. As a result, getting definitive documentation is difficult. It seems especially hard to find documentation on sysklog which is a shame as most of the directives used in the file in raspbian are sysklog ones.

Basically though, various operating system services and the kernel itself log messages to rsyslog and the configuration determines which log files the messages end up in. The log files are generally found in /var/log. Most of the files in there can only be read by the root user or someone in the adm (short for "admin") group. The default pi user on raspbian is in the adm group so most likely you can read them.
    
    
    $ ls -l /var/log/syslog
    -rw-r----- 1 root adm 189143 May 15 20:06 /var/log/syslog
    $ whoami
    pi
    $ groups
    pi adm dialout cdrom sudo audio video plugdev games users netdev input spi gpio
    

The commands above show that the syslog file is owned by root and in the adm group. The -rw-r----- part says that the owner (root) has read and write permission but not execute (the first rw-) anyone in the group (adm) has just read permission (r--) and anyone else gets no access (the final ---). The whoami and groups commands then show who you are logged in as and what groups you belong to.

The logging system makes use of two log message categories: the "facility" and the "level". The facility indicates the sub-system that the message comes from such as "kern" for kernel messages, "user" for user-level messages, "mail" for messages from the email system and "auth" for security and authorisation messages. On a default raspbian installation you won't be running an email system, a printer ("lpr"), network news or FTP so most log files will be empty.

The level of a message indicates how critical it is and ranges from "debug", via "info" and "warn", up to "emerg" which is when you need to start panicing.

Which messages go where is configured in /etc/rsyslog.conf which, quite near the top in the "GLOBAL DIRECTIVES" section includes these lines:
    
    
    #
    # Include all config files in /etc/rsyslog.d/
    #
    $IncludeConfig /etc/rsyslog.d/*.conf
    

That means that any file ending with .conf in the /etc/rsyslog.d directory will be included in the configuration at that point in the file, before any other rules are executed. The files are included in alpha-numeric order which is why they tend to have a number prefixing them (so that you can easily decide what order to put them in). In fact, files beginning with a full-stop (.) are ignored so you can temporarily disable a file in that way. If you do rename a file to start with . then you also hide it from the default directory listing (ls) and you need to do ls -a ("a" for "all") to see it.

So, back to the configuration file, the first few rules are:
    
    
    #
    # First some standard log files.  Log by facility.
    #
    auth,authpriv.*                 /var/log/auth.log
    *.*;auth,authpriv.none          -/var/log/syslog
    #cron.*                         /var/log/cron.log
    daemon.*                        -/var/log/daemon.log
    kern.*                          -/var/log/kern.log
    lpr.*                           -/var/log/lpr.log
    mail.*                          -/var/log/mail.log
    user.*                          -/var/log/user.log
    

The last line says to add message logged by the user at any level (the *) to the /var/log/user.log file. The minus in front of the filename means that the file is not synched to disc every time a message is sent there so potentially some of it is held in memory and may be lost if the computer crashes.

The top line says that anything sent from the auth or authpriv facility (used by the ssh system for instance) at any level should be written to the auth.log file and right away synched to disc to make sure we have that important info (i.e. who logged in when). I must admit I don't quite understand this syntax, I mean is auth,authpriv.* exactly the same as auth.*;authpriv.* and can you put as many facility names as you like? I think the answer's "yes" but the documentation on this is hard to find.

The second line says to send everything matching *.* (i.e. all facilities, all levels) to the syslog, but it also says that nothing from the auth/authpriv facility should go there (to keep it separate). Again, this is a bit obscure: later in the file we see that putting statements separated by semi-colons seems to mean "or" but when you put a .none in there it starts looking more like an "and" in that this says the line must match *.* and not match auth or authpriv.

The next line for the cron facility is commented out but the message will end up in the syslog file anyway.

So for the main log files, auth stuff goes into auth, everything else goes into syslog and some things are also copied into facility-specific files.

Later down the file we have:
    
    
    #
    # Logging for the mail system.  Split it up so that
    # it is easy to write scripts to parse these files.
    #
    mail.info                       -/var/log/mail.info
    mail.warn                       -/var/log/mail.warn
    mail.err                        /var/log/mail.err
    

The thing to learn about these statements is that the priority part (after the .) means "messages with this priority or higher". So messages sent from mail with level err will be written into the mail.info, mail.warn and mail.err files. The mail.err file doesn't have a - in front so that the message is written to disc immediately and can be seen instead of being buffered for a while.

Skipping further down we have:
    
    
    *.=info;*.=notice;*.=warn;\
            auth,authpriv.none;\
            cron,daemon.none;\
            mail,news.none          -/var/log/messages
    

This shows two further facets of the system. A priority of =info means messages with that log level exactly (and does not match those with a higher priority in the way we saw with the mail rules). The back-slashes (\\) at the end of a line just mean that the statement continues on the next line. This whole rule says to put into the messages log file anything with priority info or notice or warn but not anything from auth, authpriv, cron, daemon, mail, or news. I don't know why it is not just written as all six facilities with a none instead of splitting into three parts. Perhaps it could be but no-one dares try it because it's always been that way and the documentation no longer exists…?

## Rotating log files

Another important thing to take care of with log files is that they don't get too big. This is handled by the logrotate software that is part of the rsyslog package. If you look in /var/log then you see lots of archived log files as well as the live ones. For instance:
    
    
    $ ls -l /var/log/syslog*
    -rw-r----- 1 root adm  75637 May 31 11:05 /var/log/syslog
    -rw-r----- 1 root adm 377213 May 31 06:25 /var/log/syslog.1
    -rw-r----- 1 root adm  26907 May 30 06:25 /var/log/syslog.2.gz
    -rw-r----- 1 root adm  25029 May 29 06:25 /var/log/syslog.3.gz
    -rw-r----- 1 root adm  21158 May 28 06:25 /var/log/syslog.4.gz
    -rw-r----- 1 root adm  20837 May 27 06:25 /var/log/syslog.5.gz
    -rw-r----- 1 root adm  20545 May 26 06:25 /var/log/syslog.6.gz
    -rw-r----- 1 root adm  21715 May 25 06:25 /var/log/syslog.7.gz
    

We have today's syslog, yesterday's file now renamed syslog.1, the day before's now compressed and called syslog.2.gz and so on. It is keeping all the logs for the last 7 days.

The logrotate software is configured in several files in /etc/logrotate.d. Quite a few pieces of software use logrotate to rotate (archive) their log files and yet do not use rsyslog to do the actual logging. So in /etc/logrotate.d you will see a configuration file for apt as well.

The file /etc/logrotate.d/rsyslog (unsurprisingly) has the configuration for rsyslog. It is fairly self-explanatory and the options can all be seen using man logrotate. It defines one configuration for the syslog file and another for all the other files created by rsyslog where only the last 4 days' worth are kept. The only complicated bit is the postrotate part:

This runs the command invoke-rc.d rsyslog rotate once the logs have been rotated and sends any output to /dev/null (i.e. discards it). The invoke-rc.d command runs a command defined in the service's "init script" which you can find in /etc/init.d/rsyslog. It is also the init script which is used when you restart the service with sudo service rsyslog restart. Basically, all this is doing is giving the rsyslog daemon a kick to tell it that the log files have just moved and it needs to re-open the file to continue logging.

The logrotate command is executed once every day by cron thanks to the file /etc/cron.daily/logrotate.

## Logging to Loggly

[Loggly](http://loggly.com) is a web service which lets you send syslog messages to it and displays then in a nice web interface which you can search and use for analysis of the events. The basic features are free and it is easy to configure for use from a Raspberry Pi as I explained in [my post about monitoring broadband speed](http://blog.scphillips.com/posts/2015/05/monitoring-broadband-speed-with-loggly/). Read the [previous post](http://blog.scphillips.com/posts/2015/05/monitoring-broadband-speed-with-loggly/) or [Loggly's own instructions](https://www.loggly.com/docs/configure-syslog-script/) for set-up instructions.

Once you have set it up, you will have a new file called /etc/rsyslog.d/22-loggly.conf:
    
    
    #          -------------------------------------------------------
    #          Syslog Logging Directives for Loggly (scphillips.loggly.com)
    #          -------------------------------------------------------
    
    # Define the template used for sending logs to Loggly. Do not change this format.
    $template LogglyFormat,"<%pri%>%protocol-version% %timestamp:::date-rfc3339% %HOSTNAME% %app-name% %procid% %msgid% [your-secret-token-goes-here@12345] %msg%\n"
    
    # Send messages to Loggly over TCP using the template.
    *.*             @@logs-01.loggly.com:514;LogglyFormat
    
    #          -------------------------------------------------------
    #          End of Syslog Logging Directives for Loggly
    #          -------------------------------------------------------
    

From the discussion above, we now know a lot about what this is. It's an additonal rsyslog config file (they have chosen to prefix it with "22") so will be inserted near the start of the main /etc/rsyslog.conf file. It uses the $template directive which essentially is just varible assignment to create a message of a specific format to send to Loggly (see [the list of rsyslog properties](http://www.rsyslog.com/doc/property_replacer.html) that can be used in these formats). The line beginning *.* will match all messages, the action is to send the LogglyFormat message that was just created (not the raw message) over TCP (indicated by @@ rather than UDP which would be @) to the machine called logs-01.loggly.com on port 514.

What Loggly is doing here is specifying a precise format for message to be sent to its service. All the messages go to the same service endpoint and are sorted into the separate accounts by the secret token so that you only see your messages. The rest of the message is also parsed so that Loggly can search and index by the other fields.

As it says in the file: do not change this format! If you do, then I expect your messages will be silently rejected.

If you want to look into this some more, you can add this line to the same 22-loggly.conf file at the end:

That will match on any message and write the LogglyFormat message to the /var/log/loggly.conf file. If you then restart the rsyslog service again you will see in the loggly.conf files lines such as:
    
    
    $ sudo service rsyslog restart
    [ ok ] Stopping enhanced syslogd: rsyslogd.
    [ ok ] Starting enhanced syslogd: rsyslogd.
    $ cat /var/log/loggly.log
    <6>0 2015-05-17T19:04:36.502960+00:00 raspberry3 kernel  - [your-secret-token-goes-here@12345] imklog 5.8.11, log source = /proc/kmsg started.
    <46>0 2015-05-17T19:04:36.503918+00:00 raspberry3 rsyslogd  - [your-secret-token-goes-here@12345]  [origin software="rsyslogd" swVersion="5.8.11" x-pid="16410" x-info="http://www.rsyslog.com"] start
    

If you do add the line I just suggested to the 22-loggly.conf file then make sure you remove it and restart rsyslog again otherwise the log file will just get bigger and bigger.

## Logging securely

Sending all your log messages over the internet to Loggly in plain text is not always a good idea. If it bothers you, [Loggly do provide instructions to encrypt the messages](https://www.loggly.com/docs/rsyslog-tls-configuration/).

I found the instructions needed a bit of tweaking:

This is fine, I found the package was already installed and up to date but it's worth doing. The instructions continue:
    
    
    $ mkdir -pv /etc/rsyslog.d/keys/ca.d
    $ cd /etc/rsyslog.d/keys/ca.d/
    $ curl -O https://logdog.loggly.com/media/loggly.com.crt
    $ curl -O https://certs.starfieldtech.com/repository/sf_bundle.crt
    $ cat {sf_bundle.crt,loggly.com.crt} > loggly_full.crt
    

All of these, apart from the cd command need to be prefixed with sudo as they are writing into protected directories. Perhaps Loggly assume that you are the superuser which you can become by typing sudo su, but it is safer to not be root and explicitly give "super power" to each command individually. Here's the transcript of what I did:
    
    
    $ mkdir -pv /etc/rsyslog.d/keys/ca.d
    mkdir: cannot create directory `/etc/rsyslog.d/keys': Permission denied
    $ sudo mkdir -pv /etc/rsyslog.d/keys/ca.d
    mkdir: created directory `/etc/rsyslog.d/keys'
    mkdir: created directory `/etc/rsyslog.d/keys/ca.d'
    $ cd /etc/rsyslog.d/keys/ca.d/
    $ sudo curl -O https://logdog.loggly.com/media/loggly.com.crt
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  1968  100  1968    0     0   2084      0 --:--:-- --:--:-- --:--:--  2447
    $ sudo curl -O https://certs.starfieldtech.com/repository/sf_bundle.crt
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   263  100   263    0     0    229      0  0:00:01  0:00:01 --:--:--   413
    $ ls -l
    total 8
    -rw-r--r-- 1 root root 1968 May 30 14:15 loggly.com.crt
    -rw-r--r-- 1 root root  263 May 30 14:16 sf_bundle.crt
    $ cat *
    -----BEGIN CERTIFICATE-----
    MIIFfzCCBGegAwIBAgIILqvAG0gVC3QwDQYJKoZIhvcNAQEFBQAwgdwxCzAJBgNV
    blah, blah...
    ODRffuOanfiyg+bXxdmuhfXUqQ==
    -----END CERTIFICATE-----
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <html><head>
    <title>301 Moved Permanently</title>
    </head><body>
    <h1>Moved Permanently</h1>
    <p>The document has moved <a href="https://certs.secureserver.net/repository/sf_bundle.crt">here</a>.</p>
    </body></html>
    

The curl command downloads whatever is at the URL you specify. In this case we are hoping to get a "certificate" (more on what that is in a minute). I executed the two curl commands and they seem successful, I did an ls -l to check what files I now had in the directory and it looked good but then I did cat * which prints both files (as they both match the * wildcard) to the console. The first file is a certificate (it clearly says so!) but the second file is an HTML error page saying that the file has moved. The Loggly instructions need updating!

A more robust way of doing this is to use the -L option of curl to follow redirects:
    
    
    $ curl -OL https://certs.starfieldtech.com/repository/sf_bundle.crt
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   263  100   263    0     0    253      0  0:00:01  0:00:01 --:--:--   411
    100  3273  100  3273    0     0   1475      0  0:00:02  0:00:02 --:--:-- 16784
    

Now curl has followed the "301 Moved Permanently" redirect that the web server is returning and downloaded the sf_bundle.crt file.

The next instruction from Loggly is to concatenate the two certificate files:
    
    
    $ cat {sf_bundle.crt,loggly.com.crt} > loggly_full.crt
    

Again, this will work as long as you are root but the syntax is a bit odd and might only work in the bash shell, I'm not sure. I would do:
    
    
    $ sudo su
    # cat *.crt > loggly_full.crt
    # exit
    

Here I use the standard notation from the shell of prefixing a command by $ for a normal user and # when you are the super-user (or "root"). The cat *.crt command conCATenates all files it finds ending with .crt and would print them to the console, but the > loggly_full.crt part redirects it into a new file. We have to be root in order to write into the new file.

In summary, the commands you need are:
    
    
    $ sudo su
    # mkdir -pv /etc/rsyslog.d/keys/ca.d
    # cd /etc/rsyslog.d/keys/ca.d/
    # curl -OL https://logdog.loggly.com/media/loggly.com.crt
    # curl -OL https://certs.starfieldtech.com/repository/sf_bundle.crt
    # cat *.crt > loggly_full.crt
    # exit
    

So what are these "certificates" anyway? It's all to do with public-key cryptography about which I could write pages and pages. I'll try to be brief but you might want to skip this part and jump ahead to [Back to logging securely](http://blog.scphillips.com/posts/2015/05/raspberry-pi-system-logging-and-loggly/).

### What the certificates are all about

The .crt files are what are known as "PEM encoded SSL certificates". "[SSL](http://en.wikipedia.org/wiki/Transport_Layer_Security)" is "Secure Sockets Layer" which is a standard for encryption between computers. "PEM" is just a particular way of encoding (or writing) the certificate. You can decode the information in the .crt file using the following openssl command:

The command basically says that openssl is to deal with an [X.509](http://en.wikipedia.org/wiki/X.509) certificate (which is a common standard), read it in and write it out as text. What you see on the console when running this command is similar information to that which you can see in a web browser by clicking on the padlock icon when visiting a secure site. The information includes:
    
    
    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                2e:ab:c0:1b:48:15:0b:74
        Signature Algorithm: sha1WithRSAEncryption
            Issuer: C=US, ST=Arizona, L=Scottsdale, O=Starfield Technologies, Inc., OU=http://certificates.starfieldtech.com/repository, CN=Starfield Secure Certification Authority/serialNumber=10688435
            Validity
                Not Before: Apr  6 05:42:38 2015 GMT
                Not After : Apr  6 05:38:38 2016 GMT
            Subject: OU=Domain Control Validated, CN=logs-01.loggly.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    Public-Key: (2048 bit)
                    Modulus:
                        00:a8:e8:94:12:24:22:bc:cb:ae:d6:7e:0d:db:54:
                        20:67:75:59:a3:cc:5e:76:b2:19:bf:42:7f:9d:0f:
                        19:3a:81:ed:3a:cd:58:1f:67:97:0f:0f:7e:58:0d:
                        0a:9d:6c:77:72:bb:52:6a:e7:d0:24:e2:9b:bf:4d:
                        ae:6e:5a:f3:a1:52:ea:ac:0d:4b:98:c9:fb:bd:06:
                        1e:8d:1b:20:b3:bd:48:8d:17:03:9a:f5:d1:fd:5b:
                        b2:69:17:3f:c2:50:9a:a9:b0:a0:26:c1:83:43:79:
                        7b:81:d1:51:6b:2d:1c:58:09:04:f3:a9:60:43:b9:
                        79:c3:be:d7:e2:32:6b:c1:bc:58:94:28:57:e6:e2:
                        55:21:59:5d:fb:8b:15:22:5e:dc:7b:c6:ef:aa:24:
                        ea:81:79:1c:28:d1:7e:44:9f:9a:64:d6:84:93:cc:
                        76:5a:4e:d1:04:c5:b7:5e:cd:5d:ef:39:08:b1:1e:
                        d7:21:92:b4:4d:2a:56:e8:85:d9:2b:52:96:59:9f:
                        d6:76:d4:af:85:84:e4:e6:a7:fb:b4:dc:38:60:89:
                        05:da:bf:a6:f1:91:6d:4f:a3:c6:41:3e:5c:89:46:
                        51:d7:7b:6e:d7:6e:a6:66:a3:5c:89:26:7d:85:df:
                        73:3b:80:db:8a:96:ca:4e:dd:c7:52:d5:4a:83:a9:
                        67:a5
    

This says, amongst other things, that the certificate is valid for use by the server logs-01.loggly.com (that's the "Subject") and that it is issued by the "Starfield Secure Certification Authority" (the "Issuer"). It also shows the 2048 bit "public key" which is a big number that is used to encrypt the messages to the Loggly server. The last part of the data you would see in the console (not shown here) is the "signature" of the certificate authority. This is the digital equivalent of someone in charge at the issuer ("Starfield Secure Certification Authority") signing Loggly's certificate and essentially saying "this is all correct, it's the right public key, trust me".

#### Public key cryptography and signatures

Two other things the certificate says are that the "Signature Algorithm" is "sha1WithRSAEccryption" and that the "Public Key Algorithm" is "rsaEncryption".

[RSA](http://en.wikipedia.org/wiki/RSA_\(cryptosystem\)) is a clever algorithm for encryption first described in 1977. With RSA encryption each person (or company) has two keys: a public one and a private one, know as a "key pair". The public key is made public (for instance in these certificates) and if you encrypt something with the public key then only the holder of the private part of the key pair can decrypt it. This is what is used when sending a private message to Loggly: we encrypt them with Loggly's public key as found in the certificate.

The other important thing about RSA encryption is that if you encrypt with the private key then the public key can be used to read the message. This might not sound very useful as everyone has the public key so the message is clearly not secret. What _is_ useful though is that only the holder of the private key can create those encrypted messages: it is this property which is used for digital signatures.

If I have a document (such as a certificate) and I encrypt it with my private key, then I could provide the encrypted document and you (holding my public key) could decrypt it and then you would both have the certificate and the knowledge that it was me who created it and that therefore I agreed with the contents. If someone changed the encrypted version then it would no longer decrypt so you would know it had not been tampered with. If you trusted me then you could trust the document. This isn't what is actually done because (a) having the encrypted version is not what you want generally (you want to actually be able to read it easily) and (b) encrypting and decrypting large documents takes too much time.

Instead, a "hashing algorithm" is used for the signature, in this case "SHA1". SHA1 takes a document of any size and creates a short-ish number from the document. The algorithm has been designed so that if a single character of the document changes then the generated number (the "hash") also changes. Moreover, it is designed so that it is very difficult to take one document and create another one with the same hash.

So, the hash represents the document. Instead of encrypting the document we can just generate the hash and encrypt that (which is much faster): this is what a digital signature does. To check that the signature is correct (and therefore that the document has not been tampered with and that the signer agreed with the contents) you have to (a) decrypt the signature using the sender's public key and (b) generate the hash of the document. If the two match then it's all good!

#### Back to the Loggly certificate

The trouble is, how do we know that it's safe to use this public key to encrypt the messages sent to Loggly? We need to be sure that it's only Loggly that can read the messages. It could be that the private key which goes with the public key has been leaked and that anyone can decrypt the information (this is _not_ the case by the way, as far as I know). It's up to the issuer to provide this reassurance: an issuer keeps a list (a "certificate revocation list" or "CRL") of certificates (containing keys) which should no longer be used (the CRL location is part of the certificate). So we can theoretically check that, but how do we know that it really was the issuer that signed it and how do we know we can trust them? That's what the other certificate file is for.

If you split the other certificate file into two files using a text editor then you can use the same openssl command to look at the two certificates in more detail. What you will find, looking at the "subject" and "issuer" fields in particular is one certificate issued to "Starfield Secure Certification Authority" by "Starfield Class 2 Certification Authority" and another certificate issued to "Starfield Class 2 Certification Authority" by "Starfield Class 2 Certification Authority". Each certificate has another public key and another signature. You can use the public key of the issuer's certificate to verify the signatures of the certificates they sign, that is, verify that it really was them that said you should trust the "subject".

What we've found in summary is:

  * A certificate for Loggly containing the public key we need to encrypt messages to their server and signed by "Starfield Secure Certification Authority".
  * A certificate for "Starfield Secure Certification Authority" containing its public key which we can use to verify the signature of Loggly's certificate and therefore confirm it's the right key to use and that it is valid. This one is signed by "Starfield Class 2 Certification Authority".
  * A certificate for "Starfield Class 2 Certification Authority" signed by itself: this essentially just says "trust me" with no higher authority to refer to.

So, the problem becomes, why should we trust the "Starfield Class 2 Certification Authority"? That's the problem with any sort of public-key infrastructure: you have to make some decisions about who to trust. Fortunately (?) these decisions have already been taken by companies such as Microsoft who ship Windows with a set of certificate authorities already trusted. If you look into it, you will find the exact same Starfield certificate already trusted by Windows, so I guess that's okay!

Digital signatures are used in other parts of the operating system as well. For instance, when you do apt-get install to install a new package, the software package is downloaded, the hash generated and checked against signed hash in the package to make sure that someone responsible has signed the package off and that it has not been tampered with (for instance by someone adding a virus). Raspbian comes with a set of trusted certificates for this which are kept in /etc/apt in various .gpg files (which is a different format).

### Back to logging securely

The Loggly instructions go on to tell you to do one thing for rsyslog "version 6.x or lower" and something else for "version 7.x or higher". It's a bit hard to tell what version we actually have as there is no handy --version command line argument. Instead we can use the dpkg command to look at the packages installed:
    
    
    $ dpkg -l 'rsys*'
    Desired=Unknown/Install/Remove/Purge/Hold
    | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
    |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
    ||/ Name                  Version         Architecture    Description
    +++-=====================-===============-===============-================================================
    ii  rsyslog               5.8.11-3+deb7u2 armhf           reliable system and kernel logging daemon
    un  rsyslog-doc           <none>                          (no description available)
    ii  rsyslog-gnutls        5.8.11-3+deb7u2 armhf           TLS protocol support for rsyslog
    un  rsyslog-gssapi        <none>                          (no description available)
    un  rsyslog-mysql         <none>                          (no description available)
    un  rsyslog-pgsql         <none>                          (no description available)
    un  rsyslog-relp          <none>                          (no description available)
    

I just wrote 'rsys*' there as I wasn't sure what the actual package name was. This shows we have version 5.8.11 installed along with the TLS package to provide the encryption. Therefore we need to edit the /etc/rsyslog.d/22-loggly.conf file to add in these lines:
    
    
    # Setup disk assisted queues
    $WorkDirectory /var/spool/rsyslog # where to place spool files
    $ActionQueueFileName fwdRule1     # unique name prefix for spool files
    $ActionQueueMaxDiskSpace 10m      # 10MB space limit (not much room on an SD Card)
    $ActionQueueSaveOnShutdown on     # save messages to disk on shutdown
    $ActionQueueType LinkedList       # run asynchronously
    $ActionResumeRetryCount -1        # infinite retries if host is down
    
    #RsyslogGnuTLS
    $DefaultNetstreamDriverCAFile /etc/rsyslog.d/keys/ca.d/loggly_full.crt
    $ActionSendStreamDriver gtls
    $ActionSendStreamDriverMode 1
    $ActionSendStreamDriverAuthMode x509/name
    $ActionSendStreamDriverPermittedPeer *.loggly.com
    *.* @@logs-01.loggly.com:6514;LogglyFormat
    

We also need to comment out (by adding a # to the front) the line *.* @@logs-01.loggly.com:514;LogglyFormat which was the one that sent the LogglyFormat message to Loggly on port 514. Note, I've changed it a little from the Loggly version by making the ActionQueueMaxDiskSpace 10MB instead of 1GB as space is precious on a Raspberry Pi's SD card!

The first set of statements set up a queue of messages waiting to be encrypted and forwarded in a file in the /var/spool/rsyslog directory. The second set configure the encryption and point to the certificate file with all three certificates in; say to use the gtls driver and that it should be enabled; configure it to validate the X.509 certificate and check that the host it connects to is the right one; defines which hosts are permitted and then finally has the directive to send all messages *.* via TCP to the same server as before but using port 6514 instead of port 514. The server will be listening on port 6514 for encrypted messages.

As ever, once you've edited one of the configuration files, restart the daemon using sudo service rsyslog restart and check the log file in case it says there is an error by doing tail /var/log/messages.
