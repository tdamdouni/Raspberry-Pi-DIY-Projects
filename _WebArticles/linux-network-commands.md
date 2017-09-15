# Linux Network Commands

_Captured: 2017-09-01 at 20:59 from [dzone.com](https://dzone.com/articles/linux-network-commands?edition=321391&utm_source=Daily%20Digest&utm_medium=email&utm_campaign=Daily%20Digest%202017-09-01)_

[Download the blueprint](https://dzone.com/go?i=228233&u=https%3A%2F%2Foffers.automic.com%2Fblueprint-to-continuous-delivery-with-automic-release-automation%3Futm_campaign%3DAMER%252520Online%252520Syndication%252520DZone%252520Platinum%252520Sponsorship%252520Ads%252520JULY-2017%26utm_source%3DDzone%252520Ads%26utm_medium%3DBlueprint%252520to%252520CD) that can take a company of any maturity level all the way up to enterprise-scale continuous delivery using a combination of Automic Release Automation, Automic's 20+ years of business automation experience, and the proven tools and practices the company is already leveraging.

In the previous post, we talked about [Linux process managemen](https://likegeeks.com/linux-process-management/)t. In this post, we will talk about Linux network commands and how to troubleshoot your network.

Once you have confirmed that the physical network is working, the next step is to troubleshoot your network and here we come to our topic which is Linux network commands and how to use them to troubleshoot your network.

We are going to cover the most used Linux network commands.

## Check Network Connectivity Using Ping Command

The ping command is one of the most used Linux network commands in network troubleshooting. It is used to check whether or not a specific IP address can be reached.

The ping command works by sending an ICMP echo request to check the network connectivity.

`$ ping google.com`

![ping linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/01-ping-linux-network-commands.png)

These results are showing a successful ping, and it can be described as the trip of an echo request issued by our system to google.com.

This command measures the average response. If there is no response, then maybe there is one of the following:

  * There is a physical problem on the network itself.
  * The location might be incorrect or non-functional.
  * The ping request is blocked by the target.
  * There is a problem in the routing table.

If you want to limit the number of echo requests made to 3, you can do it like this:

`$ ping -c 3 google.com`

![ping -c Linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/02-ping-c-Linux-network-commands.png)

> _Here the ping command stops sending echo requests after 3 cycles._

There are some issues that you should consider about the ping command. These issues may not necessarily mean that there is a problem, like:

**Distance to the target**: If you live in the U.S. and you ping a server on Asia, you should expect that this ping will take much more time than pinging a server in the U.S.

**The connection speed**: If your connection is slow, ping will take longer time than if you have a fast connection.

**The hop count**: This refers to routers and servers that the echo travels across until it reaches its destination.

The important rule about the ping is that a low ping is always desirable.

## Get DNS Records Using Dig and Host Commands

You can use the dig command to verify DNS mappings, host addresses, MX records, and all other DNS records for a better understanding of DNS topography.

The dig command was developed to replace the `nslookup` command.

`$ dig google.com`

![dig linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/03-dig-linux-network-commands.png)

The dig command by default searches for A records; you can obtain information for specific record types like MX records or NS records.

`$ dig google.com MX`

![dig mx linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/04-dig-mx-linux-network-commands.png)

> _You can get all types of records by using the ANY query._

`$ dig google.com ANY`

![dig ANY linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/05-dig-ANY-linux-network-commands.png)

> _The dig command makes a reverse lookup to get DNS information like this:_

`$ dig -x 8.8.8.8`

![dig -x linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/06-dig-x-linux-network-commands.png)

> _The dig command does its query using the servers listed on /etc/resolv.conf._

The host command is similar to the dig command.

`$ host -a google.com`

![host linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/07-host-linux-network-commands.png)

> _Also, you can perform reverse lookups using the host command._

`$ host 8.8.8.8`

So both commands work in a similar way, but the dig command provides more advanced options.

## Diagnose Network Latency Using the traceroute Command

The traceroute command is one of the most useful Linux network commands. It is used to show the pathway to your target and where the delay comes from. This command helps basically in:

  * Providing the names and the identity of every device on the path.
  * Reporting network latency and identify at which device the latency comes from.

`$ traceroute google.com`

![traceroute linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/08-traceroute-linux-network-commands.png)

The output will provide the specified host, the size of the packet that will be used, the IP address, and the maximum number of hops required. You can see the hostname, IP address, the hop number, and packet travel times.

To avoid reverse DNS lookup, use the -n option.

`$ traceroute -n google.com`

![traceroute -n linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/09-traceroute-n-linux-network-commands.png)

By using the traceroute command, you can identify network bottlenecks. The asterisks shown here means there is a potential problem in routing to that host, as the asterisks indicate packet loss or dropped packets.

The traceroute command sends a UDP packet, traceroute can send UDP, TCP, and ICMP.

If you need to send an ICMP packet, you can send it like this:

`$ sudo traceroute -I google.com`

![traceroute -I linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/10-traceroute-I-linux-network-commands.png)

> _A TCP variation can be used like this:_

`$ sudo traceroute -T google.com`

![traceroute -T linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/11-traceroute-T-linux-network-commands.png)

> _This is because some servers block UDP requests, so you can use this method._

In this case, you can send UDP, ICMP, or TCP to bypass these issues.

## Mtr Command (Real-Time Tracing)

This command is an alternative to the traceroute command.

`$ mtr google.com`

![mtr linux network command](https://likegeeks.com/wp-content/uploads/2017/03/12-mtr-linux-network-command.png)

The best thing about the mtr command is that it displays real-time data, unlike traceroute.

Furthermore, you can use the mtr command with the -report option, this command sends 10 packets to each hop found on its way, like this:

`$ mtr --report google.com`

![mtr report linux network command](https://likegeeks.com/wp-content/uploads/2017/03/13-mtr-report-linux-network-command.png)

> _This command gives a huge amount of details, better than traceroute._

If this command doesn't run using a normal user account, you should use root, since some distros adjust the permission of this binary for root users only.

## Checking Connection Performance Using the ss Command

The socket statistics command ss is a replacement for netstat; it's faster than netstat and gives more information.

The ss command gets its information directly from the kernel instead of relying on [/proc directory](https://likegeeks.com/linux-virtual-file-system/#proc-File-System) like the netstat command.

`$ ss | less`

![ss linux network command](https://likegeeks.com/wp-content/uploads/2017/03/14-ss-linux-network-command.png)

This command outputs all TCP, UDP, and UNIX socket connections and pipes the result to the [less command ](https://likegeeks.com/main-linux-commands-easy-guide/#less-Command)for better display.

You can combine this command with either the -t to show TCP sockets, -u to show UDP, or -x to show UNIX sockets. You should use the -a option combined with any of these options to show the connected and listening sockets.

`$ ss -ta`

![ss -ta linux network command](https://likegeeks.com/wp-content/uploads/2017/03/15-ss-ta-linux-network-command.png)

> _To list all established TCP sockets for IPV4, use the following command:_

`$ ss -t4 state established`

![ss established connections](https://likegeeks.com/wp-content/uploads/2017/03/16-ss-established-connections.png)

> _To list all closed TCP states:_

`$ ss -t4 state closed`

You can use the ss command to show all connected ports from a specific IP:

`$ ss dst XXX.XXX.XXX.XXX`

And you can filter by a specific port like this:

`$ ss dst XXX.XXX.XXX.XXX:22`

## Install and Use the iftop Command for Traffic Monitoring

The iftop utility or iftop command is used to monitor the traffic and display real-time results.

You can download the tool like this:

`$ wget http://www.ex-parrot.com/pdw/iftop/download/iftop-0.17.tar.gz`

Then extract it:

`$ tar zxvf iftop-0.17.tar.gz`

Then compile it:

`$ cd iftop-0.17 $ ./configure $ make $ make install`

If you got any errors about libpcap, you can install it like this:

`$ yum install libpcap-dev`

And you can run the tool as a root user like this:

`$ sudo iftop -I <interface> `

![iftop command](https://likegeeks.com/wp-content/uploads/2017/03/19-iftop-command.png)

> _You will see this table with a real-time data about your traffic._

Add the **-**P option with iftop to show ports.

`$ sudo iftop -P`

![iftop -P linux network commands](https://likegeeks.com/wp-content/uploads/2017/03/20-iftop-P-linux-network-commands.png)

You can use the **-B** option to display the output in bytes instead of bits, which is shown by default.

`$ iftop -B`

![iftop -B linux ntwork command](https://likegeeks.com/wp-content/uploads/2017/03/21-iftop-B-linux-ntwork-command.png)

> _There a lot of options; you can check them man iftop._

## ARP Command

Systems keep a table of IP addresses and their corresponding MAC addresses; this table is called the ARP lookup table. If you try to connect to an IP address, your router will check for your MAC address. If it's cached, ARP table is not used.

To view the arp table, use the arp command:

`$ arp`

![arp linux network command](https://likegeeks.com/wp-content/uploads/2017/03/22-arp-linux-network-command.png)

By default, the arp command shows the hostnames. You can show IP addresses like this instead:

`$ arp -n`

![arp -n linux network command](https://likegeeks.com/wp-content/uploads/2017/03/23-arp-n-linux-network-command.png)

> _You can delete entries from the arp table like this:_

`$ arp -d HWADDR`

## Packet Analysis with tcpdump

One of the most important Linux network commands is the tcpdump command. The tcpdump command is used to capture the traffic that is passing through your network interface.

This kind of access to the packets which is the deepest level of the network can be vital when troubleshooting the network.

`$ tcpdump -i <network_device>`

![tcpdump linux network command](https://likegeeks.com/wp-content/uploads/2017/03/18-tcpdump-linux-network-command.png)

> _You can also specify a protocol (TCP, UDP, ICMP and others) like this:_

`$ tcpdump -i `<network_device>`  tcp `

Also, you can specify the port:

`$ tcpdump -i `<network_device>` port 80 `

tcpdump will keep running until the request is canceled; it is better to use the -c option in order to capture a pre-determined number of events like this:

`$ tcpdump -c 20 -i ``<network_device>`

You can also specify the IP to capture from using src option or going to using dst option.

`$ tcpdump -c 20 -i `<network_device>` src XXX.XXX.XXX.XXX `

You can obtain the device names like this:

`$ ifconfig`

![ifconfig linux network command](https://likegeeks.com/wp-content/uploads/2017/03/17-ifconfig-linux-network-command.png)

You can save the traffic captured from tcpdump to a file and read it later with -w option.

`$ tcpdump -w /path/ -i ``<network_device>`

And to read that file:

`$ tcpdump -r /path`

I hope that Linux network commands we've discussed in this post help you troubleshoot some of your network problems and make the right decision.

Thank you.

[Download](https://dzone.com/go?i=228234&u=https%3A%2F%2Foffers.automic.com%2Fblueprint-to-continuous-delivery-with-automic-release-automation%3Futm_campaign%3DAMER%252520Online%252520Syndication%252520DZone%252520Platinum%252520Sponsorship%252520Ads%252520JULY-2017%26utm_source%3DDzone%252520Ads%26utm_medium%3DBlueprint%252520to%252520CD) the 'Practical Blueprint to Continuous Delivery' to learn how Automic Release Automation can help you begin or continue your company's digital transformation.
