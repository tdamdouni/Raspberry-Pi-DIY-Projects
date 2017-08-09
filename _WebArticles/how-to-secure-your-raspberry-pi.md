# How to secure your Raspberry Pi

_Captured: 2017-05-10 at 22:35 from [opensource.com](https://opensource.com/article/17/3/iot-security-raspberry-pi)_

![How to secure your Raspberry Pi](https://opensource.com/sites/default/files/styles/image-full-size/public/images/life/life_bank_vault_secure_safe.png?itok=k9QlsRCB)

> _Image by : Jonathunder. Modified by Opensource.com. CC BY-SA 3.0._

The Raspberry Pi and many other inexpensive computer boards like it have become part of the "Internet of Things" or IoT revolution. Internet-connected computing devices have emerged beyond traditional servers, desktops, laptops, and mobile devices. Now your TV, DVR (digital video recorder), thermostat, refrigerator, Internet radio, Raspberry Pi, and other devices are on the network too.

IoT has been huge for experimentation and innovation. But as projects get rushed to completion, there have been severe consequences for ignoring security. And this applies both to commercial products and hobby projects. I'll talk about the Raspberry Pi specifically in this article, so this post is oriented more toward do-it-yourself projects.

## Security on your Raspberry Pi

Because your Raspberry Pi is a Linux system, most advice for security on larger systems applies to your project, too. If you search online for IoT security, most results are for commercial developers making products. Some are also for IT staff who have to deal with expected and unexpected devices showing up on their networks. Those articles may have long lists of requirements that look intimidating. But remember that in the commercial arena, they are dealing with various regulatory consequences for security breaches. They also have training budgets and paychecks to motivate the staff to plow through the long lists of requirements.

For you and your hobby project on a Raspberry Pi, frankly, I don't want to discourage you from experimenting. Let's keep things in perspective--I hope to broaden your horizons about the need to consider security. For example, leaving your device open to an attacker allows them to use it to attack someone else from your network. Or your device might contain data you'd prefer to keep private. This article will give you some tools for your toolbox and some ways to think about the problem.

Unfortunately, risk is the reality of life on the Internet. It's a jungle out there, or sometimes more like a war zone. However, you can take sensible steps to reasonably protect your Raspberry Pi and other IoT devices. So don't let it scare you away.

## Raspberry Pi considerations

Before anything else, one tip has to be first. **Change the passwords on your devices**--don't leave them at the default setting. Default passwords are easy to look up. So that's a common thing attackers will always try.

### What kind of target is your device?

When considering the security of your device, it matters what it does and what's on it. You'll want to consider what would make it a target. These attacks can come from various different sources, such as _viruses_ installed by someone operating the system, _worms_ that automatically break in from the network, or an individual manually performing an attack. With that in mind, let's look at what might make your system a target.

**What data is on the device?** Passwords could perhaps be reused to attack other systems. Does the device have a web interface that an attacker could analyze to find more methods to attack? DIY IoT devices shouldn't have financial or medical data--but bad ideas happen.

**What hardware does your device control?** Cameras are something you don't want under the control of a stranger. Home automation and appliances are things you want to function correctly--what could an attacker control or disable? I've seen articles before about some Raspberry Pi or Arduino projects that automatically unlock the front door by a signal from a phone or NFC (Near Field Communication) tag. If anyone breaks into that system, they can unlock the door.

**What does the device communicate with?** If your project is a network router, could an attacker use it to monitor your network traffic? These are the places that cryptographic MiTM ("man in the middle") attacks could be installed to tap encrypted data.

**What information does the device display?** Could an attacker disable or vandalize the display? For example, if you have a Raspberry Pi displaying worker schedules or software build status on monitors in your office, you wouldn't want it to suddenly display ads or worse.

**Just being on the network can make it a target.** Even if there is nothing else of value to you on the device, the fact that it's connected to the Internet is of value to an attacker. An unsecured device is open to automated harvesting by worms. It may become part of a botnet, or it could be used as an anonymous relay to attack other sites. This makes the attacker more difficult to trace, until an investigation comes demanding information from you. You probably don't want to deal with that. So don't leave your devices open to it.

### Identify the attack surface

In computer security, the term "attack surface" is the set of all the ways a system is exposed to potential attack. These aren't necessarily vulnerabilities, just the places to look for them. In this step, I'll consider all the possible exposures to external access. It includes the network, physical interfaces, databases, web APIs, and even the people who operate it. One useful resource is the [Attack Surface Analysis Cheat Sheet](https://www.owasp.org/index.php/Attack_Surface_Analysis_Cheat_Sheet) by OWASP (Open Web Application Security Project).

As the cheat sheet says, the list quickly becomes overwhelming. You need ways to think about how to prioritize actually important potential attack paths. You want to avoid insignificant wastes of time.

![Risk matrix](https://opensource.com/sites/default/files/resize/iotsectable-650x260.jpg)

> _Table 1: An example of a risk matrix._

Table 1 shows an example of a risk matrix. It compares the likelihood of an event with the magnitude of its impact. You can determine how serious it is and how to prioritize against competing issues. Though it's simplistic, making decisions like these carries over to other fields in life. For example, a business manager routinely has to make decisions based on the potential uses of people, resources, money, and time, which are in demand beyond what's available. In aviation, the FAA makes a similar-looking table to train pilots on aeronautical decision making. For example, if an urgent condition (mechanical, medical, weather, etc.) occurs in flight, this line of thinking is used to decide whether to proceed to the destination, divert to another airport, or return to the origin of the flight.

Similarly, when you analyze the attack surface of your Raspberry Pi project, some things matter a lot more than others. A Raspberry Pi that unlocks your front door or controls security cameras is also part of your home's physical security. It's critically important. However, a Raspberry Pi that displays a game and is not connected to the network probably is not an urgent security matter. This is how you can narrow down an overwhelming list.

Let's look at what contributes to the attack surface of your project.

If it's on the network, even if behind a firewall, then that's an exposure. All the programs that listen to network sockets become part of the attack surface. Running **netstat -ap** as root shows which programs are listening to sockets. Turn off and uninstall any software that doesn't need to listen to the network. This reduces your system's attack surface.

Among the programs that need to run, look at server programs and web APIs. Make sure you have the latest security updates and know where to look for new updates. Make sure the software is configured correctly for its security recommendations. On Linux distributions based on Debian Linux, such as Raspbian and Ubuntu, use this command to update all the packages installed on the system.
    
    
    sudo apt-get update && sudo apt-get upgrade

On RPM-based Linux distributions such as Fedora, this command will update the system's packages.
    
    
    sudo dnf update 
    

Physical interfaces need to be considered, too. Keyboards and mice are obvious. Even if you remove them, is there a USB port where attackers can connect their own? Would a USB stick be able to run programs on the system?

What about the theft of the Raspberry Pi's boot SD card or the whole board? If your project is a science fair project or convention booth display, it will be exposed to members of the public. A competitor or small child could walk away with an unsecured device. An appropriately locked enclosure would reduce the attack surface of the project in that case.

When everything else is considered, the people around it can be part of the attack surface. "Social engineering" is a type of trick where someone convinces an authorized user to do something or disclose information they shouldn't. For example, if your team can look up customer data, what happens when someone claims to be a customer but is actually competitor or thief? Can you adequately identify your customer and catch such a trick?

What about a friendly sounding person asking about your home security system? This could be preparation for a burglary. So make sure everyone in the household knows not to discuss the security system. Change the system if information gets inadvertently disclosed.

## IoT considerations

Current advice in computer security says to include security from the design phase. But what if you're just experimenting with your Raspberry Pi as a DIY project? You're probably adding things on as you learn them. So there's no design phase. Just do the best you can. Keep this article and other resources in mind.

### Code review

In professional or open source software development, "code reviews" are highly recommended to help catch errors. It's a good practice for dealing with inevitable human error. Just getting another set of eyes to read any code often catches errors the author overlooked. For your own DIY projects, you can take advantage of that experience by enlisting the help of friends to review each other's projects for errors and security issues.

### Encryption

For networked connections, use encryption. Even the original Raspberry Pi 1 is powerful enough to do encryption. Configure web servers to use HTTPS with SSL/TLS. Use SSH with remote logins. For just about any case, you can use software packages. So you don't have to learn to be a cryptographer to use cryptography. Let's get a quick overview of the types of encryption.

[Secret-key cryptography](https://en.wikipedia.org/wiki/Symmetric-key_algorithm) uses the same key string to encrypt and decrypt. So it's also called "symmetric." The danger is how to store the key and distribute it to authorized users. Once exposed, an attacker can use it to decrypt everything that was encrypted with it. It's called a "secret key" because you have to keep the key a secret.

There's also [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography), which has separate mathematically related keys that can each decrypt what the other key encrypted. This is also called "asymmetric" encryption because of it using different keys. The usual usage is that one key is the private key, which is kept secret. The other key can be posted in public, and it is called the public key. The public key can be used to decrypt anything that was encrypted with the private key, and prove it came from you. A public/private key pair can represent an individual user or a server machine. This is what SSL/TLS is using to secure your HTTPS web requests.

Another form of cryptography is a one-way **hash**. Any **hashing algorithm** will turn a string into a short, fixed-sized value. I strongly advise storing passwords as hashes, not plain text. This way, a user knows his or her password and the software runs it through the hashing algorithm to verify it matches the stored hash. An attacker can't reverse the stored hash easily. Even so, we need to tell users not to use words from the dictionary as passwords. Because an attacker who gets a hold of the password hashes can try hashing all the words in the dictionary to see if there's a match. That's called a **dictionary attack**.

Passwords should never be stored or transmitted "in the clear" without encryption.

### Existing software packages

When building your project, **use existing software packages** when possible. The reason is because more often than not, reinventing the wheel leads to creating more vulnerabilities inadvertently. Existing systems are more likely to have been reviewed and have had vulnerabilities patched.

### Connecting to the Internet

If your Raspberry Pi project doesn't need to be connected to the Internet, you can eliminate a lot of the attack surface by disconnecting the network. If you need it on the network, think about using multiple layers of defense, such as an iptables firewall in addition to shutting off unnecessary server programs.

Be sure to think about network security on both the client and server sides of the connection. A Raspberry Pi can be either the client or server.

If possible, try turning on SELinux (security enhanced Linux) to enforcing mode. It will catch a lot of abusive behaviors automatically. Unfortunately, it takes some studying manuals--when it denies actions you intended to do, remember to allow just that action. If you get into the habit of simply allowing everything SELinux complains about, eventually you'll open the door for an attacker.

If your project has a web interface, consider and avoid the [OWASP Top Ten](https://www.owasp.org/index.php/OWASP_Top_Ten_Cheat_Sheet) web application security errors.

## Security alerts

Stay aware of security alerts and patches for the software you used in your Raspberry Pi project. The first place to look for notices is from the developers of the software you installed. Check their website for mail lists, RSS feeds, social media, or however they distribute their alerts.

Here are some more useful sources of software security alerts.

## Have fun! with security in mind

In its short history, IoT already has a well-deserved reputation for security problems. A significant recent news story was the DDoS (distributed denial of service) attack on Dyn Networks in October 2016. The Internet nameservers at Dyn turned out to be a single point of failure that, once disabled, took down Twitter, Netflix, CNN, The Guardian, and many other major websites in North America and Europe. How did it happen? Many thousands of IoT devices were taken over by attackers and turned into a robot army or "botnet," which overwhelmed Dyn's servers with network traffic. Under the crushing load, they couldn't provide service to legitimate users. The attackers didn't even have to break into those websites. They merely disabled the network so users couldn't get to them.

So, your first job is not to be part of that problem. Don't create insecure devices that can become part of a botnet.

You probably already guessed that securing your device involves protecting your device from the Internet. But it turns out you also need to think about protecting the Internet from your device. You don't want to be attacked - and you don't want to contribute to attacks on others, even inadvertently.

However, there are other more direct consequences. Depending what your device does, it could have data about you. If the device has a security camera in or around your home, the privacy implications are obvious. But plenty of other data can be sensitive too. If it's nobody else's business to have it, it's sensitive.

There is much more to the field of computer and network security, lately called cybersecurity. But I don't have room in this article. I hope I've gotten you thinking of security at an appropriate level for your Raspberry Pi and IoT projects without scaring you away from playing, experimenting, and innovating. It's about striking a balance. Don't let a challenge stop you from trying. Just be aware of the big picture for securing your projects. All of us always have more to learn as things change.

I can be found on Twitter at [@KO6YQ](https://twitter.com/KO6YQ). I'd like to thank Tony Vargas for help with initial review of the article.
