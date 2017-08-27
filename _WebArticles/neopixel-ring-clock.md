# NeoPixel Ring Clock

_Captured: 2017-08-24 at 23:50 from [learn.adafruit.com](https://learn.adafruit.com/neopixel-ring-clock?view=all)_

![](https://s3.amazonaws.com/learn-production/guides/images/000/000/504/medium800/neopixel-ring-clock-adafruit-necklace.jpg?1448301643)

> _NeoPixel Ring Clock_

![flora_neopixel-ring-clock-adafruit-necklace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/167/large1024/flora_neopixel-ring-clock-adafruit-necklace.jpg?1392142267)

Build a clock with NeoPixel rings and FLORA! The FLORA GPS provides accurate timekeeping, and the clock's circular motif make it a handsome addition to your desk, wall, or even around your neck.

![flora_neopixel-ring-clock-adafruit-desk-version.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/168/large1024/flora_neopixel-ring-clock-adafruit-desk-version.jpg?1392142463)

> _To build this project you will need:_

  * [GPS antenna](http://www.adafruit.com/products/960) with [SMA to uFL adapter](http://www.adafruit.com/products/851) (optional)
  * packing or painter's tape
  * double sided tape
![flora_neopixel-ring-clock-adafruit-materials-00.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/203/large1024/flora_neopixel-ring-clock-adafruit-materials-00.jpg?1392226314)

![flora-neopixel-ring-clock-diagram.png](https://cdn-learn.adafruit.com/assets/assets/000/014/209/large1024/flora-neopixel-ring-clock-diagram.png?1392229359)

NeoPixel rings connect as follows:

  * +5V -> FLORA VBATT
  * GND -> FLORA GND
  * outer ring Data Input -> FLORA D12
  * outer ring Data Out -> inner ring Data Input

FLORA GPS connects as follows:

  * GPS GND -> FLORA GND
  * GPS 3.3V -> FLORA 3.3V
  * GPS RX -> FLORA TX
  * GPS TX -> FLORA RX
  * GPS BAT -> positive side of coincell holder
  * GPS GND -> negative side of coincell holder

power circuit via USB or battery connected to JST port

  * ![flora_neopixel-ring-clock-adafruit-04.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/152/medium640/flora_neopixel-ring-clock-adafruit-04.jpg?1392138313)

  * ![flora_neopixel-ring-clock-adafruit-04.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/152/thumb160/flora_neopixel-ring-clock-adafruit-04.jpg?1392138313)

  * ![flora_neopixel-ring-clock-adafruit-02.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/153/thumb160/flora_neopixel-ring-clock-adafruit-02.jpg?1392138406)

Line up your FLORA and GPS module according to the circuit diagram. You'll be attaching them back to back!  
  
Solder wires onto the FLORA GPS' GND, TX, RX, 3.3V pins. Solder two longer wires to the GND and BAT pads on the FLORA GPS.

  * ![flora_neopixel-ring-clock-adafruit-03.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/154/medium640/flora_neopixel-ring-clock-adafruit-03.jpg?1392138498)

  * ![flora_neopixel-ring-clock-adafruit-03.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/154/thumb160/flora_neopixel-ring-clock-adafruit-03.jpg?1392138498)

  * ![flora_neopixel-ring-clock-adafruit-05.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/155/thumb160/flora_neopixel-ring-clock-adafruit-05.jpg?1392138584)

Use a piece of double-sided tape to position the GPS in the center back of FLORA, with the wires pointing towards the appropriate FLORA pads.

  * ![flora_neopixel-ring-clock-adafruit-06.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/156/medium640/flora_neopixel-ring-clock-adafruit-06.jpg?1392138766)

  * ![flora_neopixel-ring-clock-adafruit-06.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/156/thumb160/flora_neopixel-ring-clock-adafruit-06.jpg?1392138766)

  * ![flora_neopixel-ring-clock-adafruit-07.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/157/thumb160/flora_neopixel-ring-clock-adafruit-07.jpg?1392138864)

  * ![flora_neopixel-ring-clock-adafruit-08.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/158/thumb160/flora_neopixel-ring-clock-adafruit-08.jpg?1392139022)

  * ![flora_neopixel-ring-clock-adafruit-13.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/159/thumb160/flora_neopixel-ring-clock-adafruit-13.jpg?1392139309)

Clip wires to length, strip the ends, and solder the four connections to FLORA.  
  
Route the two long BAT/GND wires through an unused hold on FLORA (like D9).

  * ![flora_neopixel-ring-clock-adafruit-12.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/160/medium640/flora_neopixel-ring-clock-adafruit-12.jpg?1392139504)

  * ![flora_neopixel-ring-clock-adafruit-12.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/160/thumb160/flora_neopixel-ring-clock-adafruit-12.jpg?1392139504)

  * ![flora_neopixel-ring-clock-adafruit-11.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/161/thumb160/flora_neopixel-ring-clock-adafruit-11.jpg?1392140184)

  * ![flora_neopixel-ring-clock-adafruit-10.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/162/thumb160/flora_neopixel-ring-clock-adafruit-10.jpg?1392141050)

  * ![flora_neopixel-ring-clock-adafruit-09.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/163/thumb160/flora_neopixel-ring-clock-adafruit-09.jpg?1392141134)

  * ![flora_neopixel-ring-clock-adafruit-14.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/164/thumb160/flora_neopixel-ring-clock-adafruit-14.jpg?1392141541)

  * ![flora_neopixel-ring-clock-adafruit-19.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/166/thumb160/flora_neopixel-ring-clock-adafruit-19.jpg?1392142076)

Thread on a coincell battery holder. BAT goes to + and GND goes to - on the holder. Adjust the wire lengths to position the battery holder on the FLORA as shown (we'll use foam tape to stick it down later).  
  
Solder these connections and insulate the back of the holder with tape.  
  
Plug in the FLORA via USB and test the GPS circuit according to the [FLORA GPS guide.](http://learn.adafruit.com/flora-wearable-gps)

  * ![flora_neopixel-ring-clock-adafruit-15.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/165/medium640/flora_neopixel-ring-clock-adafruit-15.jpg?1392142042)

  * ![flora_neopixel-ring-clock-adafruit-15.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/165/thumb160/flora_neopixel-ring-clock-adafruit-15.jpg?1392142042)

  * ![flora_neopixel-ring-clock-adafruit-16.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/169/thumb160/flora_neopixel-ring-clock-adafruit-16.jpg?1392142614)

  * ![flora_neopixel-ring-clock-adafruit-17.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/170/thumb160/flora_neopixel-ring-clock-adafruit-17.jpg?1392142735)

  * ![flora_neopixel-ring-clock-adafruit-18.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/171/thumb160/flora_neopixel-ring-clock-adafruit-18.jpg?1392143067)

Arrange the two NeoPixel rings face down on your work surface. It can help to use tape, sticky side up, on your desk to help keep the rings aligned while you solder.  
  
Make small pieces of solid-core wire shaped like staples to connect 5V, GND, and data between the two pixel rings according to the circuit diagram.

  * ![flora_neopixel-ring-clock-adafruit-21.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/172/medium640/flora_neopixel-ring-clock-adafruit-21.jpg?1392143415)

  * ![flora_neopixel-ring-clock-adafruit-21.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/172/thumb160/flora_neopixel-ring-clock-adafruit-21.jpg?1392143415)

  * ![flora_neopixel-ring-clock-adafruit-22.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/173/thumb160/flora_neopixel-ring-clock-adafruit-22.jpg?1392143630)

  * ![flora_neopixel-ring-clock-adafruit-23.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/178/thumb160/flora_neopixel-ring-clock-adafruit-23.jpg?1392150044)

Solder longer wires as shown to the extra 5V and GND on the outer ring, as well as data input.  
  
Place the GPS/FLORA circuit in the center and solder these longer wires to VBATT, D12, and GND on FLORA according to the circuit diagram.  
  
Test the NeoPixel rings by downloading the [NeoPixel](http://learn.adafruit.com/adafruit-neopixel-uberguide) code library and running one of the test Arduino sketches provided.
![flora_neopixel-ring-clock-adafruit-24.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/179/large1024/flora_neopixel-ring-clock-adafruit-24.jpg?1392153321)
    
          1. //https://github.com/zeroeth/time_loop
      2. Adafruit_GPS GPS(&Serial1);
      3. // Set GPSECHO to 'false' to turn off echoing the GPS data to the Serial console
      4. // Set to 'true' if you want to debug and listen to the raw GPS sentences
      5. // this keeps track of whether we're using the interrupt
      6. boolean usingInterrupt = false;
      7. const uint8_t gamma[] = {
      8. 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
      9. 0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,
      10. 1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,  2,  3,  3,  3,  3,
      11. 3,  3,  4,  4,  4,  4,  5,  5,  5,  5,  5,  6,  6,  6,  6,  7,
      12. 7,  7,  8,  8,  8,  9,  9,  9, 10, 10, 10, 11, 11, 11, 12, 12,
      13. 13, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20,
      14. 20, 21, 21, 22, 22, 23, 24, 24, 25, 25, 26, 27, 27, 28, 29, 29,
      15. 30, 31, 31, 32, 33, 34, 34, 35, 36, 37, 38, 38, 39, 40, 41, 42,
      16. 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
      17. 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75,
      18. 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 92, 93, 94, 96,
      19. 97, 99,100,102,103,105,106,108,109,111,112,114,115,117,119,120,
      20. 122,124,125,127,129,130,132,134,136,137,139,141,143,145,146,148,
      21. 150,152,154,156,158,160,162,164,166,168,170,172,174,176,178,180,
      22. 182,184,186,188,191,193,195,197,199,202,204,206,209,211,213,215,
      23. 218,220,223,225,227,230,232,235,237,240,242,245,247,250,252,255
      24. Adafruit_NeoPixel strip = Adafruit_NeoPixel(36, PIN, NEO_GRB + NEO_KHZ800);
      25. //--------------------------------------------------|
      26. //Your NeoPixel rings may not line up with ours, or each other.     |
      27. //tequila sunrise color scheme
      28. uint32_t milli_color  = strip.Color ( 44,  21,  0); // redest orange
      29. uint32_t second_color = strip.Color (  44,  30, 0); //slightly yellower
      30. uint32_t hour_color   = strip.Color (  44, 42,  0); //yellow
      31. uint32_t minute_color = strip.Color ( 43, 0, 5); //red
      32. uint32_t off_color    = strip.Color (  0,  0,  0);
      33. uint32_t milli_color  = strip.Color ( 24,  0,  24); // magenta
      34. uint32_t hour_color   = strip.Color (  0, 10,  44); // royal blue
      35. const int offset = -4;  // Eastern Daylight Time (USA)
      36. if (GPS.fix) {
      37.       setTime(GPS.hour, GPS.minute, GPS.seconds, GPS.day, GPS.month, GPS.year);
      38.   currentsecond = outertopLED + map ((second() % 60), 0, 60, 0, 23);
      39. if (currentsecond > 24) {currentsecond = currentsecond-24;};
      40.   milli  = map ((millis() %  1000), 0,  1000, 0, 24);
      41.   currenthour   = innertopLED + map ((hour() % 12), 0,  12, 24, 35);
      42. if (currenthour > 35) { currenthour = currenthour-12;}
      43.   currentminute = outertopLED + map (minute() % 60, 0,  60, 0, 23);
      44. if (currentminute > 23) {currentminute = currentminute-24;};
      45. ClockSegments (Adafruit_NeoPixel&, ClockPositions&);
      46. void add_color (uint8_t position, uint32_t color);
      47. uint32_t blend (uint32_t color1, uint32_t color2);
      48. ClockSegments::ClockSegments (Adafruit_NeoPixel& n_strip, ClockPositions& n_positions): strip (n_strip), positions (n_positions)
      49. void ClockSegments::draw()
      50.   add_color (positions.currentminute,  minute_color);
      51.   add_color (positions.currenthour,  hour_color  );
      52.   add_color (positions.currentsecond     % 24, second_color);
      53.   add_color ((positions.currentsecond+1) % 24, second_color);
      54. void ClockSegments::add_color (uint8_t position, uint32_t color)
      55. uint32_t blended_color = blend (strip.getPixelColor (position), color);
      56. uint8_t r,b,g;
      57.   r = (uint8_t)(blended_color >> 16),
      58.   g = (uint8_t)(blended_color >>  8),
      59.   b = (uint8_t)(blended_color >>  0);
      60.   strip.setPixelColor (position, blended_color);
      61. uint32_t ClockSegments::blend (uint32_t color1, uint32_t color2)
      62. uint8_t r3,g3,b3;
      63.   r1 = (uint8_t)(color1 >> 16),
      64.   g1 = (uint8_t)(color1 >>  8),
      65.   b1 = (uint8_t)(color1 >>  0);
      66.   r2 = (uint8_t)(color2 >> 16),
      67.   g2 = (uint8_t)(color2 >>  8),
      68.   b2 = (uint8_t)(color2 >>  0);
      69. return strip.Color (constrain (r1+r2, 0, 255), constrain (g1+g2, 0, 255), constrain (b1+b2, 0, 255));
      70. for(uint16_t i=0; i<strip.numPixels (); i++) {
      71.       strip.setPixelColor (i, off_color);
      72. ClockSegments  segments(strip, positions);
      73. // connect at 115200 so we can read the GPS fast enough and echo without dropping chars
      74. Serial.println("Adafruit GPS library basic test!");
      75. // uncomment this line to turn on RMC (recommended minimum) and GGA (fix data) including altitude
      76. // For the parsing code to work nicely and have time to sort thru the data, and
      77. // print it out we don't suggest using anything higher than 1 Hz
      78.   strip.begin ();
      79.   strip.show (); // Initialize all pixels to 'off'
      80. uint32_t gpsTimer = millis();
      81. char c = GPS.read();
      82. if (GPSECHO)
      83. if (!GPS.parse(GPS.lastNMEA())) // this also sets the newNMEAreceived() flag to false
      84. return; // we can fail to parse a sentence in which case we should just wait for another
      85. // if millis() or timer wraps around, we'll just reset it
      86. if (gpsTimer > millis()) gpsTimer = millis();
      87.       setTime(GPS.hour, GPS.minute, GPS.seconds, GPS.day, GPS.month, GPS.year);
      88. Serial.print("\nTime: ");
      89. Serial.print(GPS.hour, DEC); Serial.print(':');
      90. Serial.print(GPS.minute, DEC); Serial.print(':');
      91. Serial.print(GPS.seconds, DEC); Serial.print('.');
      92. Serial.println(GPS.milliseconds);
      93. if ((millis() - gpsTimer > 60000)) {
      94.     gpsTimer = millis(); // reset the timer
      95. if (GPS.fix) {
      96.       setTime(GPS.hour, GPS.minute, GPS.seconds, GPS.day, GPS.month, GPS.year);
      97.       adjustTime(offset * SECS_PER_HOUR);
      98.   positions.update ();
      99.   segments.draw ();
      100. // Fill the dots one after the other with a color
      101. void colorWipe(uint32_t c, uint32_t wait) {
      102. for(uint16_t i=0; i<strip.numPixels(); i++) {
      103.       strip.setPixelColor(i, c);
      104.       strip.show();
      105.       delay(wait);
      106. // Slightly different, this makes the rainbow equally distributed throughout
      107. for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
      108. for(i=0; i< strip.numPixels(); i++) {
      109.       strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
      110. // Input a value 0 to 255 to get a color value.
      111. // The colours are a transition r - g - b - back to r.
      112. if(WheelPos < 85) {
      113. return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
      114. } else if(WheelPos < 170) {
      115. return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
      116. return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);

  * ![flora_neopixel-ring-clock-adafruit-25.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/174/medium640/flora_neopixel-ring-clock-adafruit-25.jpg?1392143714)

To set the time, make sure the GPS has a clear view of the sky, or attach a GPS antenna and stick it out the window.
![flora_neopixel-ring-clock-adafruit-desk-version.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/176/large1024/flora_neopixel-ring-clock-adafruit-desk-version.jpg?1392145043)

> _Use a piece of wire to make a stand for your desk, hang your clock on the wall, or attach a big 'ol gold chain and jam out like 21st century Flavor Flav._

![flora_neopixel-ring-clock-adafruit-necklace.jpg](https://cdn-learn.adafruit.com/assets/assets/000/014/177/large1024/flora_neopixel-ring-clock-adafruit-necklace.jpg?1392145357)
