# 5V Mini Portable Power Supply

_Captured: 2017-09-13 at 20:32 from [www.instructables.com](http://www.instructables.com/id/5V-Mini-Portable-Power-Supply/)_

![5V Mini Portable Power Supply](https://cdn.instructables.com/F98/Y4FL/J7AQQ0W9/F98Y4FLJ7AQQ0W9.MEDIUM.jpg)

![DSCN2458.jpg](https://cdn.instructables.com/FM5/6DCT/J7AQQ0Z5/FM56DCTJ7AQQ0Z5.MEDIUM.jpg)

All of us who have had some history with tinkering and electronics, have faced an issue quite frequently. The problem of **powering up 5V projects**! Since there are no things such as 5V batteries in the common market and powering up those projects using a 9V battery might be **risky**. The only solution we had to such issues was to add a 5V regulator in our every project. But that was too expensive and tedious and caused a problem whenever the project we had to make was **hectic**. So to solve this problem, I present to you this "**5V Mini Portable Power Supply**". It is based on the usage of a 9V battery (which is easily available to everyone) which makes it good for general use. Since the whole project is made on a 9V battery clip, therefore it is the **same size** as your **generic 9V battery clip**. Therefore supplying the project would be the same as if you were powering it through a 9V battery and battery clip. However, in this case the battery will only be supplying 5V due to the embedded circuit within the project.

That's all for the introduction. So without further ado, let's start making it!

## Step 1: Gathering Around Some Stuff

![Gathering Around Some Stuff](https://cdn.instructables.com/FFG/J7EZ/J70QN2N6/FFGJ7EZJ70QN2N6.MEDIUM.jpg)

![9V to 5V Converter.jpg](https://cdn.instructables.com/F0L/K6B0/J70QN2Q8/F0LK6B0J70QN2Q8.MEDIUM.jpg)

This project is based on "**jellybean parts**"(easily available) therefore you might probably have these parts beforehand. The components required for this project are as follows:

  1. A 9V Battery Clip 
  2. Heat Shrink Tube (1.5-2cm) 
  3. A 5V Voltage Regulator(LM7805) 
  4. A Filtering Capacitor 
  5. Some wire.

> Since I'm into recycling, I have preferred to **salvage** the battery clip from another dead battery. For the heat shrink tube, please make sure that it should easily cover the clip **along with the regulator**.  
The filtering capacitor can be **any electrolytic capacitor** based on the usage. I'll be using my **100uF SMD capacitors **for this purpose.  
  
  
  
  


## Step 2: Soldering the Voltage Regulator and the Capacitor

![Soldering the Voltage Regulator and  the Capacitor](https://cdn.instructables.com/FTT/N0ZH/J70QN2N1/FTTN0ZHJ70QN2N1.MEDIUM.jpg)

![Adding Flux to the Terminals.jpg](https://cdn.instructables.com/FTH/XB4V/J70QN2MR/FTHXB4VJ70QN2MR.SMALL.jpg)

![Terminals Soldered.jpg](https://cdn.instructables.com/FKK/UHIM/J70QN2N7/FKKUHIMJ70QN2N7.SMALL.jpg)

![Preparing the LM7805 Regulator.jpg](https://cdn.instructables.com/FAJ/SRZN/J70QN2N3/FAJSRZNJ70QN2N3.SMALL.jpg)

![Placing The LM7805 Regulator.jpg](https://cdn.instructables.com/FIG/AXBP/J70QN2N2/FIGAXBPJ70QN2N2.SMALL.jpg)

> _Show All Items_

![Soldering the Anode.jpg](https://cdn.instructables.com/FW7/AXHD/J70QN2N4/FW7AXHDJ70QN2N4.SMALL.jpg)

To keep the project compact, I have done everything on the clip itself. Therefore the regulator also has to be placed on the clip. It may be done by following the below steps:

  1. Pick up the 9V battery clip and **cut the metallic plates** which come out of it. Now you should be left with only the 9V battery terminals. Add flux to them and then add solder blobs to them.
  2. In your voltage regulator (**LM7805**), there should be 3 pins, the middle one**(PIN-2)** is the **GND** or the **negative** pin. Remove that pin. This has been done to **prevent shorting** of the pins. 
  3. After that is done, **sand** or **scratch** the top plate of LM7805 using any of your tools. I had used a sandpaper to do so. Keep sanding or scratching it until you are able to see **copper's lustre**. Here, the reason why we're doing this is because the top plate is also a **GND **pin.
  4. Now that the copper of the top plate is exposed, **solder it to the cathode** of the battery clip. Be careful here because the **polarity of the battery clip and any 9V battery is opposite**. Therefore solder the voltage regulator keeping this in mind. 
  5. Solder the left pin or **PIN-1 **(according to the pin configuration posted above) to the anode of the clip.

### The Filtering Capacitor:

Pick up the filtering capacitor and place it along LM7805. After that, solder the **anode of the capacitor to PIN-3** and **cathode to the GND plate **of LM7805.

## Step 3: Drawing Out Wires

![Drawing Out Wires](https://cdn.instructables.com/F72/VDAB/J70QN2MT/F72VDABJ70QN2MT.MEDIUM.jpg)

Now all of the circuitry is done and all that is left is to draw out wires for **supplying 5V output** from the battery. This may be done by simply soldering the wires directly to the **GND plate** and **PIN-3** of LM7805. PIN-3 will be **+5V** and GND plate will be **GND**.

Now that everything has been done, you may test if you're getting 5V output from the drawn out wires using a multi-meter. After you've successfully tested it, proceed to the next step, that is the insulating part.

## Step 4: Insulating Everything

![Insulating Everything](https://cdn.instructables.com/FCC/R7KD/J70QN2PC/FCCR7KDJ70QN2PC.MEDIUM.jpg)

For insulating the entire setup, push your heat shrink tube up the clip and after it is placed ideally, heat it to insulate everything. After the shrinking is done, neatly cut the tube covering the terminals for inserting the battery.

> In my case, I didn't have any heat shrink tube wider than 1cm therefore I had to switch to using tape as a last resort.

That concludes this step.

## Step 5: Congratulations

![Congratulations](https://cdn.instructables.com/FGF/SQ7X/J70QN2PS/FGFSQ7XJ70QN2PS.MEDIUM.jpg)

You have finished making this project and may use it **to power anything** which requires a regulated 5V power supply. So go ahead and make your projects more compact by using this power supply.

That's all for this instructable! If you have any doubt, feel free to comment. Don't forget to **subscribe** if you liked this instructable.

### Project By:

**Utkarsh Verma**

Thanks to **Ashish Choudhary **for lending his camera.
