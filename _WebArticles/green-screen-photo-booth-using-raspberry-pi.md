# Green Screen photo booth using Raspberry Pi

_Captured: 2017-05-25 at 13:42 from [www.winkleink.com](http://www.winkleink.com/2017/02/green-screen-photo-booth-using.html?m=1)_

![](https://4.bp.blogspot.com/-lXzN7hljpVc/WKXrvu7rM_I/AAAAAAAASZc/Cr2We7wwHjMw2eFY0_542IgAuT_MtRkqQCLcB/s280/superman_returns_greenscreen.jpg)

How cool would that be to make your own version of the special effects used in big budget movies.

So, I started the search for tools under Linux that would permit the green screen to be done.

As a short summary green screen[/**chroma key**](https://en.wikipedia.org/wiki/Chroma_key) is where a a single colour is removed from an image.

Most often it is green as modern cameras are more sensitive to green and a bright green works best as it's less likely to be a colour in a natural scene. I remember when I was younger hearing it being done with blue screen as well.

After a bit of looking I found **[Imagemagick**](https://www.imagemagick.org/script/index.php) a jack of all trades image processing tool. It has a function to remove a single colour from an image and as importantly for my use includes a 'fuzzy' search for the colour which gave a bit of tolerance to the lighting.

I know there is a lot going on in there. She short version is it takes imagescam.png, makes transparent the colour rgbnum with a tolerance of fuzzpercent and saves it as imagecamt.png

Once I had my head around this it was then a matter of doing the rest of the code.

For testing I used some of my kids PlayMobil and a piece of A0 green card.

All looks like it's working well even with the ability to change the background using the arrow keys

This of course means I needed a [green screen background with standard](http://ebay.to/2kD3MOi) that I bought from eBay. No idea when I'll use the black or white backgrounds that came with this kit, but I have them now.

Finally, wouldn't it be great to have a little remote control and not have to rely on a keyboard. Since the Raspberry Pi 3 has Bluetooth I thought this might be the ideal solution. No wires and no messing about. Since Pygame was already being used for the displaying of the images and I knew Pygame had joystick support built in this looked like the obvious choice.

Again, on eBay I found this small little **[Bluetooth gamepad**](http://ebay.to/2lQ9Rf3) and thought it would be perfect. Super small which means you can have it in your hand but not interfere with your final picture.

![](https://4.bp.blogspot.com/-Vsu_k6q8eB8/WKX9S-VhGRI/AAAAAAAASaE/m7Xob8DmhbIRWCNyMz-Cxk0X-uFXkMSMQCLcB/s320/IMG_2815.JPG)

> _Iddy biddy, teeny weeny, black gamepad_

My usual style is before bring a new feature into a project I like to test it standalone to make sure it works. For the gamepad I created a small [Python/Pygame program to test the gamepad](https://github.com/winkleink/pygame_test_gamepad)

It paired with the Raspberry Pi first time and worked perfectly with the gamepad test program. So, 100% sure it will function with the chromaCam setup.

Now all the parts are in place. PiCamera to take the picture. Imagemagick to remove the background colour. Pygame to merge background, foreground picture with green removed and finally an overlay with the background images changed with the keyboard or the super small gamepad. (Oh yeah, the circular thing at the bottom is an analogue joystick)

The chromaCam set up got it's outing at the last Wimbledon Raspberry Jam. Here are some pictures.

On the day I used a camera tripod and a lot of tie wraps to hold the Pi Display and the Pi Camera onto the tripod. I would definitely recommend a more secure mounting method

![](https://4.bp.blogspot.com/-78jeEKOAS74/WKX-rQ4HQuI/AAAAAAAASaY/UhzPzOSA9bABSOcoy5QBg255-b1UhftBgCLcB/s280/IMG_2928.JPG)

> _Getting set up https://twitter.com/MrTomsWorld_

![](https://2.bp.blogspot.com/-dg_r0Q5nVvo/WKX-rHYKggI/AAAAAAAASaM/onGDwQZ6e64VyPiuFFqwAf8NvpiVaNoSgCLcB/s280/harry_potter.jpg)

> _Who doesn't love a bit of Harry Potter - https://twitter.com/rdhayler_

![](https://4.bp.blogspot.com/-HrUiGjEf3rg/WKX-rXfeGPI/AAAAAAAASaQ/VXAwRWzIyLEoN9TaZ6-mHtzHQRhLpkZ8QCLcB/s280/lion.jpg)

> _Those Lions are dangerous_

![](https://2.bp.blogspot.com/-awQ3doIYPyI/WKX-rdRneuI/AAAAAAAASaU/syEmdPEvDTMNJnZDHf1_0-qZYY1bpjfvQCLcB/s280/marcus_dinosaur.jpg)

> _That doesn't look like a sensible thing to do - https://twitter.com/HackHorsham_

![](https://2.bp.blogspot.com/-5VYFMAwNNx4/WKYBHGDfEKI/AAAAAAAASak/46lHtcrmtGgomZpPAEVrblw8hHn_u5l3QCLcB/s280/bad_2.jpg)

> _Taking out too much - https://twitter.com/Codepope_

![](https://3.bp.blogspot.com/-LOXyIqc6ddM/WKYBHIhf1UI/AAAAAAAASag/C1WddV_hWdkUwQGHDoyu02RSX57GvYLqQCLcB/s280/not_right.jpg)

> _I'm sure the top of the Raspberry Pi logo isn't transparent_

![](https://4.bp.blogspot.com/-9owqt6cJ2mo/WKX-rEPoOFI/AAAAAAAASaI/fRI91frSGMIpN2bOBPH-ijchqmRNf0VvACLcB/s280/grace.jpg)

> _A few bits of rogue green - https://twitter.com/gowolade_

If you want to make your own Green Screen Photo Booth then the code is available on **[GitHub**](https://github.com/winkleink/ChromaCam)

Yes, this project worked and was great fun to build and see people using it.

For the project I limited the image size to 640x480 as even at that resolution it took about 2 seconds for the picture to be updated. This meant it took a little bit of patients to get the picture you wanted before pressing the button to Tweet the image.

I took the set up to **[Hack Horsham**](https://twitter.com/hackhorsham) as well but I didn't bring my own lighting and the lighting in the room was perfect for a Jam but didn't give enough contrast for chromaCam to work. So, it didn't make the final cut and I stuck to **[Button Flash**](http://www.winkleink.com/2016/08/buttonflash-game-made-with-raspberry-pi.html).

Again, this was a great learning experience for me and once the computing power for the Raspberry Pi enables it or access to the GPU is supported this will be amazing when the green screen transparency can be done in real time.

I expect as new devices come out I'll be revisiting this project to see if the performance is improved.
