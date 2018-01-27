// https://gist.github.com/emoryy/2a614458b556969b5e8a1a824468518c
// https://forums.pimoroni.com/t/arduino-and-blinkt/5444/7

#include <Adafruit_DotStar.h>
#include <SPI.h>
#define NUMPIXELS 8 // Number of LEDs in strip

// Here's how to control the LEDs from any two pins:
#define DATAPIN    4
#define CLOCKPIN   5

Adafruit_DotStar strip = Adafruit_DotStar(NUMPIXELS, DATAPIN, CLOCKPIN, DOTSTAR_BGR);

String inputString = "";         // a String to hold incoming data
boolean stringComplete = false;  // whether the string is complete

int mode = 2;

uint8_t clearedX = 0;

// pong
int head0 = 0;
uint32_t color = 0xFF0000;      // 'On' color (starts red)
bool dir0 = true;

// rainbow
const double spacing = 360.0 / 16.0;
int hue = 0;
int t = 0;

void setup() {

#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000L)
  clock_prescale_set(clock_div_1); // Enable 16 MHz on Trinket
#endif

  strip.begin(); // Initialize pins for output
  
  strip.setBrightness(20);
  strip.show();  // Turn all LEDs off ASAP

  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  
}
/*
void getPixelColorRGB(uint32_t &r, uint32_t &g, uint32_t &b, uint16_t n) const {
  uint8_t *pixels = strip.getPixels();
  if (n >= 8) return 0;
  uint8_t *p = &pixels[n * 3];
  r = (uint32_t)p[rOffset] << 16);
  g = (uint32_t)p[gOffset] <<  8);
  b = (uint32_t)p[bOffset];
}
*/
void HSVtoRGB(double& r, double& g, double& b, double h, double s, double v) {
  if (s == 0.0) {
    r = v;
    g = v;
    b = v;
  }
  int i = int(h * 6.0); // XXX assume int() truncates!
  double f = (h * 6.0) - i;
  double p = v * (1.0 - s);
  double q = v * (1.0 - s * f);
  double t = v * (1.0 - s * (1.0 - f));
  i = i % 6;
  if (i == 0) {
    r = v; g = t; b = p; return; // v, t, p  
  }
  if (i == 1) {
    r = q; g = v; b = p; return; // q, v, p
  }
  if (i == 2) {
    r = p; g = v; b = t; return; // p, v, t
  }
  if (i == 3) {
    r = p; g = q; b = v; return; // p, q, v
  }
  if (i == 4) {
    r = t; g = p; b = v; return; // t, p, v
  }
  if (i == 5) {
    r = v; g = p; b = q; return; // v, p, q
  }
}

void loop() {
  
  if (stringComplete) {
    Serial.println(inputString);
    if (inputString.startsWith("m-")) {
      mode = inputString.substring(2).toInt();
      if (mode > 0) {
        clearedX = 0;
      }
      Serial.println(inputString.substring(5));
    }
    
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
  
  if (mode == 1) {
    strip.clear();
    strip.setPixelColor(head0, 0xFF0000);
    strip.show();                     // Refresh strip
    if (dir0) {
      head0++;
      if (head0 == 8) {
        head0 = 6;
        dir0 = !dir0;
      }  
    } else {
      head0--;
      if (head0 < 0) {
        head0 = 1;
        dir0 = !dir0;
      }
    }
    
    delay(50);
  } else if (mode == 2) {
    hue = t;
    for (int x = 0; x < 8; x++) {
      double offset = x * spacing;
      double h = (int(hue + offset) % 360) / 360.0 ;
      double r, g, b;
      HSVtoRGB(r, g, b, h, 1.0, 1.0);
      strip.setPixelColor(x, int(255.0 * r), int(255.0 * g), int(255.0 * b));
    }
    strip.show();
    t++;
    if (t > 359) {
      t = 0;
    }
    delay(10);
  } else if (mode == 0) {
    if (clearedX != 255) {
      for (int x = 0; x < 8; x++) {
        if (!(clearedX & (1 << x))) {
          uint32_t colorx = strip.getPixelColor(x);
          uint8_t r = colorx >> 16;
          uint8_t g = colorx >> 8 & 0xFF;
          uint8_t b = colorx & 0xFF;
        //Serial.println(colorx, HEX);
        //Serial.println(r, DEC);
        //Serial.println(g, DEC);
        //Serial.println(b, DEC);
          strip.setPixelColor(
            x,
            r > 0 ? r - 1 : 0,
            g > 0 ? g - 1 : 0,
            b > 0 ? b - 1 : 0
          );
          if (r == 0 && g == 0 && b == 0) {
            clearedX |= 1 << x;
          }
        }
      }
      strip.show();
      delay(5);
    } else {
      // idle
      delay(1000);  
    }
  } else {
    delay(100);
  
  }

}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}