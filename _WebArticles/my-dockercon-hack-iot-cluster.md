# My Dockercon Hack: IoT cluster

_Captured: 2017-08-29 at 10:21 from [blog.alexellis.io](https://blog.alexellis.io/iot-docker-cluster/)_

Adam Herzog (@ah3rz) of Docker's community marketing team reached out to me about _Docker Hacks 2016_ \- a challenge where you submit a cool hack showing something awesome with Docker. Here's what the blog says about the contest:

### Cool hacks

> _The winner(s) of the DockerCon Cool Hack Challenge will receive a free ticket to DockerCon 2016, flight to Seattle and hotel accommodations. Up to two teams will be accepted, maximum 2 members per team._

You can read more on the [blog](https://blog.docker.com/2016/05/dockercon-cool-hack-challenge/). If you're working on something cool then send it in!

#### Background

Ever since I started using Docker on my Raspberry PIs and writing tutorials around it I wanted to find a way to bridge the worlds together. I wanted to raise the profile of Raspberry PI within the Docker world and Docker within the tech community of the Raspberry PI. Here is why I think they meld well together:

  * The RPi community is full of educators, innovators and makers
  * Docker runs very well on all three generations of the Raspberry PI (Zero/A/B/B+), Model 2 and Model 3.
  * GPIO (controlling sensors, LEDs and extension boards) is awesome for opening up IoT possibilities
  * Docker's Native clustering solution (Swarm) works almost out of the box with the Raspberry PI.
  * Raspberry PIs are both cheap and widely available - great for simulating real clusters.

#### The Hack

My hack builds a network cluster from four Raspberry PI Zeros costing just 5USD each and three 8-Segment LED boards. It brings together the IoT functionality of the Raspberry PI and the power and ease of Docker's native clustering capabilities. One PI Zero is designated as a manager and the other three are workers which light up when a web request is passed onto them.

![Diagram of the Hack](https://blog.alexellis.io/content/images/2016/05/rpi_swarm.png)

#### Putting it all together

Earlier in the year I wrote a [magazine tutorial](http://blog.alexellis.io/linux-user-developer-magazine/) for Linux User & Developer showing that Raspberry PIs could scale a web application across multiple devices using Docker Swarm. So I was already half-way towards achieving my hack.

Next I had to prove that Docker could access the GPIO pins of the PI, this was simply a case of building out an image with the relevant Python libraries and system permissions.

> Dockerfile: [alexellis2/python-gpio-arm](https://github.com/alexellis/docker-arm/tree/master/images/armv6/python-gpio-arm)

Once I had turned an LED on and off a few times I moved on to add-on boards such as the [Pimoroni scroll-phat](https://shop.pimoroni.com/products/scroll-phat). I raised a [Pull Request](https://github.com/pimoroni/scroll-phat/pull/46) to have my Dockerfile merged so that anyone can use the board through Docker in the future.

![scroll-phat](http://blog.alexellis.io/content/images/2016/04/pi_swarm.jpeg)

> _Version 0.1 with the scroll-phat showing the CPU count of the Swarm_

I eventually settled on the Ciseco Pi-Liter for its low price of £3.00 and compact form. I didn't want any cables to be trailing off the PI's headers. This kit would have to travel well.

### How it works

We have 4x Raspberry PI Zeros. The first PI is designated as the Swarm Manager and the other boards are Swarm Agents. Each Agent has its own Pi-Liter LED board connected to the 40-pin GPIO header.

  * Consul is started on the Manager
  * Docker Swarm is started on the Manager
  * Three Python Flask containers (iotnode) are started on the swarm and automatically placed on each one of the PIs. These are responsible for turning LEDs on and off.
  * Nginx (a common load-balancer) is started on the Manager and queries the Swarm Remote API to get a list of (iotnode) containers and builds up an nginx.conf file of upstream servers.

This this point `curl` or `apache-bench` is used to make a number of requests to the Nginx load balancer on the Manager. Nginx will distribute the requests across the PI Zeros. Each PI Zero lights up waits 0.1 seconds then turns the LEDs off again using a [simple Python script](https://github.com/alexellis/pizero-docker-demo/blob/master/iotnode/lights.py).

### Watch the video

In the video I give a quick explanation of the setup then use `curl` and Apache Bench `ab` to simulate a real-world load on the cluster.

#### Want to know more?

**Please star or fork** the Github repository for the project:

Do you want to start building your own Docker IoT cluster? Then head over to my Docker ARM portal on Github:

#### What people are saying

My video was re-tweeted by Solomon Hykes: the creator of the Docker Project and I got this, too. I will be getting a framed copy!

![](https://blog.alexellis.io/content/images/2016/05/Screen-Shot-2016-05-17-at-18-38-36.png)

What would you build with Docker and the Raspberry PI? What sensors, lights or add-on boards make sense to you in a cluster? Let me know in the comments or on Twitter @alexellisuk.

> **And please wish me luck with my Dockercon hack :)**
