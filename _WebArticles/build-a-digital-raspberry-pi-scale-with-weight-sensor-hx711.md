# Build a digital Raspberry Pi Scale (with Weight Sensor HX711)

_Captured: 2017-10-27 at 19:02 from [tutorials-raspberrypi.com](https://tutorials-raspberrypi.com/digital-raspberry-pi-scale-weight-sensor-hx711/)_

![Raspberry Pi Waage selber bauen \(mit Gewichtssensor HX711\)](https://tutorials-raspberrypi.com/wp-content/uploads/2017/01/Raspberry-Pi-Waage-selber-bauen-mit-Gewichtssensor-HX711-1024x681.png)

As hardly any scales work analogously, it is of course also possible to measure weights with a digital Raspberry Pi scale. This can be used in various applications as the weight value ranges which can be measured are also almost unlimited. Only a sensor and a load cell are required, which are available for different weight ranges.

In this tutorial we are building a simple Raspberry Pi kitchen scale, whose precision is amazingly accurate. Of course, it is also possible to unscrew an existing (person) scale and read it out using a Raspberry Pi.

## Accessories for the Raspberry Pi Scale

![Raspberry Pi Scale - Load Cell HX711](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Wage-Wägezelle-für-HX711-137x180.jpg)

The most important thing to build your own scale is a "load cell", which is a metal bar with a hole in the center (see picture on the right). This is available for different weight classes (up to 1kg, up to 5kg, up to 50kg, etc.). Even though some have a different form, all are provided with four cables. To read out the values, the HX711 weight sensor is also required. This sensor is available in two versions: red and green. The pressure sensors probably have small differences, but are - theoretically - both compatible. I have used the green HX711. Fixing material is also required.

In summary, the required components are:

  * Load Cell ([US](https://www.amazon.com/s/ref=nb_sb_noss_2?tag=754u-20&url=search-alias%3Daps&field-keywords=load+cell) / [UK](https://www.amazon.co.uk/s/ref=nb_sb_noss/?tag=755-21&url=search-alias%3Daps&field-keywords=load+cell))
  * Two boards (the boards should not bend easily, therefore the best is not too thin plywood)
  * Longer bolts + matching nuts

Alternatively, you can also take an existing [person or kitchen scale](https://www.amazon.com/b/ref=sr_aj?node=678508011&ajr=0&tag=754u-20) and unscrew it. In any cases, a load cell is available and sometimes also a HX711 weighting sensor. With this you could start directly. Since complete scales cost only slightly more than the load cells, this is definitely worth considering.  
If someone has screwed his scale and both are present, I would be pleased about a comment with name / manufacturer of the balance.

## Raspberry Pi Scale - Assembling

Before the load cell is connected to the HX711 weight sensor, it should be mounted on the two plates. For this I made markings with a ballpoint pen on the wooden boards, where the screws come in. With a drill I drilled the holes and inserted the screws. Between the screw and the load cell, there should be a nut, which serves as a protection to the board (see pictures).

![Raspberry Pi Waage Wägezelle](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Waage-Wägezelle-600x338.jpg)

> _Attach the underside of the balance first._

The nuts should be well tightened so that the screws do not slip off the board.

![Raspberry Pi Waage Wägezelle seitlich](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Waage-Wägezelle-seitlich-600x338.jpg)

> _Side view of the scale after both boards are mounted._

If the construction is complete, we can go to the HX711. The four cables of the Load Cell must be connected to the weight sensor. The green HX711, however, has six connections, of which we only need four for the cables. The connection is as follows:

  * Red: E+
  * Black: E-
  * Green: A-
  * White: A+

The pins labeled B+/B- remain empty. Apparently there are versions of the sensor. Where the pins are labeled S+/S- instead of A+/A-.

Now you just have to connect the sensor to the Raspberry Pi. Since this also has only four connections, the wiring is quite simple:

  * VCC to Raspberry Pi Pin 2 (5V)
  * GND to Raspberry Pi Pin 6 (GND)
  * DT to Raspberry Pi Pin 29 (GPIO 5)
  * SCK to Raspberry Pi Pin 31 (GPIO 6)

Schematically, the connection to a [Raspberry Pi 3](https://www.amazon.com/Raspberry-Model-A1-2GHz-64-bit-quad-core/dp/B01CD5VC92/ref=sr_1_3?s=pc&ie=UTF8&qid=1494780060&sr=1-3&tag=754u-20&keywords=raspberry+pi+3) then looks as follows:

![Raspberry Pi HX711 Steckplatine](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-HX711-Steckplatine-600x342.png)

Of course, you can also change the pin assignments of DT and SCK, e.g. If you have an older model. However, you have to adjust the corresponding pins then synonymous in the code.

## Raspberry Pi Weight Sensor Software

To measure the weight and to read out the value we use a Python library. Although there are corresponding [C ++ libraries](https://github.com/ggurov/hx711), however, I have no good experience with that. First, we will clone the project:
    
    
    git clone https://github.com/tatobari/hx711py

It contains an `example.py` file which shows the function of the library and can also be used. Before that, however, a few adjustments are necessary.

First we will edit this file:
    
    
    cd hx711
    sudo nano example.py

We are looking for the line in which the reference unit is set and comment it out with a hashtag sign, so that the line looks as follows:

Save it with CTRL+O and exit with CTRL+X. This reference unit is the divisor, but we must first find it out in the next step. Meanwhile you can run the example (abort with CTRL+C). The values should appear in the range 0 to 200, but this is not important at this point.
    
    
    sudo python example.py

[RF Filters, GPS, WiFi, GSM Band   
Pass, Duplexers and More.](https://tutorials-raspberrypi.com/aclk?sa=l&ai=C7M8shWbzWdKQFpKmpgPIjpHgCZHGxbtNwdvu9Z0GwI23ARABIIO56CJgyQagAdne2_oDyAEGqAMByAMCqgTbAU_QryQapjTJfAKq8Cphm2EB7nyl0rwap_efWuWJzH7eN0UVyJDRLmcG_LYtCIkoS9rz5ImjQWh9pSzveAgj5JaXvKYo54Gnwec2Yem_gRIYpN6XxUuc-jZhk2RQ1YS1XYbGT74NC8VGktqGinRTYJmAMU-K-uA7fHEOdjulWq5QmiUk-wAm1kTrAvLbtgW7Db5jv2QecPcpM-5NZq_P6SC9GdGij7goUOUCbiutZPc2M0Onhq21aMpV1IiunVqIU3vV-dm22Xgpijimt8LSgqlDmF0XtEHLJ9LjXKAGN4AHj6GkBagHpr4b2AcB0ggHCIBhEAEYArEJFDpVJsN4YcPYEwM&num=1&sig=AOD64_1gKip67jGjtMz-zU6j8IJoq5a54w&client=ca-pub-7500567011943156&adurl=https://www.anatechelectronics.com/standard&nb=0)

Ad

[RF filters, RF cable assemblies, for   
Military and Commercial communication …](https://tutorials-raspberrypi.com/aclk?sa=l&ai=C7M8shWbzWdKQFpKmpgPIjpHgCZHGxbtNwdvu9Z0GwI23ARABIIO56CJgyQagAdne2_oDyAEGqAMByAMCqgTbAU_QryQapjTJfAKq8Cphm2EB7nyl0rwap_efWuWJzH7eN0UVyJDRLmcG_LYtCIkoS9rz5ImjQWh9pSzveAgj5JaXvKYo54Gnwec2Yem_gRIYpN6XxUuc-jZhk2RQ1YS1XYbGT74NC8VGktqGinRTYJmAMU-K-uA7fHEOdjulWq5QmiUk-wAm1kTrAvLbtgW7Db5jv2QecPcpM-5NZq_P6SC9GdGij7goUOUCbiutZPc2M0Onhq21aMpV1IiunVqIU3vV-dm22Xgpijimt8LSgqlDmF0XtEHLJ9LjXKAGN4AHj6GkBagHpr4b2AcB0ggHCIBhEAEYArEJFDpVJsN4YcPYEwM&num=1&sig=AOD64_1gKip67jGjtMz-zU6j8IJoq5a54w&client=ca-pub-7500567011943156&adurl=https://www.anatechelectronics.com/standard)

[Anatech Electronics Inc.](https://tutorials-raspberrypi.com/aclk?sa=l&ai=C7M8shWbzWdKQFpKmpgPIjpHgCZHGxbtNwdvu9Z0GwI23ARABIIO56CJgyQagAdne2_oDyAEGqAMByAMCqgTbAU_QryQapjTJfAKq8Cphm2EB7nyl0rwap_efWuWJzH7eN0UVyJDRLmcG_LYtCIkoS9rz5ImjQWh9pSzveAgj5JaXvKYo54Gnwec2Yem_gRIYpN6XxUuc-jZhk2RQ1YS1XYbGT74NC8VGktqGinRTYJmAMU-K-uA7fHEOdjulWq5QmiUk-wAm1kTrAvLbtgW7Db5jv2QecPcpM-5NZq_P6SC9GdGij7goUOUCbiutZPc2M0Onhq21aMpV1IiunVqIU3vV-dm22Xgpijimt8LSgqlDmF0XtEHLJ9LjXKAGN4AHj6GkBagHpr4b2AcB0ggHCIBhEAEYArEJFDpVJsN4YcPYEwM&num=1&sig=AOD64_1gKip67jGjtMz-zU6j8IJoq5a54w&client=ca-pub-7500567011943156&adurl=https://www.anatechelectronics.com/standard)

[Learn more](https://tutorials-raspberrypi.com/aclk?sa=l&ai=C7M8shWbzWdKQFpKmpgPIjpHgCZHGxbtNwdvu9Z0GwI23ARABIIO56CJgyQagAdne2_oDyAEGqAMByAMCqgTbAU_QryQapjTJfAKq8Cphm2EB7nyl0rwap_efWuWJzH7eN0UVyJDRLmcG_LYtCIkoS9rz5ImjQWh9pSzveAgj5JaXvKYo54Gnwec2Yem_gRIYpN6XxUuc-jZhk2RQ1YS1XYbGT74NC8VGktqGinRTYJmAMU-K-uA7fHEOdjulWq5QmiUk-wAm1kTrAvLbtgW7Db5jv2QecPcpM-5NZq_P6SC9GdGij7goUOUCbiutZPc2M0Onhq21aMpV1IiunVqIU3vV-dm22Xgpijimt8LSgqlDmF0XtEHLJ9LjXKAGN4AHj6GkBagHpr4b2AcB0ggHCIBhEAEYArEJFDpVJsN4YcPYEwM&num=1&sig=AOD64_1gKip67jGjtMz-zU6j8IJoq5a54w&client=ca-pub-7500567011943156&adurl=https://www.anatechelectronics.com/standard)

## First Test of our Raspberry Pi Scale

The correct calibration of the weight sensor and the Raspberry Pi balance is crucial. For this we need a comparison object whose weight we know. For example, I have taken two packs of rice (1kg each), since it is recommended to choose an average value of the maximum (my load cell could be used up to 5 kilograms). Place it on the scale and run it again with `sudo python example.py`. The displayed values can be positive as well as negative. In my case were displayed at 2kg (= 2000 gramm) values around -882000. My reference value is thus `-882000 ÷ 2000 = -441`.

We then edit the sample file in the same way as above descirbed, remove the comment hashtag and enter this value accordingly. My line now looks as follows:

After saving and starting the file, the weights should now be displayed as shown in the following video. Since I had the problem that sometimes values below 0 slipped and this should not be possible, I have extended the line, in which the value is read out. This displays no longer negative weights.

In my tests I took a load cell with up to 5kg and calibrated with 2kg. As seen in the video, the measurement is astonishingly accurate. It is important, however, to ensure that the mounted plate does not bend too much (especially the floor plate must be fixed). However, you should be aware that the values outside the range (e.g. above 5kg) will no longer be accurate - a different load cell with its own calibration is required.

How to show text on a LCD display, I have described in [this tutorial](https://tutorials-raspberrypi.com/control-a-raspberry-pi-hd44780-lcd-display-via-i2c) and in the video also used.
