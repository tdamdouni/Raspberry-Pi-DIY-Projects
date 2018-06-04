# Build a solar-powered nature camera for your garden

_Captured: 2018-04-07 at 08:46 from [www.raspberrypi.org](https://www.raspberrypi.org/blog/solar-powered-nature-camera/)_

Spring has sprung, and with it, sleepy-eyed wildlife is beginning to roam our gardens and local woodlands. So why not follow hackster.io maker reichley's tutorial and build your own solar-powered squirrelhouse nature cam?

![Raspberry Pi- and solar-powered nature camera](https://www.raspberrypi.org/app/uploads/2018/04/squirrel2374_93S8Sgy7XG.jpg)

## Inspiration

"I live half a mile above sea level and am SURROUNDED by animals…bears, foxes, turkeys, deer, squirrels, birds", [reichley explains in his tutorial](https://www.hackster.io/reichley/solar-powered-squirrel-cam-pi-zero-w-797db4). "Spring has arrived, and there are LOADS of squirrels running around. I was in the building mood and, being a nerd, wished to combine a common woodworking project with the connectivity and observability provided by single-board computers (and their camera add-ons)."

## Building a tiny home

reichley started by sketching out a design for the house to determine where the various components would fit.

![Raspberry Pi- and solar-powered nature camera](https://www.raspberrypi.org/app/uploads/2018/04/squirrel2399_aomngvStZ3.jpg)

Since he's fan of autonomy and renewable energy, he decided to run the project's Raspberry Pi Zero W via solar power. To do so, he reiterated the design to include the necessary tech, scaling the roof to fit the panels.

![Raspberry Pi- and solar-powered squirrel cam](https://www.raspberrypi.org/app/uploads/2018/04/squirrel2329_2IDmqifMtd-150x150.jpg)

![Raspberry Pi- and solar-powered squirrel cam](https://www.raspberrypi.org/app/uploads/2018/04/squirrel2334_RXq4G5f1HW-150x150.jpg)

![Raspberry Pi- and solar-powered squirrel cam](https://www.raspberrypi.org/app/uploads/2018/04/squirrel2345_d4tKdjMzBL-150x150.jpg)

To keep the project running 24/7, reichley had to figure out the overall power consumption of both the Zero W and the Raspberry Pi [Camera Module](https://www.raspberrypi.org/products/camera-module-v2/), factoring in the constant WiFi connection and the sunshine hours in his garden.

![Raspberry Pi- and solar-powered nature camera](https://www.raspberrypi.org/app/uploads/2018/04/squirrel_haus_schematic_jKcM8KOoJf.jpg)

He used a LiPo SHIM to bump up the power to the required 5V for the Zero. Moreover, he added a BH1750 lux sensor to shut off the LiPo SHIM, and thus the Pi, whenever it's too dark for decent video.

![Raspberry Pi- and solar-powered nature camera](https://www.raspberrypi.org/app/uploads/2018/04/squirrel2352_B22BPqw6LS.jpg)

To control the project, he used Calin Crisan's [motionEyeOS](https://github.com/ccrisan/motioneyeos) video surveillance operating system for single-board computers.

## Build your own nature camera

To build your own version, [follow reichley's tutorial](https://www.hackster.io/reichley/solar-powered-squirrel-cam-pi-zero-w-797db4), in which you can also find links to all the necessary code and components. You can also check out our free tutorial for [building an infrared bird box](https://projects.raspberrypi.org/en/projects/infrared-bird-box) using the [Raspberry Pi NoIR Camera Module](https://www.raspberrypi.org/products/pi-noir-camera-v2/). As Eben said in our [YouTube live Q&A last week](https://www.youtube.com/watch?v=rsHspM5V11Q), we really like nature cameras here at Pi Towers, and we'd love to see yours. So if you have any live-stream links or photography from your Raspberry Pi-powered nature cam, please share them with us!
