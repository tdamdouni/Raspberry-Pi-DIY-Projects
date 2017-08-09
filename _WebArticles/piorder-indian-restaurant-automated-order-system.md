# PiOrder: Indian restaurant automated order system

_Captured: 2017-05-18 at 00:29 from [www.raspberrypi.org](https://www.raspberrypi.org/magpi/piorder-indian-restaurant/)_

Indian restaurant using Raspberry Pi to automate its whole kitchen ordering system

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/05/Main_Image_PiOrder.jpg)

> _PiOrder is an automated ordering system for restaurants developed by Ehsan Rahman. I help at my father's restaurant on Friday and Saturday evenings," says Ehsan._

That establishment is the [Khyber Tandoori](http://magpi.cc/2miqcqv), an Indian restaurant based in Kingswood, Surrey. Thanks to the Raspberry Pi, it has become a highly automated environment.

Two years ago, Ehsan became frustrated at writing orders on pen and paper. Ehsan's answer was to code and hack his way out.

The result is PiOrder, a fully automated EPOS (electronic point of sale) system. PiOrder comprises Raspberry Pis, several Pi Camera Modules, and a [Pipsta](http://magpi.cc/2miwYMQ) thermal printer.

The waiting staff use large Kindle Fire tablets to take orders. Two smaller tablets are kept near the phones so staff can take orders over the telephone.

### The PiOrder automated restaurant ordering system

![PiOrder](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/05/CloseUp.jpg)

> _A Camera Module scans the printer order as it comes through. This scan is used to provide a backup._

  * The Raspberry Pi, housed inside the box, hosts an Apache web server to provide web access
  * The Pipsta printer is used to print out the order. The kitchen staff tear off the order and cook the food

In the kitchen is a Raspberry Pi board hosting the Apache website. A program written in PHP and HTML is used to provide the webpages.  
Apache is used to host the webpage used by the waiting staff to take orders. It also offers online ordering for takeaway customers.  
Chefs are alerted to new orders via a speaker attached to the Raspberry Pi.

The Pipsta printer also prints a hard copy of the order, and a Camera Module takes a photograph of the order to ensure it has printed out correctly (and to act as a backup). More Camera Modules are used by managers to keep an eye on how busy the kitchen is.

As well as making Ehsan's waiting duties easier, PiOrder saves on costs."Just Eat charges approximately £699 + VAT just for signing up," reveals Ehsan. Then it charges around 11% per order, an amount that rapidly racks up.

More importantly, "we have control over our software and order flow," adds Ehsan.

The system is a mixture of PHP, JavaScript, and jQuery, with Bash scripting used to communicate between the Raspberry Pis. "The great thing about Unix files is just how reliable they are," says Ehsan.

The other waiting staff and Ehsan's father have completely stopped using pen and paper.

### Using the PiOrder system in the restaurant

![PiOrder](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/05/Step3_PiOrder.jpg)

There were some teething troubles: the original WiFi system occasionally dropped the connection, and the Pipsta struggled to print large orders. But after sorting those issues, the system has "been resilient." There's an automated test every day at 5:30 for a single popadom, "so the chefs and waiting staff know the system is up and working," explains Ehsan.

There are even spare Raspberry Pi boards in case of failure. "But I've not needed them yet after two years," Ehsan reveals.

As a result of all this tinkering, the restaurant is incredibly high-tech. As well as the ordering system, they are using Raspberry Pi Model B boards as smart CCTV cameras. Ehsan has even set up a Raspberry Pi 3 to act as a remote monitoring system, "so my father can see how busy the restaurant is from home."

Ehsan isn't finished. He plans to enable customers to order food from their table using a smartphone or tablet.

"The chefs and my father were not convinced at first, but slowly they saw the benefit." The waiting staff love the ability to update orders with just a few taps. And the chefs would not go back to reading handwritten orders ever again.

The PiOrder Indian restaurant menu ordering system works like this:

  1. Tablet interface: Waiting staff place orders on a webpage, viewed on Amazon Kindle Fire tablets. A Raspberry Pi running Apache serves up the webpage over a WiFi network.
  2. Kitchen printer: The order is printed out in the kitchen using a Raspberry Pi connected to a Pipsta printer. A Camera Module scans the order as a backup and sends a push alert to the manager.
  3. >Remote management: The manager can keep an eye on how many orders have been placed. The system also enables them to view the kitchen-monitoring and security cameras.
