# Build an Object Detection DC Motor Controller

_Captured: 2017-11-22 at 09:15 from [www.allaboutcircuits.com](https://www.allaboutcircuits.com/projects/building-raspberry-pi-controllers-part-3-object-detection-dc-motor-controll/)_

### Previous Articles in Series:

### Intro

In the [previous Build Raspberry Pi Controllers project](https://www.allaboutcircuits.com/projects/building-raspberry-pi-electronic-controlllers-part-2controlling-leds/) you learned how to build a a programmable LED flasher. To start the LED flashing cycle, a tactile pushbutton switch had to be pressed. Although the tactile pushbutton switch is a basic manual method of providing an input control signal for the RPi to process and provide an appropriate output response, an automatic approach to control can be achieved by using a sensor. Photocells or light dependent resistors (LDRs) are often used to automatically turn lights on at night. The typical night light has a photocell that detects darkness based on a change in its resistance. When darkness has been detected by the photocell, the light turns on. Applying the same working principle of a typical night light, we can operate a small DC motor in a similar manner. In this project, you will build an object detection DC motor controller. The block diagram for our object detection DC motor controller is shown in Figure 1. The electronic components required to build the object detection DC motor controller are shown in the Parts List.

![](https://www.allaboutcircuits.com/uploads/articles/object_detection_dc_motor_controller_A.png)

> _Figure 1. The electrical-electronics and embedded hardware required to build the object detection DC motor controller._

### Project Parts List

  * Raspberry Pi (Model A+,B, B+, or the Pi 2)
  * (R1) [220 ohm resistor](https://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_690700_-1) (red, red, brown, gold), 1/4W, 5% 
  * solderless breadboard
  * DMM (digital multimeter) or VOM (volt-ohm-milliammeter)
  * jumper wires (hand stripped 22 AWG [American Wire Gauge]) solid wires or Adafruit Breadboard wires Product ID: 153)

### Light Detection and the Photocell

A photocell is a light sensitive resistor. Antother term used in electrical textbooks or electronics hobbyists magazines is light dependent resistor or LDR. If you never seen a photocell, Figure 2 shows the electrical symbol and component view of a LDR..

![](https://www.allaboutcircuits.com/uploads/articles/photocell_component_electrical_symbol_A.png)

> _Figure 2. The electrical symbol and component view of a photocell_

The photocell's electrical response to light is the changing of resistance. The more light the photocell receives on its sensitive surface, the more its resistance decreases down to a few hundred ohms. In the dark, the photocell resistance is in the megaohms. A simple experiment can be conducted to see how the photocell's resistance changes based on light levels. First, take a DMM (digital multimeter) and set it to read ohms. Adjust the ohmmeter scale to the 20 kilo ohm setting. Attach the DMM's positive and negative test leads across the photocell as shown in Figure 3. The reading displayed on the ohmmeter will be in a few thousands of ohms.

![](https://www.allaboutcircuits.com/uploads/articles/Photocell_light_measurement_A.png)

_**Figure 3**. The authors ohmmeter is reading a value of 3.11Kilo-ohms.** Note**: Resistance values will vary based on the ambient light received by the photocell._

Next, adjust the scale to the highest megaohm setting. Place your hand over the photocell and you will see a resistance value in a few millions of ohms as shown in Figure 4.

![](https://www.allaboutcircuits.com/uploads/articles/Photocell_dark_measurement.png)

_**Figure 4**. The author's ohmmeter is reading a value of 1.587 megaohms._

For best results, make a collimator (a device that narrows light) by cutting the barrel of an ink pen and painting the inside of it black. Once dried, place the collimator over the photocell. Placing the collimator over the photocell reduces ambient (outside) light from disturbing the resistance reading of the ohmmeter. I made a collimator using the "finger grip" of a non-working ink pen as shown in Figure 5. The resistance measurement value obtained in Figure 4 was based on my homebrew "finger grip" collimator. These mininum and maximum photocell resistance values will allow us to wire a simple light sensor switch to the RPi on a solderless breadboard.

![](https://www.allaboutcircuits.com/uploads/articles/Homebrew_photocell_collimator.png)

_**Figure 5. **The author's homebrew collimator built from an ink pen finger grip._

### Building a Simple Light Sensor Switch

We will use the photocell along with a pull-up resistor to make a simple light sensor switch. Figure 6 shows a basic circuit schematic diagram of the simple light sensor switch wired to a RPi GPIO pin. The voltage drop will be proportional to the amount of photocell resistance. For example, placing an object or your hand over the photocell will provide an approximate +3,3VDC voltage drop across the LDR. Removing the object or your hand will reduce the photocell's resistance thereby providing a proportional small voltage drop across it. The voltage drop will be read by the RPi GPIO pin. The Python code will read the absence and presence of the light as either +3.3VDC or 0VDC. Thus, the electrical behavior of an ordinary tactile pushbutton - digital switch will be emulated by using a simple light sensor circuit. The next phase of the project is to build and test a DC motor operated by a transistor.

![](https://www.allaboutcircuits.com/uploads/articles/Photocell_rpullup_light_sensor_circuit_B.png)

_**Figure 6**. A simple light sensor switch built using a photocell and a pull-up resistor. **Note:** The pull-up resistor is programmed electrical component using a single line of Python code._

### Build the Transistor Motor Driver Circuit

The next phase of the project build is to wire an electronic circuit that will operate a small DC motor. A single bipolar junction transistor (BJT) with an appropriate amplification factor (_B_eta) can be used to operate or drive a small DC motor. You can easily build a transistor DC motor driver by building the circuit on a solderless breadboard as shown in Figure 7. I've also included the electronic circuit schematic diagram as additional wiring reference material shown in Figure 8. Once the circuit has been built on the solderless breadboard, pressing the tactile pushbutton switch will turn on the small DC motor wired to the transistor's collector lead. If the DC motor doesn't spin, remove the battery pack from the circuit and recheck your wiring and proper component orientation of the 1N4001 rectifier diode and the 2N2222 NPN transistor. After the wiring errors have been corrected, reconnect the battery pack and test the circuit again, Congratulations on building a functional transistor motor driver circuit! Now, let's see how the DC motor driver circuit works by reviewing basic transistor theory.

![](https://www.allaboutcircuits.com/uploads/articles/Transistor_DC_Motor_Driver_breadboard.PNG)

> _Figure 7. The transistor motor driver solderless breadboard wiring diagram_

![](https://www.allaboutcircuits.com/uploads/articles/BJT-Motor-Starter.png)

_**Figure 8.** The electronic circuit schematic diagram of a typical transistor DC motor driver _

### Basic Transistor Theory

The transistor is able to operate the DC motor because of electrical source current that flows from the +6VDC Battery pack through the collector - emitter leads to ground. The DC motor winding is in series between the collector lead and the +6VDC battery pack. The electrical current from the +6VDC battery pack flows through the dc motor winding allowing it to rotate. In order for the electrical current to flow through the collector-emitter leads and the DC motor winding, the transistor must be turned on. To turn on a transistor, an electronic circuit operation technique called forward biasing must be used. Forward biasing a transistor consists of an input voltage applied to the base-emitter junction being greater than 0.7V (700 mV). Also, the transistor must be properly wired based on the semiconductor component type. BJT component types consist of a PNP or NPN pin configuration. The 2N2222 transistor is a NPN component.

The collector and emitter leads are negative (N-material) with the base being positive (P-Material). Figure 9 shows the pin configuration and package type for the 2N2222 NPN transistor. As shown in Figure 8, the base is attached to the +6VDC battery pack positive-red wire through a tactile pushbutton switch and a 220 ohm series limiting resistor with the emitter wired to ground (the black wire). A 220 ohm resistor is attached to the transistor's base to reduce the full battery current and heat from damaging it. The 220 ohm resistor is a nice resistance value to allow a sufficient amount of base current to flow so the transistor will turn on properly. Also, the 1N4001 diode prevents back peak reverse current from the DC motor winding damaging the transistor when it turns off. If you're interested in learning more about this semiconductor device, read AAC's article on[ Bipolar Junction Transistors](https://www.allaboutcircuits.com/textbook/semiconductors/chpt-2/bipolar-junction-transistors/) for additional electrical theory information. Let's proceed to the final hardware build of the project.

![](https://www.allaboutcircuits.com/uploads/articles/2N2222_NPN_transistor_package_symbol.png)

> _Figure 9. The electronic symbol and component package type for the 2N2222 NPN transistor_

### Final Hardware Build 

With the transistor motor driver circuit working properly, we are now ready to complete the final hardware build for the project. The final electrical wiring for the object detection/DC motor controller is to wire the driver circuit to the Raspberry Pi. In the LED flasher project, the [Adafruit Pi cobbler](https://www.adafruit.com/products/914) was used to connect the opto-isolator and supporting circuit components to the appropriate RPi's GPIO pins. The Pi Cobbler provides convenience in terms of having all the RPi GPIO pins accessible on the solderless breadboard for electrical wiring to electronic interfacing circuits. Therefore, the same circuit wire assembly technique will be used in this project as well. Figure 10 shows the solderless breadboard wiring for the object detection DC motor controller. Again, the electronic circuit schematic diagram shown in Figure 11 is provided as an additional wiring resource.

![](https://www.allaboutcircuits.com/uploads/articles/Photocell_dc_motor_control.PNG)

_**Figure 10**.The complete object detection DC motor controller wiring diagram assembled on a solderless breadboard. **Notice** the removal of the tactile pushbutton switch, +6VDC battery pack and new placement location of the electronic components on the solderless breadboard._

![](https://www.allaboutcircuits.com/uploads/articles/Photocell-Motor-Driver.png)

_**Figure 11**. The electronic circuit schematic diagram for the object detection DC motor controller_

I provided an example of the object detection DC motor controller by way of my prototype unit shown next. I used an old Erector set metal base with a [Meccano DC motor](http://http://www.meccanospares.com/EM02-BK-O.html) attached to it for my prototype build. Also, a video clip showing how the controller work is provided in the link below. The final step to making our object detection DC motor controller operational is to add the Python code.

![](https://www.allaboutcircuits.com/uploads/articles/Photocell_RPi_DC_motor_control.png)

> _Final build of the author's the object detection DC motor controller. The 2N2222 transistor has enough Beta to properly drive the Meccano erector motor without overheating it._

_**Figure 12.**_

### The Object Detection Python Code

The Python code shown below is a program re-use from the LED flasher project. The variable names were changed to reflect the physical components wired to the RPi. The code works by placing an object over the photocell to turn the DC motor on. A second placement of the object over the sensor will turn the DC motor off. As discussed earlier, the pull-up resistor is a programmed component using the following line of Python code:

GPIO.setup(photocell_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

The entire Python program can be typed onto the LXTerminal by opening the nano editor with the linux command ~sudo nano object detection.py. Also, the python program can be saved on your RPi's SD card by clicking the code button below.
    
    
                        # ***********Object Detection code******************
    #
    # inspired by Simon Monk, Raspberry Pi Cookbook, 2013
    #
    # modified by Don Wilcher Dec 18, 2015
    #
    # Placing a object over the photocell will turn on the dc motor. 
    # Placing an object over the photocell a 2nd time turns off the motor.
    
    # Add libraries to python script
    
    import RPi.GPIO as GPIO
    import time
    
    # Include BCM I/O pins into python script and define pin numbers
    
    GPIO.setmode(GPIO.BCM)
    photocell_pin = 4
    motor_pin = 18
    
    # Create photocell pin as an active low switch (use RPi internal pullup resistor)
    # and define motor pin as an output.
    
    GPIO.setup(photocell_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(motor_pin, GPIO.OUT)
    
    # Define and set (initialize) the motor output state as False and the old input event as True
    
    motor_state = False
    old_input_event = True
    
    # pbswitch event monitoring loop: check pbswitch_pin and toggle dc motor  output based on input events
    # being True or False
    while True:
        new_input_event = GPIO.input(photocell_pin)
        if new_input_event == False and old_input_event == True:
            motor_state = not motor_state
        old_input_event = new_input_event
        GPIO.output(motor_pin, motor_state)
        time.sleep(0.1)#provides a 100 msec motor actuation on/off time
                      

With the objection detection Python code entered into the LX Terminal, type the Linux command ~sudo python object_detection.py after the prompt onto the screen. Take an object and place it over the photocell: the DC motor should be spinning. Place the same object over the LDR to turn off the motor. A big congratulations is in order! You now have an operational object detection DC motor controller. An application for an object detection device is a non-contact start switch for a conveyor system. Instead of using a standard pushbutton switch to start the conveyor, a basic hand motion will operate it. Explore other applications with your object detection DC motor controller and record them in a lab notebook. Next time, we'll investigate how to build an event counter using the RPi along with litteBits modules.
