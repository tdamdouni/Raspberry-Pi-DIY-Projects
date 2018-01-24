# Simple Pixel Watch

_Captured: 2017-10-04 at 14:53 from [santamatt.blogspot.de](http://santamatt.blogspot.de/2017/09/simple-pixel-watch.html?m=1)_

Simple Pixel Watch

This is a simple watch using two pixel rings, a Flora and a real time clock (RTC). I wanted a less expensive and lower power consumption alternative to the NeoGeo watch. So I dropped the GPS and positioning boards in favor of a RTC. Construction is easy and fairly quick. You should have some soldering and leather working skills but this is definitely a beginner's level project.

##  Parts List

  * Flora (Adafruit PRODUCT ID: 659) 
  * NeoPixel Ring - 12 x 5050 RGBW LEDs (Adafruit any variant) 
  * NeoPixel Jewel - 7 x 5050 RGB LED (Adafruit any variant but it is best to match the pixel ring. IE. they should both be cool white or both be natural white.) 
  * Real time clock (Adafruit PCF8523 Real Time Clock Assembled Breakout Board) 
  * Battery and charger (Adafruit Micro Lipo w/MicroUSB Jack - USB LiIon/LiPoly charger - v1) 
  * Assorted leather strips 2 ¼ to 2 ½ inches wide. (One will need to be long enough to go around your wrist and overlap 2-3 inches.) 
  * 3 small push button momentary switches (I used Amazon Icstation 12 Type Mini Panel Mount Momentary Tactile Push Button Switch Assortment Kit DIP (Pack of 120)) 
  * Small piece of perfboard (Mine is 1 ¾ by ¾ inches) 

##  Tools

  * Soldering iron 
  * Wire cutters/strippers 
  * Leather cutting scissors or a sharp knife 
  * Leather hole punch 
  * Optional: Thonging chisel (Makes stitching a lot easier.) 

##  Schematic

## ![](https://lh3.googleusercontent.com/0hADGi2Se15OH61MWkKR7NRk33F7nxh_Eq9EHVmIoL0UehnOjl9v6fuDu0a0Z9dUTUsFm2UgkPMkRrFaM3f8NjjIk0_CQv6Qc4Hisnc0q86ifs2RYL1HyBWi9NyJT2gaecoAfIbL)

##  Construction

Step 1: Glue the two pixel rings together, I couldn't find a mark showing pixel 0 on the 12 ring so I just lined up the silk screened text on the back and then did a fine adjustment aligning the pixel LEDs on the front. Glue them together. I used hot glue but any good glue should work.

![](https://lh5.googleusercontent.com/oS6khoB7NwjsOHoTRLUy0wqto0DZq6iKyDxeWyPjtG5f7_ug_0fo1AG0K_yz_tafrw6VfBCt9BlraUjoOo2eBCbn3AsJArYgAEFBhPZ75f5Y_lXaBF2ZorsxDRL2WEnjNndmz6rk)

Don't worry if pixel LED numbers don't line up. The software has a routine to fix that. It is important that the pixel LEDs line up or your watch will look crooked.

![](https://lh6.googleusercontent.com/MoXa9G09bupX36F10J2sMJEQQXmC_5CG6WbP_oRkIpWyU3hdiUWg_dmx3qvBhme4czHWWtPtNIcL7ic13k79D-fdbgqRT0XDxW3G0zhSYdoKBMGwMxOx4Cx0dV0-XWHWyl1wwNz4)

Step 2: Solder wires to the Pixel LED array. I used 22 gauge solid wire for the connects between the pixel LED boards because I wanted the strength. I used 26 gauge stranded wire (cut from an old PBX cable) for the leads for flexibility. Do not connect the pixel LED array to the Flora yet.

![](https://lh5.googleusercontent.com/6x-ORuFo1nGi-ICSsN1uTxXZRjT5_W2c5ErFh-C9Q-RLEPk1zqs94yiRQeHsf9JsK3SlCAM4nuRXnj_3E1AKQ3PbFuQG607yW2JVGTxwiLk-VBSmFNJg90RZoKm-BNW7pJv-nyix)

Step 3: Take a small piece of perfboard and solder a 22 gauge solid wire along one side. Then add four leads, again using the 26 gauge stranded wire. The arrangement of wires should match the location where the switches will be mounted. Do not mount the switches yet.

![](https://lh6.googleusercontent.com/J6MO8kFZjm1rg4S5sNMaQz4aKlpojLhnzj-m9TPV2bHAVShft_sJHfDJr9uiX8eHHiOUvIDl9L6Riio8RMM4S_KqSNDaTxm2NwMGy_d3OdjvUGhw8kEtkfqpY2G8SqYqLMpW6HFM)

> _Step 4: Punch 3 holes in the leather aligned with where the switches will connect to the perfboard._

![](https://lh5.googleusercontent.com/4YDCfnYjmwyu000fJoNSMvK5H-NHE3qIvyBQfgHsKb_l6I0ApcefGBj0BbEEUy07J2T6B3uDy9BRUXedGQfZ8_4AZGRpHSuHK6dPwaEutzpnNI6QCeVVf8OTegbo-ffkWXTEH72F)

Slide the leads of the switches through the leather into the appropriate holes in the perfboard. Bend them over and solder them into place.

Step 5: Cut a thicker piece of leather to hold your circuits.

![](https://lh6.googleusercontent.com/ldVZSqYkSJxorBGfb-pO412zfNyUKMqXVr1oxS5JHRIjvCqKogHPaw8-yQqYO86c1PaMWDvq49FsZJqQrHMofam-6fUr65FkzHmHHsZnOl3t0KXB6INVdWa3PS2LMf5kzFqsxn7e)

Stitch around your perfboard, sandwiching it between the two leather pieces. I found it sufficient to only stitch above and below the perfboard. Be careful to not damage any of the leads coming from the perfboard.

Step 6: Using the 26 gauge stranded wire, attach the RTC to the Flora. Attach the leads from the perfboard to the Flora. I attached the left button to pin 12 of the Flora, middle switch to pin 6 of the Flora and the right button to pin 9 of the Flora.

Step 7: Punch a hole in the light leather arm band where you want the pixel array to be. Pass the leads from the pixel array through the hole and attach them to the Flora. Do not glue down the pixel array yet.

Step 8: Attach the Flora, RTC and LiPo battery to the heavy leather piece. I used a combination of heavy cotton twine, copper wire and hot glue.

![](https://lh4.googleusercontent.com/HuZ0uYJCnu4Sp_Z2Lb_2lnFzjqkYatQPlP-7eEZq6mlztwSldRvnGNRS8hymVJ5anaZmO4mRdLovLp0vdbE_RSgTp4ulBnsl1phU_PcXC7sECmttjUN5SomLhw50ukapKjl9BuAj)

> _Step 9: Connect the Flora to your PC and instal the sketch. The default time on startup is 11:05._

Press the middle button. If everything is correct you should see the hour hand (red led) should be to the left of 12 and the minute hand (blue led) should be to the right of 12 on the outer ring. The blue led on the inner ring should also be at the 12 position. Quickly take note of the actual locations so we can adjust them in the code.

Step 10: Align the 12 position of the inner ring (where you noted the blue led in step 9) toward the top of your watch and glue the pixel array in place. Optionally you can add a bezel around the pixel array. I used a piece of luan.

Step 11: Add snaps, buckles, velcro or whatever closure you have decided to use to the ends of the thin leather strap. I used snaps. The physical construction is complete.

##  Sketch (Software)

```
#include

#include

#include

#include

#define timePIN 6

#define menuPIN 9

#define advPIN 12

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(19, pixPIN);

const int pressed = 0;

const int outerRingOffset = 3;

RTC_PCF8523 rtc;

bool inmenu = false;

int mode = 0,

ssec = 0,

esec = 10,

showFlash = 0,

dispMode = 0;

DateTime currTime = 0,

dispTime = 0,

syncTime = 0;

uint32_t hColor = 0x700000,

mColor = 0x000070,

bColor = 0x400030,

sColor = 0x303030,

noColor = 0x000000;

///////////////////////////////////////////////////// Functions

void clearHands() {

uint8_t i;

for (i = 0; i < 19; i++) {

pixels.setPixelColor(i, noColor);

pixels.show();

int adjustOuter(int raw) {

int ptr = raw + outerRingOffset;

if (ptr > 11) {

ptr = ptr - 12;

return ptr;

void showSecOuter(DateTime showTime) {

pixels.setPixelColor(adjustOuter(showTime.second() / 5), sColor);

void showSecInner(DateTime showTime) {

int sc = (showTime.second() % 5) + 12;

pixels.setPixelColor(sc, sColor);

void showHrMnOuter(DateTime showTime) {

int hr = showTime.hour();

if (hr > 11) {

hr = hr - 12;

int mn = (showTime.minute() / 5);

if (hr == mn) {

pixels.setPixelColor(adjustOuter(hr), bColor);

else {

pixels.setPixelColor(adjustOuter(hr), hColor);

pixels.setPixelColor(adjustOuter(mn), mColor);

void showMnOuter(DateTime showTime) {

int mn = (showTime.minute() / 5);

pixels.setPixelColor(adjustOuter(mn), mColor);

void showMnInner(DateTime showTime) {

int mn = (showTime.minute() % 5) + 12;

pixels.setPixelColor(mn, mColor);

void showHrInner(DateTime showTime) {

int hr = showTime.hour();

if (hr > 11) {

hr = hr - 12;

pixels.setPixelColor(hr / 2 + 13, hColor);

if (hr % 2 == 1) {

pixels.setPixelColor(hr / 2 + 14, hColor);

void showPulse(DateTime showTime) {

if (showTime.second() % 2 == 0) {

pixels.setPixelColor(12, sColor);

void showNum(int theNumber, uint32_t tColor) {

clearHands();

pixels.setPixelColor(theNumber / 12 + 13, mColor);

pixels.setPixelColor(adjustOuter(theNumber % 12), mColor);

pixels.setPixelColor(12, tColor);

pixels.show();

int getNum(int startNum, int limit, uint32_t tColor) {

if (startNum > 2000) {

startNum = startNum - 2000;

showNum(startNum, tColor);

if (digitalRead(menuPIN) == pressed) {

do

while (digitalRead(menuPIN) == pressed);

delay(500);

return startNum;

if (digitalRead(advPIN) == pressed) {

do

while (digitalRead(advPIN) == pressed);

delay(1000);

startNum = (startNum + 1);

if (startNum > limit) {

startNum = 1;

showNum(startNum, tColor);

if (digitalRead(timePIN) == pressed) {

do

while (digitalRead(advPIN) == pressed);

delay(1000);

startNum = (startNum + 12);

if (startNum > limit) {

startNum = 1;

showNum(startNum, tColor);

while (1 == 1);

//////////////////////////////////////////////////// Faces

void caFlash() {

uint8_t i;

clearHands();

pixels.setPixelColor(12, hColor);

pixels.show();

delay(500);

for (i = 13; i < 19; i++) {

pixels.setPixelColor(i, sColor);

pixels.show();

delay(500);

for (i = 0; i < 12; i++) {

pixels.setPixelColor(i, mColor);

pixels.show();

delay(1000);

void cosmicFlash() {

uint8_t i, j;

for (j = 0; j < 3; j++) {

for (i = 2; i < 12; i++) {

clearHands();

pixels.setPixelColor(i, 0x707000);

pixels.setPixelColor(i - 1, 0x404000);

pixels.setPixelColor(i - 2, 0x101000);

pixels.show();

delay(50);

for (j = 0; j < 3; j++) {

for (i = 13; i < 19; i++) {

clearHands();

pixels.setPixelColor(i, 0x707000);

pixels.setPixelColor(i - 1, 0x404000);

pixels.show();

delay(50);

clearHands();

pixels.setPixelColor(12, 0xf0f000);

pixels.show();

delay(100);

void showFace0(DateTime showTime) {

clearHands();

showSecOuter(showTime);

showHrMnOuter(showTime);

showMnInner(showTime);

pixels.show();

void showFace1(DateTime showTime) {

clearHands();

showMnOuter(showTime);

showHrInner(showTime);

showPulse(showTime);

pixels.show();

void showFace2(DateTime showTime) {

clearHands();

showSecOuter(showTime);

showHrMnOuter(showTime);

showMnInner(showTime);

showPulse(showTime);

pixels.show();

void setRTC() {

if (rtc.initialized()) {

currTime = rtc.now();

int yr = getNum(currTime.year(), 72, 0x700000);

int mo = getNum(currTime.month(), 12, 0x303000);

int dy = getNum(currTime.day(), 31, 0x007000);

int hr = getNum(currTime.hour(), 24, 0x003030);

int mn = getNum(currTime.minute(), 60, 0x000070);

rtc.adjust(DateTime(yr, mo, dy, hr, mn, currTime.second()));

else {

int yr = getNum(2017, 72, 0x700000);

int mo = getNum(9, 12, 0x303000);

int dy = getNum(2, 31, 0x007000);

int hr = getNum(23, 24, 0x003030);

int mn = getNum(5, 60, 0x000070);

rtc.adjust(DateTime(yr, mo, dy, hr, mn, 0));

dispMode = 0;

///////////////////////////////////////////////////////////// Setup

void setup() {

// put your setup code here, to run once:

if (! rtc.initialized()) {

rtc.adjust(DateTime(2017, 9, 4, 11, 5, 0));

//setRTC();

rtc.begin();

currTime = rtc.now();

//dispTime = currTime;

//syncTime = currTime;

pinMode(timePIN, INPUT);

pinMode(menuPIN, INPUT);

pinMode(advPIN, INPUT);

digitalWrite(timePIN, HIGH); // activate pullup

digitalWrite(menuPIN, HIGH); // activate pullup

digitalWrite(advPIN, HIGH); // activate pullup

pixels.begin();

pixels.setBrightness(10); // 1/3 brightness

//////////////////////////////////////////////////////////////// Main Loop

void loop() {

if (digitalRead(menuPIN) == pressed)

clearHands();

do

while (digitalRead(menuPIN) == pressed);

delay(500);

inmenu = not(inmenu);

if (inmenu) {

pixels.setPixelColor(12, 0xf00000);

pixels.setPixelColor(dispMode + 13, 0x00f000);

pixels.show();

if (digitalRead(advPIN) == pressed)

clearHands();

do

while (digitalRead(advPIN) == pressed);

delay(500);

dispMode = (dispMode + 1) % 6;

else {

if (digitalRead(timePIN) == pressed)

currTime = rtc.now();

switch (dispMode) {

case 0:

showFace0(currTime);

delay(5000);

break;

case 1:

showFace1(currTime);

delay(1000);

break;

case 2:

showFace2(currTime);

delay(1000);

break;

case 3:

setRTC();

break;

case 4:

if (showFlash == 1) {

caFlash();

showFlash = 0;

showFace0(currTime);

delay(5000);

break;

case 5:

if (showFlash == 1) {

cosmicFlash();

showFlash = 0;

showFace0(currTime);

delay(5000);

break;

else {

if (dispMode == 3) {

setRTC();

else {

clearHands();

showFlash = 1;

```

##  Adjusting the outer ring 12 o'clock position

To move where the 12 o'clock appears on the outer ring you need to change the line:

const int outerRingOffset = 3;

The "3" is the number of spaces to move the 12 led to the right (clockwise) I needed to rotate 3 spaces so I set it to 3. You can set it from 0 (No adjustments) to 11. Once you have set the adjustment you need to reload the sketch.

##  Operation

To show the current watch face press the middle button. It will stay lit as long as you hold the button down and 1-5 seconds after you release the button.

To change the watch face or set the time press the right button. This will hide the "hands" and show the menu selection indicator. Positions 0 (12 o'clock) through 2 select one of three different watch faces. 0 is my favorite. Position 3 will enter the time set routine. Position 4 and 5 are the same watch face as 0 except they play an animation before showing the time. The animations are just a little eye candy to show some of the things the NeoPixels can do. To advance the menu press the left button. Press the right button again to exit the menu and save your selections.

NOTE: Although the time is maintained by the real time clock when the watch is powered down. The menu settings are not. So if the LiPo battery dies or is disconnected you will need to re-enter your menu selections on power up.

To set the time, enter menu mode and select item 3. If the RTC has just been initialized the time will be Sept 4, 2017 11:05:00 You will then have to set:

  * Year center led red 
  * Month center led yellow 
  * Day center led green 
  * Hour center led aqua (light green blue) 
  * Minute center led blue 

Seconds are always set to 0 when exiting the time set function.

The center ring shows multiples of 12 starting with 0 through 5. The outer ring shows single count 0 through 11. So a center ring with led 3 lit and an outer ring with the 5 o'clock led lit would be 2 x 12 + 4 or 28 (remeber both inner and outer leds start at 0.) pressing the left button increments the number by 1. Pressing the middle button increments the number by 12. So from the example above pressing the middle button once and the left button twice will result in 3 x 12 + 6 or 42. Press the right button to advance to the next setting (IE. from year to month). Pressing the right button after setting the minute will set the time, exit the time set function and set the watch face to 0. If you only want to change one number for instance Day, you can just press the left button to accept the other settings without changes.
