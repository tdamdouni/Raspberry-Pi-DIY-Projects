# Carefully Researched Raspberry Pi 3 Active Cooling

_Captured: 2017-10-19 at 21:13 from [blog.hackster.io](https://blog.hackster.io/carefully-researched-raspberry-pi-3-active-cooling-10109a045235)_

While it may not be a problem for normal Raspberry Pi use, when pushed to its limits, these boards will eventually overheat. Once they hit 85°C (185°F), the board responds by either running at a lower speed, or even shutting down completely. [As reported here](http://www.zdnet.com/article/raspberry-pi-microsoft-comes-up-with-a-cool-idea-to-stop-it-overheating/), this wasn't acceptable for a [team at Microsoft Research](https://microsoft.github.io/ELL/tutorials/Active-cooling-your-Raspberry-Pi-3/), which was working on porting image and AI models to run on the [Raspberry Pi](http://hackster.io/raspberry-pi). Without cooling accommodations, these processor-intensive tasks take the board's temperature well above the 85° threshold, necessitating a solution to keep things at a more reasonable range.

![](https://cdn-images-1.medium.com/freeze/max/60/1*kfCD3dZGY89G6NxVWCXapg.jpeg?q=20)![](https://cdn-images-1.medium.com/max/1600/1*kfCD3dZGY89G6NxVWCXapg.jpeg)

> _3D-printed fan mount for the Raspberry Pi 7" touch display. (📷: Microsoft Research)_

While most would stick a heat sync or fan on the board and call it a day, this wasn't good enough for the team, which took infrared images of the Pi running at idle, and after running their AI model for a few minutes. What they found was that while the entire board heats up, the processor temperature shoots well above the rest of the board.

Their solution was to mount a cooling fan just larger than a quarter at an angle to the processor, implementing a 3D-printed bracket to allow use with the Raspberry Pi touchscreen. The fan, along with a heat sync did the trick, keeping the processor at under 50°C under full load. Temperature readings over time were also taken using just a heat sync, just a fan, and no additional cooling apparatus whatsoever. Certainly interesting data for those looking to optimize their hardware performance.
