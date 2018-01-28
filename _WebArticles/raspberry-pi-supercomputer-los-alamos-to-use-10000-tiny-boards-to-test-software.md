# Raspberry Pi supercomputer: Los Alamos to use 10,000 tiny boards to test software

_Captured: 2017-12-19 at 09:07 from [www.zdnet.com](http://www.zdnet.com/article/raspberry-pi-supercomputer-los-alamos-to-use-10000-tiny-boards-to-test-software/?utm_content=bufferc8561&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer)_

_Video: A guide to Raspberry Pi in 60 seconds_

The Los Alamos National Lab (LANL) has installed a supercomputer testbed built from a cluster of 750 Raspberry Pis, which could grow to 10,000 Pi boards next year.

A huge cluster of cool-running Raspberry Pi boards has given LANL the answer to a unique challenge faced by people who develop software for 'exascale' supercomputers, such as LANL's giant Cray Trinity, one of the world's top 10 fastest supercomputers.

Software developers have little time to test their software on these high-cost systems because they're fully occupied running many trillions of calculations for actual scientific research.

LANL hasn't revealed the exact cost of the Raspberry Pi cluster, but it suggests it is significantly cheaper and more power-efficient than the alternatives.

For the past seven years LANL has been using older and retired machines with lots of nodes for software development and testing. However, it didn't scale to a Trinity-sized environment, which [has 20,000 nodes](http://www.lanl.gov/projects/trinity/specifications.php). It was expensive to run, requiring water towers for cooling and other equipment.

[According to](http://www.lanl.gov/discover/news-release-archive/2017/November/1113-raspberry-pi.php) Gary Grider, head of its LANL's HPC division, the new Raspberry Pi cluster can offer the same testing capabilities as a dedicated testbed, which could cost $250m and use 25MW of energy.

To buy 750 Raspberry Pi boards at $25 a piece would cost just under $19,000, though that figure is unlikely to reflect the actual cost of the setup. Grider highlights power-efficiency benefits too and estimates that each board in a several thousand node Pi-based system would use 2W to 3W.

The current 3,000-core Pi cluster is a pilot, and LANL intends to boost this setup to 40,000 cores next year, [according to the Raspberry Pi Foundation](https://www.raspberrypi.org/blog/raspberry-pi-clusters-come-of-age/). That increase would mean a cluster of around 10,000 Raspberry Pi boards.

The pilot cluster was built by Australian developer BitScope and distributed by US firm Sicorp. It's constructed out of five rack-mounted Pi Cluster Modules, which consist of 150 four-core Raspberry Pi ARM-based boards. This totals 750 CPUs, representing 3,000 cores.

NANL believes the Pi cluster has applications beyond HPC software development, including better simulation of large-scale sensor networks and HPC network topology research to improve production performance.

![gf13k-bitscope-blade-cluster-lights.jpg](https://zdnet2.cbsistatic.com/hub/i/r/2017/11/29/1d1677be-274f-47bf-975d-e18f03fb3e87/resize/770xauto/1480caeecf5a840f34b91c1b46ec996d/gf13k-bitscope-blade-cluster-lights.jpg)

> _Los Alamos hasn't revealed the cost of its Raspberry Pi cluster but suggests it is significantly cheaper and more power-efficient than the alternatives._

China already had the world's fastest supercomputer, but now it's crowding out the US in the top 500.

Commodity hardware makes possible massive 100,000 node clusters, because, after all, commodity hardware is "cheap" \-- if you're Google. What if you want a lot of cycles but don't have a few million dollars to spend? Think Raspberry Pi.

Last week I wrote about a 300 node cluster using Raspberry Pi (RPi) microcomputers. But can you do useful work on such a low-cost, low-power cluster? Yes, you can. Hadoop runs on massive clusters, but you can also run it on your own, highly-scalable, RPi cluster.

The Raspberry Pi is a tiny, ultra-cheap computer--and it has taken the world by storm. This ebook offers an overview of what this little board can do and how it's being put to use.
