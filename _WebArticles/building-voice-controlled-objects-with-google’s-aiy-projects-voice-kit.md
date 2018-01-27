# Building Voice-Controlled Objects with Google’s AIY Projects Voice Kit

_Captured: 2017-11-14 at 16:09 from [blog.hackster.io](https://blog.hackster.io/building-voice-controlled-objects-with-googles-aiy-projects-voice-kit-352d3272cede)_

## Do-It-Yourself Artificial Intelligence for the Internet of Things

I've been playing with Google's new [AIY Projects Voice Kit](https://aiyprojects.withgoogle.com/voice) for a couple of months now. I was both fortunate enough to pick up one of the original kits that were distributed with [issue 57 of the MagPi](https://medium.com/@aallan/hands-on-with-the-aiy-projects-voice-kit-7c810856faaf), and then to later get my hands on with a few pre-production hardware samples as the second version of the kit was [made available for pre-order](https://blog.hackster.io/the-google-aiy-projects-voice-kit-is-now-available-for-pre-order-from-micro-center-e20a41537e7) at the end of August.

![](https://cdn-images-1.medium.com/freeze/max/60/1*iK28qTSIts_xNU1njvqDBA.png?q=20)![](https://cdn-images-1.medium.com/max/1600/1*iK28qTSIts_xNU1njvqDBA.png)

> _The Google AIY Projects Voice Kit (right), a retro rotary phone (left), and magic mirror (back)._

Over the I've put together a couple of different projects using the kit. My favourite by far has to be a [retro-computing interface](https://medium.com/@aallan/a-retro-rotary-phone-powered-by-aiy-projects-and-the-raspberry-pi-e516b3ff1528) based around a [GPO 746 Rotary Telephone](http://www.gporetro.com/products/category/rotary-dial-telephones/gpo-746-rotary/). Watching people interact with it was intriguing. Adding simple sounds to imitate a 'real' phone--like a dial tone, a hang up noise, and a simple greeting by an operator--left enough room that people were no longer quite sure whether they were talking to a machine, or human. It lent a curious hesitancy to the interactions that I haven't seen with other voice controlled objects.

However most of my time with the kit has been spent [building a magic mirror](https://medium.com/@aallan/a-magic-mirror-powered-by-aiy-projects-and-the-raspberry-pi-e6a0fea3b4d6) based around the kit and open source [MagicMirror²](https://magicmirror.builders) platform.

But unlike a lot of magic mirror builds you might come across, my mirror was deliberately quite modest. Most builds use full-sized stripped down LCD monitors, this build used a comparatively small 30cm×30cm square frame, while the LCD was the (smaller still) official [7-inch touch screen](http://amzn.to/2gMgbzC). This was a deliberate decision, not only did it reduce the amount of wood working necessary, but it made the mirror portable, and less intimidating.

Like my previous retro-computing build I deliberately made use of sound to attempt to make the mirror more magical. While home hubs like [Amazon Alexa](http://amzn.to/2jq7Whz), or the [Google Home](https://store.google.com/product/google_home), are blatantly creations of technology I've always been fascinated by David Rose's [enchanted objects](http://amzn.to/2yzgTHS). Technology is never really mature until it is invisible, and while voice interfaces are a step towards that I still feel that these interfaces need to be further embedded, hidden, into the environment.

The mirror was also served as a testbed for my exploration of deep learning at the edge, allowing me to [test Google's TensorFlow on the device](https://medium.com/@aallan/a-magic-mirror-with-added-tensorflow-b8fcc5528a6) for simple hotword recognition.

The ability to run these trained networks "at the edge" nearer the data -- without the cloud support that seems necessary to almost every task these days, or even in some cases without even a network connection -- could help reduce barriers to developing, tuning, and deploying machine learning applications. It could potentially help make "smart objects" actually smart, rather than just network connected clients for machine learning algorithms running in remote data centres. It could in fact, be the start of a sea change about how we think about machine learning and how the Internet of Things might be built. Because now there is -- at least the potential -- to allow us to put the smarts on the smart device, rather than in the cloud.

> "The positive reception to Voice Kit has encouraged us to keep the momentum going with more AIY Projects. We'll soon bring makers the 'eyes,' 'ears,' 'voice' and sense of "balance" to allow simple, powerful device interfaces."_ -- __[Google_](https://www.blog.google/topics/machine-learning/aiy-voice-kit-inspiring-maker-community/)_._

I think I've learned a lot more about the user experience behind voice interfaces by experimenting with the form and function of the objects offering the interface than I would have done purely by playing with code. I think kits like [Google's new Voice Kit](http://www.microcenter.com/site/content/google_aiy_preorder.aspx) are invaluable for both makers and product designers alike, and if Google's promises of more kits to come proves to be prophetic then integrating vision, and other sensors, with processing at the edge could move us all closer to an Internet of Things [that makes sense](https://medium.com/@aallan/the-business-of-things-5992c7eb9922) and gives us [more choice when it comes to privacy](https://medium.com/@aallan/has-the-death-of-privacy-been-greatly-exaggerated-f2c4f2423b5).
