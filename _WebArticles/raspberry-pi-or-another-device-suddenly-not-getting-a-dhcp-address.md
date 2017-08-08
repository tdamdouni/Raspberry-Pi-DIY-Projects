# Raspberry Pi (or another device) suddenly not getting a DHCP address?

_Captured: 2017-05-21 at 10:45 from [www.jeffgeerling.com](https://www.jeffgeerling.com/blog/2016/raspberry-pi-or-another-device-suddenly-not-getting-dhcp-address)_

Tonight, after I made a couple changes to my wired in-house Gigabit network (I recently added a few Cat6 runs after moving my main Wireless router--in this case an AirPort Extreme base station), I noticed the Raspberry Pi webserver that was hosting [www.pidramble.com](http://www.pidramble.com/) wasn't reachable over the network, and [Server Check.in](https://servercheck.in/) started reporting an outage.

I have that particular device set using a DHCP Reservation based on it's MAC address, and it's been working like a champ for over a year. So something was strange, since I hadn't made any networking configuration changes on the Pi itself in a few months, nor had I unplugged it at all in the past month.

After spending an hour or so plugging the Pi into a monitor/keyboard to run through diagnostics, checking over `/etc/network/interfaces` and trying `static` for the `eth0` configuration with a given IP address, trying `dhcp`, and trying `manual`, and using every software trick in the book, I couldn't get the Pi to see the in-house network. But the lights on the Pi's LAN jack were lit up and blinked here and there, meaning it saw the network. And my network switch lights lit up and blinked too... something was definitely up!

I then started looking into hardware issues:

  * I tried plugging the Pi into _another_ jack on the switch, that didn't work.
  * I tried plugging the Pi into a different switch, that didn't work.
  * I tried pulling the microSD card out of the Pi and swapping the entire Pi (thinking the network port might be physically damaged). Nothing.

I was at my wit's end, when I remembered that (since AirPort's own utility only shows connected Wireless clients) I should use `arp` to see all the devices my Mac could notice on the network. When I ran `$ arp -a`, I noticed something funny about the Pi's IP address:

`$ arp -a  
? (10.0.1.1) at 80:ef:94:b6:fc:25 on en0 ifscope [ethernet]  
...   
? (10.0.1.99) at (incomplete) on en0 ifscope [ethernet]`

The Pi was supposed to be at 10.0.1.99... and what's more, `arp` ran really slow for some reason (usually it's a pretty quick lookup).

I was browsing some threads discussing this issue when running `arp` and noticed [this answer](http://askubuntu.com/a/429323/88829), mentioning the physical network being a potential point of failure. I went back over to my switch, unplugged and replugged all the cables... and VOILA! The Pi now gets its reserved IP address.

Also, `arp -a` runs faster, and returns the MAC address (instead of `(incomplete)`) for the Pi.

So, moral of the story: if there's ever a really weird, sudden networking issue with one of your computers, and you haven't changed anything on the software side in some time... it could just be a flaky cable or plug!
