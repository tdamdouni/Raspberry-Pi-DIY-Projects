# Announcing the AIY Projects Vision Kit

_Captured: 2017-12-02 at 14:58 from [blog.hackster.io](https://blog.hackster.io/announcing-the-aiy-projects-vision-kit-234505bc6eef)_

## The second Google AIY Projects kit has just been announced.

The first Google [AIY Projects](https://aiyprojects.withgoogle.com/) kit arrived free [on the cover of issue 57](https://blog.hackster.io/raspberry-pis-new-aiy-project-s-kit-1b7df33c34ee) of the [MagPi](https://www.raspberrypi.org/magpi/), enabling you to [add voice interaction to your Raspberry Pi projects](https://medium.com/@aallan/hands-on-with-the-aiy-projects-voice-kit-7c810856faaf) using Google's Voice Assistant. The magazine sold out in hours, so a couple of months later a retail version of the Voice Kit was made [available for pre-order](https://blog.hackster.io/the-google-aiy-projects-voice-kit-is-now-available-for-pre-order-from-micro-center-e20a41537e7), and those kits shipped to customers a couple of months after that, in October.

I was fortunate enough to get my hands on some pre-production hardware samples of the retail kit, and over the last few months, in the lead up to the kits arriving onto the shelves, have been [putting together a series of builds](https://blog.hackster.io/building-voice-controlled-objects-with-googles-aiy-projects-voice-kit-352d3272cede) using the Voice Kit.

With the success of the Voice Kit under their belts it was inevitable that more AIY Projects kits were on the way, and today [Google has announced](https://blog.google/topics/machine-learning/introducing-aiy-vision-kit-make-devices-see/) the next, the [Vision Kit](https://aiyprojects.withgoogle.com/vision). It's [available for pre-order at Micro Center](http://www.microcenter.com/site/content/Google_AIY.aspx?utm_source=medium&utm_medium=google_aiy&utm_campaign=Google_AIY_preorder), and is expected to arrive on shelves towards the end of December.

![](https://cdn-images-1.medium.com/freeze/max/60/1*Hna3TxxEEUy-Cv_wK_aQew.png?q=20)![](https://cdn-images-1.medium.com/max/1600/1*Hna3TxxEEUy-Cv_wK_aQew.png)

> _The contents AIY Project Vision Kit. (📷: Google)_

The contents will look familiar to anyone that's [played with the original Voice Kit](https://medium.com/@aallan/hands-on-with-the-aiy-projects-voice-kit-7c810856faaf). The kit consists of the Vision Bonnet, which connects directly to the GPIO header of your Raspberry Pi Zero, two camera cables -- one to connect to the Raspberry Pi Camera, the other to connect the Vision Bonnet to the Raspberry Pi Zero -- a big arcade button, an LED, a piezo buzzer, some spacers, a tripod mounting nut, and a lens assembly which gets fitted in front of the Raspberry Pi Camera module.

Finally there's also the cardboard case which, after [Google Cardboard](https://vr.google.com/cardboard/), has become somewhat synonymous with Google's own prototyping efforts.

The big departure the new kit makes from the "look and feel" of the original [Voice Kit](https://aiyprojects.withgoogle.com/voice/) is the Vision Bonnet itself. Instead of a full HAT the new Vision Kit is [a pHAT](https://www.raspberrypi.org/forums/viewtopic.php?t=166673) -- more commonly know, thanks to Lady Ada -- as a "Bonnet."

> _Vision Bonnet mounted on top of a Raspberry Pi Zero and connected to a Camera module. (📷: Alasdair Allan)_

Designed to work with the lower powered Raspberry Pi Zero, or Zero W, the bonnet--instead of relying on the horse power of the Raspberry Pi's 3 faster processor--has moved a lot of the processing power it needs onto the Vision board itself, and the [Movidius chip](https://www.movidius.com/myriad2) on top hints at the biggest departure from the original Voice Kit.

Unlike the Voice Kit, the Vision Kit is designed to run the all the machine learning locally--on the device--rather than talk to the cloud. While it [was possible to run TensorFlow](https://medium.com/@aallan/a-magic-mirror-with-added-tensorflow-b8fcc5528a6) locally on your Raspberry Pi with the Voice Kit, the previous kit was far more suited to using Google's [Assistant API](https://medium.com/@aallan/a-retro-rotary-phone-powered-by-aiy-projects-and-the-raspberry-pi-e516b3ff1528) or their [Cloud Speech API](https://medium.com/@aallan/a-magic-mirror-powered-by-aiy-projects-and-the-raspberry-pi-e6a0fea3b4d6) to do voice recognition. However the Vision Kit is designed from the ground up to run do all its image processing locally. In theory at least, depending on your project, you can use the kit without any network connection at all.

#### Building the Box

No matter what you intend to do with the the new Vision Kit, your first move is probably going to be to put it together the cardboard version.

Stuffing all the components inside the folded cardboard provided by the Vision Kit looks to be somewhat more difficult that the same process was [for the Voice Kit](https://medium.com/@aallan/hands-on-with-the-aiy-projects-voice-kit-7c810856faaf).

> _Assembling the Vision Kit. (📷: [Google](https://www.blog.google/topics/introducing-aiy-vision-kit-make-devices-see/))_

The cardboard box the kit needs to be poured into is smaller, and sleeker, than the relatively roomy box of the Voice Kit that was--by necessity--larger than you'd expect so that the beefy speaker that Google used in the kit could be fitted inside the case.

This time the wiring harness is a a fair bit more complicated, and folding ribbon cables over and around things is never going to be particularly easy.

However Google have tried to simplify the process, the new button assembly and the connectors on the Vision Bonnet itself are all far more obvious than the original Voice Kit--where assembling the originally arcade button proved to be the most fiddly part of the build--and the cardboard itself looks a fair bit sturdier than last time around.

Closed up the completed Vision Kit shares a lot of visual cues with the Voice Kit, however I think the overall affect is a lot slicker.

> _The completed Vision Kit. (📷: [Google](https://www.blog.google/topics/introducing-aiy-vision-kit-make-devices-see/))_

Intriguingly, in the same way the cardboard box of the original Voice Kit echoed the [Google Home](https://store.google.com/product/google_home), the new Vision Kit also has echoes of the [newly released](https://www.theverge.com/2017/10/4/16402682/google-clips-camera-announced-price-release-date-wireless) [Google Clips](https://store.google.com/product/google_clips). Except this time, the resemblance is a lot more pronounced. Perhaps that's intentional, or perhaps it's just because--at a certain level--all cameras look alike?

#### The Vision Bonnet

The Vision Bonnet is filled with components on both sides. The designer was obviously struggling to pack everything onto the board, and I think they've managed to do a neat job of it.

The most obvious bit of silicon on the top of the board is the Movidius MA2450, a vision processing unit. We've seen the Movidius chip before back in July when [Intel launched the Movidius Neural Compute Stick](https://blog.hackster.io/deep-learning-on-a-usb-stick-29c117cf93e2) -- stuffing machine learning hardware onto a USB stick--and it's a powerful piece of silicon that probably accounts for most of the cost of the board.

> _The AIY Projects Vision Bonnet (top) showing the Movidius MA2450. (📷: Alasdair Allan)_

On top of the board is the connectors for the arcade button and LED, along with an analog I/O header block wired up to the microprocessor on the flip side of the board. Also visible on the top (to the far left) is a camera connector.

This connector is where the Raspberry Pi Camera module is plugged into when you use the board, with another second connector--located at the other end of the board on the underside--being used to connect the Vision Bonnet to the Raspberry Pi Zero's own camera connector with a short length of ribbon cable.

Flipping the board over, the underside is a bit more crowded. The most obvious thing here is the second camera connector, however the main piece of silicon on this side of the board is an Atmel [SAM D09](http://www.atmel.com/products/microcontrollers/arm/sam-d.aspx#samd09).

The smallest member of the SAM D family, the chip is a low power ARM Cortex-M0+ based microcontroller--the little brother of the faster [SAM D21](http://www.atmel.com/products/microcontrollers/arm/sam-d.aspx#samd21) used on the Arduino Zero, MKR1000, and MKRZero boards. The Atmel chip handles the buttons, LEDs, and buzzers in the kit and provides the processing behind the analog I/O headers on the other side of the board--the chip has a 10 channel 12-bit ADC onboard.

> _The AIY Projects Vision Bonnet (underside), Atmel SAM D09 chip visible in the lower right. (📷: Alasdair Allan)_

However also present on underside are a large number of rather tempting test pads. Considering [how useful those exposed pads on the Raspberry Pi Zero](https://blog.hackster.io/adding-usb-ports-to-the-raspberry-pi-zero-c9a50dc40af4) have turned out to be, I'm hoping that there will be some documentation at some point in the future talking about how to use them--or at least gives us an idea of what they're for--that Atmel chip on the board has a lot of pins that aren't, at least on the face of it, currently being used. Perhaps the extra pins are exposed on some of the test pads? It'd be nice.

The Vision Bonnet is a really nice, compact, board. There's a lot crammed in here and a lot of information on the silk screen. I thought having all the names of the AIY Projects team members hidden amongst the other labelling on the flip side of the board was a nice touch.

#### The Software

For those of you who have worked with the Movidius chip before and are starting to worry about how complicated this is going to be you can stop worrying. Google seem to have totally rewritten the SDK and it bears no resemblance to the one shipping with the Movidius Neural Compute Sticks.

Along with the SDK they've also provided three TensorFlow-based pre-trained neural network models for different vision applications. The first, based on [MobileNets](https://research.googleblog.com/2017/06/mobilenets-open-source-models-for.html), can recognise a thousand common objects, a second can recognise faces and their expressions and moods, whilst the third is trained to tell the difference between a person, a cat, and a dog.

However also included are tools to compile new models for the Vision Kit, so you can train and retrain models with TensorFlow in the cloud, and then deploy the trained models onto the Vision Kit.

Like the Voice Kit, the SDK gives you access to the default buttons, LEDs, and piezo buzzer included in the kit. As well as those four analog GPIO pins on the top of the board.

Finally, alongside the SDK, Google is also going to release an AIY companion app for Android. The app allows you to view live video from the Vision Kit, and gives you control over user settings.

#### The Competition?

The comparison with Amazon's [DeepLens](https://aws.amazon.com/blogs/aws/deeplens/) that [launched yesterday](https://venturebeat.com/2017/11/29/amazon-unveils-deeplens-a-249-camera-for-deep-learning/) at [AWS re:Invent](https://reinvent.awsevents.com/) in Las Vegas is so obvious we have to talk about it. It too is intended to run deep learning models directly on the device, out in the field. However there the comparison sort of stops.

Amazon's device is intended, aimed, at software developers and data scientists using machine learning, and Amazon have packed a lot of power into it--a 4 megapixel camera that can capture 1080P video, a 2D microphone array, and even an Intel Atom processor. Intended to sit connected to the mains and be used as a platform, as a tool. It's a finished product, with a [$249 sticker price](http://amzn.to/2ng1efA) to match, not a bare circuit board and a wiring harness inside some cardboard. It also doesn't ship till next April.

Google's kit on the other hand is exactly that, a kit, connecting to the Raspberry Pi it offers us possibilities, the Vision Bonnet has those exposed analog I/O pins, as well as those intriguing test pads on the back.

The Amazon kit is aimed at developers looking to build and train deep learning models in the real world. The Google kit is aimed at makers looking to build projects, or even products. It's an interesting divergence and perhaps shows the underlying motivations of two of the biggest players in this space.

I think the arrival of the Voice, and now the Vision kits, especially with Amazon's DeepLens being announced at almost the same time is telling.

Either gives us the ability to run trained networks "at the edge" nearer the raw data -- without the cloud support that seems necessary to almost every task these days, and even without a network connection -- this could help reduce barriers to developing, tuning, and deploying machine learning applications out in the world.

It could potentially help make "smart objects" actually smart, rather than just network connected thin clients for machine learning algorithms running in remote data centres. It could in fact, be the start of a sea change about how we think about machine learning and how the Internet of Things might be built. Because now there is -- at least the potential -- to allow us to put the smarts on the smart device, rather than in the cloud.

I think all of this is a sign of the next big swing for computing, back, away from the cloud. Towards the edge.

#### Where Now?

I'm in the fortunate position to have got my hands on some pre-production hardware again, so over the next month or so--in the run up to the kits arriving on the shelves--you should expect to see some builds from me using the new kit. I think I'll start [with the magic mirror](https://medium.com/@aallan/a-magic-mirror-powered-by-aiy-projects-and-the-raspberry-pi-e6a0fea3b4d6) I built using the Voice Kit, using the new Vision Kit to replace the awkward custom hotword support with something a bit more seamless -- having the mirror just 'wake up' when someone stands in front of it.

After that? Well, I've got an idea for a project around citizen journalism that might just be the good fit for the kit, but we'll have to wait until I've got some hands on time with the hardware and SDK before I know just how practical it is going to be to build.

Anyway, watch [this space](https://medium.com/@aallan) over the next month or so for more. Or go follow me [on Twitter](http://twitter.com/aallan), where I'll no doubt post some teaser pictures on how the builds are progressing.

#### Available for Pre-order

The new Vision Kit is [available now for pre-order at Micro Center](http://www.microcenter.com/site/content/Google_AIY.aspx?utm_source=medium&utm_medium=google_aiy&utm_campaign=Google_AIY_preorder) and is priced at $44.99. Although pre-orders opened today, the kits themselves are not expected to be on shelves until towards the end of December, and if you don't already have them around you'll need to add a few more things to your basket to get going--a [Raspberry Pi Zero W](http://www.microcenter.com/product/486575/Zero_W?utm_source=medium&utm_medium=google_aiy&utm_campaign=Google_AIY_preorder), a [Raspberry Pi Camera module](http://www.microcenter.com/product/463611/8MP_Raspberry_Pi_Camera_Module?utm_source=medium&utm_medium=google_aiy&utm_campaign=Google_AIY_preorder), an appropriately sized [SD Card](http://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294950358+4294864425+4294863845&utm_source=medium&utm_medium=google_aiy&utm_campaign=Google_AIY_preorder), and of course, a [power supply](http://www.microcenter.com/product/461761/Micro_USB_Wall_Charger?utm_source=medium&utm_medium=google_aiy&utm_campaign=Google_AIY_preorder).

This first batch is a limited run of just 2,000 units and is available in the US only; however there should be world wide availability in the early Spring. I think they're going to sell out pretty quickly, so if you want to get your hands on one of the first batch of kits, I'd pre-order fairly quickly.
