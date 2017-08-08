# Raspberry Pi As Speed Camera 

_Captured: 2016-04-06 at 11:09 from [hackaday.com](http://hackaday.com/2016/04/03/raspberry-pi-as-speed-camera/)_

![](https://hackadaycom.files.wordpress.com/2016/03/pi-speed-cam-featured1.jpg?w=800)

Wherever you stand on the topics of road safety and vehicle speed limits it's probably fair to say that speed cameras are not a universally popular sight on our roads. If you want a heated argument in the pub, throw that one into the mix.

But what if you live in a suburban street used as a so-called "rat run" through route, with drivers regularly flouting the speed limit by a significant margin. Suddenly the issue becomes one of personal safety, and all those arguments from the pub mean very little.

![Sample car speed measurements](https://hackadaycom.files.wordpress.com/2016/03/carspeed_sample.gif?w=800)

> _Sample car speed measurements_

[Gregtinkers]' brother-in-law posted a message on Facebook outlining just that problem, and sadly the local police department lacked the resources to enforce the limit. This set [Gregtinkers] on a path to document the scale of the problem and lend justification to police action, [which led him to use OpenCV and the Raspberry Pi camera to make his own speed camera](http://gregtinkers.wordpress.com/2016/03/25/car-speed-detector/).

The theory of operation is straightforward, the software tracks moving objects along the road in the camera's field of view, times their traversal, and calculates the resulting speed. The area of the image containing the road is defined by a bounding box, to stop spurious readings from birds or neighbours straying into view.

He provides installation and dependency instructions and a run-down of the software's operation in his blog post, and [the software itself is available on his GitHub account](https://github.com/gregtinkers/carspeed.py).

We've had [a lot of OpenCV-based projects](http://hackaday.com/tag/opencv/) but haven't featured a speed camera before here on Hackaday. But we have had a couple of dubious countermeasures, like [that humorous attempt at an SQL injection attack](http://hackaday.com/2014/04/04/sql-injection-fools-speed-traps-and-clears-your-record/), or [a flash-based countermeasure](http://hackaday.com/2012/10/23/traffic-camera-countermeasure/).
