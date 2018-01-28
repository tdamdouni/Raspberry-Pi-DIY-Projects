# A Voice Controlled Jumping Jack- AIY Hampelmann

_Captured: 2018-01-23 at 16:31 from [www.instructables.com](http://www.instructables.com/id/AIY-Hampelmann-a-Voice-Controlled-Jumping-Jack/)_

![](https://cdn.instructables.com/F3R/5920/JBMJYQD8/F3R5920JBMJYQD8.MEDIUM.jpg)

![](https://cdn.instructables.com/FU3/T8J1/JBMJYM7U/FU3T8J1JBMJYM7U.MEDIUM.jpg)

So you have got that AIY voice kit for Christmas, and have been playing with it, following the instructions.   
It's funny, but now?

The project described in the following presents a simple device that can be build using the AIY voice HAT for the Raspberry Pi. It uses the Google voice recognition system to control LEDs and two servos, driving the arms and legs of a jumping jack by a very simple gear.

The software working in the background is a modification of the servo_demo.py script, as it has been described in the AIY voice kit manual. Just follow the instructions given there to set up hard- and software. The device itself is easy to build and requires not much handcrafting skills. In addition a cutter knife, a drill and a soldering iron would be helpful.

If you activate the voice recognition system with a wink of your hand and say 'hands up' the jumping jack will raise hands and legs, 'hands center' will move both servos to the middle position and on 'hands down' hands and legs will be lowered. On 'left up' the left hand and legs will be raised and on "right down" the right ones lowered, on 'right up' vice versa. "Dance", will make it dance, well at least kind of. It is also talking, please have a look on the attached video.

So with little efforts, you can build your own dancing, chatting and singing robot.

To simplify its usage especially by smaller children, and to enhance the 'magic' factor, the button on the AIY box was replaced as trigger by a proximity sensor. For its simplicity, I used a digital distance sensor breakout from Pololu which recognizes if an object is closer than 5 cm, and can be use very much like a button. LEDs do indicate when the device is waiting for orders, listening or "thinking". Servos, sensor and LEDs are controlled by the GPIOZero software library.

The prototype was build from Forex, PVC foam plates, that can be cut very easy with a cutter knife and glued, but is also quite stable. Feel free to build a larger, nicer, improved or more fancy version, but it would be kind if you would document and present your improvements.

You may use both sides of the body, depending whether you want to present the moving gear or have a nice, children-friendly layout.   
\---------  
"Hampelmann" is the German term for "jumping jack", having certain connotations.

## Step 1: Materials Used

![](https://cdn.instructables.com/F5Q/A78F/JBMJXGP3/F5QA78FJBMJXGP3.MEDIUM.jpg)

![](https://cdn.instructables.com/F8T/HPA3/JBMJZ7GZ/F8THPA3JBMJZ7GZ.MEDIUM.jpg)

Raspberry Pi 3; 32 £ at Pimoroni, UK

AIY voice Kit; 25 £ at Pimoroni, UK

Pololu digital distance sensor breakout with Sharp sensor, 5 cm; 5.90 € at Exp-tec.de

Two 9g servos

Two white LEDs and a resistor

Some headers and jumper cables

A 2 mm Forex plate, 250 x 500 mm; 1.70 € at Modulor, Berlin, Germany

M3 screws, nuts and washers, to connect all moving parts. I used six 10 and four 16 mm Nylon screws.

Six M2 screws and nuts, to fix the servos to the plates and connect the servos arms and gears.

A few drops of plastic glue

## Step 2: Assembly and Usage of the Device

![](https://cdn.instructables.com/FP9/25G7/JBMJYM7V/FP925G7JBMJYM7V.MEDIUM.jpg)

![](https://cdn.instructables.com/F73/DFVT/JBMJYM8B/F73DFVTJBMJYM8B.SMALL.jpg)

![](https://cdn.instructables.com/FNQ/H29Z/JBMJXHC6/FNQH29ZJBMJXHC6.MEDIUM.jpg)

![](https://cdn.instructables.com/FND/7CKV/JBMJYM8A/FND7CKVJBMJYM8A.SMALL.jpg)

![](https://cdn.instructables.com/FY4/5YVH/JBMJYM85/FY45YVHJBMJYM85.SMALL.jpg)

![](https://cdn.instructables.com/FOD/BQRM/JBMJYM80/FODBQRMJBMJYM80.SMALL.jpg)

Concerning the AIY voice kit itself, just follow the instructions in the [description](https://www.raspberrypi.org/magpi/issues/essentials-aiy-v1/) that comes with the kit, including the section about the servo. I would recommend to solder several three-pin headers to the servo ports on the AIY voice breakout, so you may connect servos, sensor and LEDs very easy with the HAT.

Concerning the jumping jack, you may either use the drawings I provided here as svg- and PDF-files as a template, or just modify them according to your own ideas. You may like to keep the basic layout of the gear driving the legs and arm of the jumping jack, ensuring that the distance between the pivoting point and the gear is the same at the servo, arm and leg.

Alternatively, you may also construct a version were arms and legs are driven directly by four separate servos, or by a more advanced gear.

Using the drawing, cut the pieces from a Forex, cardboard or plywood plate and drill the holes at the appropriate positions. Glue the distance pieces to the pivoting points of arms and legs, ensuring good alignment of the holes.

Fix the servos and the moving parts to the base plate. Add the distance sensor and LED as indicated. The servos are fixed with M2 screws, all moving parts with M3 screws. I used Nylon M3 screws, but just for esthetic reasons.

Check if the servo arms are placed in the middle position. Connect servo arms and gears, I used M2 screws for this purpose.

Attach servos, LEDs and the distance sensor to the servo connectors on the AIY board. You may need some elongation/jumper cables. I attached the left servo to "servo0" (GPIO 26) the right servo to "servo2" (GPIO 13), the LEDs to "servo5" (GPIO 24), and the sensor to "servo3" (GPIO 5) on the AIY voice HAT.

Copy the provided "Hampelmann.py" file to the AIY "src" subfolder and make it directly executable for anyone. To do so, you may select the file in the file manager, then right click and select Properties, select Permissions, go to Execute, select ~ anyone. Or write "chmod +x src/Hampelmann.py" in the dev console.

Check if everything is set in place and fixed,or movable when required. Open the Dev command line, enter "src/Hampelmann.py" and start the program. If you move your hand or fingers in front of the distance sensor, the AIY unit will ask for orders and the LEDs will blink. Implemented orders are "right/left/hands up/down/center", "dance", "LED on/off" and "goodbye".

Play. Move you hand in front of the sensor, speak when being asked, and give the device a little time to react. Latency is rather high. Crtl+C or "Goodbye" will stop the program.

You may modify the file using Nano or another simple text editor.

Remarks: Please be aware that some words and terms are recognized as words starting with a capital letter, as 'Center' or 'Right Center', as others are not, e.g. 'right up'. You have to use the exact form given back by the voice recognition module to trigger some action.
