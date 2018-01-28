# Custom LED Lights on DIY Electric Skateboard - Raspberry Pi

_Captured: 2017-12-29 at 05:32 from [www.hackster.io](https://www.hackster.io/theraspberrypiguy/custom-led-lights-on-diy-electric-skateboard-raspberry-pi-8ca243)_

![Custom LED Lights on DIY Electric Skateboard - Raspberry Pi](https://hackster.imgix.net/uploads/attachments/399518/skateboard_lights_xs6S7sXoKf.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

Last year I made a DIY electric skateboard using a Raspberry Pi Zero and Wiimote. My homemade electric skateboard can reach speeds of up to 30km/h, accelerates in true Tesla-fashion and travels over 13km on a single charge… But… As with everything in life, it could be made better with LEDs! Lots of them!

![](https://hackster.imgix.net/uploads/attachments/399521/p1040282_E3hUNiHHwP.JPG?auto=compress%2Cformat&w=680&h=510&fit=max)

Recently I used two 26-long NeoPixel strips from Adafruit to jazz up the underside of my board. NeoPixels are fully programmable RGB LEDs that are incredibly bright - perfect for lighting up the pavement as you carve it up on a skateboard. Take a look at the video below:

This guide is not just limited to electric skateboards however, you can customise any skateboard you want! Electric ones, especially of the DIY variety, lend themselves to this the most as there is already a battery to draw power from.

**_Parts List_**

* **NeoPixel strip/s** - Adafruit stock whole reels of NeoPixels that can easily be cut down to the necessary size. The number of NeoPixels on your board is totally up to you - more will lead to a brighter, more vibrant effect, however that comes with the trade-off of using more power. I used two 26-long strips, making 52 NeoPixels in total.

* **Battery** - a battery of some kind will be needed to power your NeoPixels. Bear in mind that the more NeoPixels you are using, the more current your battery will need to be able to provide at any instant. LiPo batteries are usually quite lightweight and energy dense, however they do require a specialist charger to recharge them. Also note that your batteries will most likely be mounted onto the bottom of your skateboard. Unsurprisingly this area is prone to knocks and incidents like rocks being kicked upwards at it. Batteries, _especially_ Lithium-based ones, do **not** like this. If a rock punctures a LiPo battery then it can rapidly set fire and/or explode. Whatever battery option you go for ensure that you have adequate protection. For my project, I am taking power off of my electric skateboard's main battery. This is a ~22V 8AH LiPo - it is encased in foam and a plastic box too.

![](https://hackster.imgix.net/uploads/attachments/399523/p1040254_WDfs055dkQ.JPG?auto=compress%2Cformat&w=680&h=510&fit=max)

* **Voltage Regulator Module**- your battery will probably not provide the exact 5V of goodness that your NeoPixels need to function. Consequently, you will need a voltage regulator. I would recommend using a step-down buck converter. Remember that skateboards are prone to a lot of vibrations so bear that in mind. My original step-down buck converters (LM13 modules) were shaken to pieces! I quite like these converters as they are encased in metal: [https://www.amazon.co.uk/Converter-Adjustable-Module-Regulated-Supply/dp/B00H1MZ794/ref=sr_1_22?ie=UTF8&qid=1514440804&sr=8-22&keywords=buck+converter ](https://www.amazon.co.uk/Converter-Adjustable-Module-Regulated-Supply/dp/B00H1MZ794/ref=sr_1_22?ie=UTF8&qid=1514440804&sr=8-22&keywords=buck+converter)

* **Microcontroller Board **- my electric skateboard is entirely controlled by a Raspberry Pi Zero… But when it came to adding these lights I didn't want to bother the on-board Pi with extra work. Because of this I added a small Arduino Nano (a clone board can be picked up for less than £5) and I am using this as the NeoPixel driver board. I would recommend an Arduino or similar microcontroller.

**_Assembly_**

1\. Firstly, ensure that your battery is fully charged. Then mount it inside your casing - don't forget to keep the charging cables accessible! After this take your buck converter/voltage regulator module and wire the output of your battery to the input of your converter. Be cautious and check to make sure that you have connected the positive lead to the positive input and the same for the negatives. I would recommend soldering these wires together and then covering them in heat shrink for protection.

2\. Next grab a multimeter and connect it up to the output of your buck converter. Adjust the screw on the top of the converter until your voltage reads 5V. After this, disconnect your multimeter.

3\. Now you need to prepare your NeoPixels. If you have purchased yours in a reel then cut the specific number you would like. You can just use scissors to cut along the gold connection pads between the actual LEDs. I have found that the rubber casing that they come in makes a good semi-waterproof/semi-dirtproof casing, though it is up to you whether you want to use it as such.

4\. Notice that NeoPixels strips have three inputs on them: +5V, ground and data. You can now use a soldering iron to solder the output power lines of your buck converter to the gold +5V and ground connection pads on your NeoPixels. Again, ensure that you are connecting the right ones! Soldering to the gold pads can be a tricky task. I usually find it is best to deposit some solder onto them first, then use your iron to reheat it and place a wire.

5\. With the power to your NeoPixels successfully connected, all that is left to do is to connect the single data line and a ground wire from your Arduino/microcontroller. I would tackle ground first: use your soldering iron to solder a wire to a ground pin on your Arduino and then connect that to the ground of your NeoPixels. This is the common ground.

6\. Finally wire a PWM-enabled pin from your microcontroller to the data line of your NeoPixels. For me I have used pin** 6** of my Arduino Nano.

In my project, I use two 26 NeoPixel strips, however my Arduino just treats them as a single strip, with all patterns being mirrored. To do this I just connected another NeoPixel strip to the exact same connections and Arduino pin that I connected the first strip too!

When you have finished wiring up your LEDs, stick them to your skateboard! Getting them to stick can be challenging… I resorted to super glue. You may also want to use some plastic protective casing for the exposed wires in this project.

**_Programming _**

Adafruit has a comprehensive programming and information over at their website so you can find out how to create your own patterns of lights etc. I am actually using a collection of the Adafruit demos. My code is below and on GitHub [here](https://github.com/the-raspberry-pi-guy/skateboard/blob/master/arduino_neopixel/ALTERNATIVE_PATTERNS/ALTERNATIVE_PATTERNS.ino):
    
    
    // Skateboard Neopixel Program
    // Controls 2*26 sets of neopixels on the bottom of my DIY electric skateboard
    // Used an Arduino Nano to control the lights to save logic level conversion on the Pi Zero and worrying about task management
    // Wiimote 'A' button triggers Pi that then triggers Arduino inputs that then turn on the lights
    #include <Adafruit_NeoPixel.h>
    #ifdef __AVR__
     #include <avr/power.h>
    #endif
    #define PIN 6
    #define BUTTON 7
    #define INTERRUPT_PIN 2
    Adafruit_NeoPixel strip = Adafruit_NeoPixel(26, PIN, NEO_GRB + NEO_KHZ800);
    void setup() {
     strip.begin();
     strip.show();
     pinMode(BUTTON, INPUT);
     attachInterrupt(digitalPinToInterrupt(INTERRUPT_PIN), ISRturn_off, RISING);
     }
    void loop() {
     int value = 0;
     int but_val = 0;
     blank();
     while (true){
       but_val = digitalRead(BUTTON);
       if (but_val == 1){    
           sequence();
         }
       if (but_val == 0){
           blank();
         }
       }
     }
    void ISRturn_off(){
     blank();
     }
    void colorWipe(uint32_t c, uint8_t wait) {
     for(int i = (strip.numPixels()-1); i >= 0; i = i - 1) {
       strip.setPixelColor(i, c);
       strip.show();
       delay(wait);
       }
     }
    void sequence(){
     colorWipe(strip.Color(255, 0, 0), 25);
     colorWipe(strip.Color(0, 255, 0), 25); 
     colorWipe(strip.Color(0, 0, 255), 25);
     for(int i = 0; i <=4; i++){
       theaterChase(strip.Color(127, 127, 127), 25); // White
       theaterChase(strip.Color(127, 0, 0), 25); // Red
       theaterChase(strip.Color(0, 0, 127), 25); // Blue
     }
     rainbow(20);
     rainbowCycle(20);
     theaterChaseRainbow(25);
     }
    void blank(){
     colorWipe(strip.Color(0, 0, 0), 25);
     }
    /////// ADAFRUIT PRESET PATTERNS BELOW//////////
    void rainbow(uint8_t wait) {
     uint16_t i, j;
     for(j=0; j<256; j++) {
       for(i=0; i<strip.numPixels(); i++) {
         strip.setPixelColor(i, Wheel((i+j) & 255));
       }
       strip.show();
       delay(wait);
     }
    }
    // Slightly different, this makes the rainbow equally distributed throughout
    void rainbowCycle(uint8_t wait) {
     uint16_t i, j;
     for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
       for(i=0; i< strip.numPixels(); i++) {
         strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
       }
       strip.show();
       delay(wait);
     }
    }
    //Theatre-style crawling lights.
    void theaterChase(uint32_t c, uint8_t wait) {
     for (int j=0; j<10; j++) {  //do 10 cycles of chasing
       for (int q=0; q < 3; q++) {
         for (uint16_t i=0; i < strip.numPixels(); i=i+3) {
           strip.setPixelColor(i+q, c);    //turn every third pixel on
         }
         strip.show();
         delay(wait);
         for (uint16_t i=0; i < strip.numPixels(); i=i+3) {
           strip.setPixelColor(i+q, 0);        //turn every third pixel off
         }
       }
     }
    }
    //Theatre-style crawling lights with rainbow effect
    void theaterChaseRainbow(uint8_t wait) {
     for (int j=0; j < 256; j++) {     // cycle all 256 colors in the wheel
       for (int q=0; q < 3; q++) {
         for (uint16_t i=0; i < strip.numPixels(); i=i+3) {
           strip.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
         }
         strip.show();
         delay(wait);
         for (uint16_t i=0; i < strip.numPixels(); i=i+3) {
           strip.setPixelColor(i+q, 0);        //turn every third pixel off
         }
       }
     }
    }
    // Input a value 0 to 255 to get a color value.
    // The colours are a transition r - g - b - back to r.
    uint32_t Wheel(byte WheelPos) {
     WheelPos = 255 - WheelPos;
     if(WheelPos < 85) {
       return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
     }
     if(WheelPos < 170) {
       WheelPos -= 85;
       return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
     }
     WheelPos -= 170;
     return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    }
    

Note that this is for my specific project: when I press the _A_ button of the Wiimote controlling my electric skateboard, a Bluetooth signal is sent to the Pi Zero underneath. The Pi Zero then sets one of its GPIO pins to high. This GPIO pin is connected to an interrupt pin on my Arduino. When this detects a change in state, my NeoPixel LED code is triggered.

If you want to keep things simple and would like your lights to come on just when you turn on the power, then use the _strand test _Adafruit demo. Don't forget to change the number of NeoPixels you are using and the pin it is connected to! [https://github.com/adafruit/Adafruit_NeoPixel/blob/master/examples/strandtest/strandtest.ino ](https://github.com/adafruit/Adafruit_NeoPixel/blob/master/examples/strandtest/strandtest.ino)

**_Conclusion_**

In conclusion, this has been a super fun project. NeoPixels are great. The ability to program your own LED patterns is something that few skaters would even dream of being able to do!
