/***************************************************
  Adafruit MQTT Library ESP8266 Example

  Must use ESP8266 Arduino from:
    https://github.com/esp8266/Arduino

  Works great with Adafruit's Huzzah ESP board:
  ----> https://www.adafruit.com/product/2471

  Adafruit invests time and resources providing this open source code,
  please support Adafruit and open-source hardware by purchasing
  products from Adafruit!

  Written by Tony DiCola for Adafruit Industries.
  MIT license, all text above must be included in any redistribution
 ****************************************************/
#include <ESP8266WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include "Adafruit_NeoPixel.h"
#include "config.h"

/************ Global State (you don't need to change this!) ******************/

// Create an ESP8266 WiFiClient class to connect to the MQTT server.
WiFiClient client;

// Setup the MQTT client class by passing in the WiFi client and MQTT server and login details.
Adafruit_MQTT_Client mqtt(&client, MQTT_SERVER, MQTT_SERVERPORT, MQTT_USERNAME, MQTT_USERNAME, MQTT_KEY);

/****************************** Feeds ***************************************/

Adafruit_MQTT_Subscribe daniel = Adafruit_MQTT_Subscribe(&mqtt, "clantastic/daniel");
Adafruit_MQTT_Subscribe jessica = Adafruit_MQTT_Subscribe(&mqtt, "clantastic/jessica");
Adafruit_MQTT_Subscribe emily = Adafruit_MQTT_Subscribe(&mqtt, "clantastic/emily");

/****************************** LEDs ****************************************/

int red = 255;
int green = 255;
int blue = 255;
char hex[8] = {0};

#define PIXELS_PIN 15
#define NUM_LEDS 8
#define BRIGHTNESS 50

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIXELS_PIN, NEO_GRB + NEO_KHZ800);

/*************************** Sketch Code ************************************/

void redcallback(double x) {
  Serial.print("Red value is: ");
  Serial.println((int)x);
  red = (int)x;
}

void greencallback(double x) {
  Serial.print("Green value is: ");
  Serial.println((int)x);
  green = (int)x;
}

void bluecallback(double x) {
  Serial.print("Blue value is: ");
  Serial.println((int)x);
  blue = (int)x;
}

void setup() {
  Serial.begin(115200);
  delay(10);

  strip.setBrightness(BRIGHTNESS);
  strip.begin();
  updateLEDs();
 
  // Connect to WiFi access point.
  Serial.println(); Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);

  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.println("WiFi connected");
  Serial.println("IP address: "); Serial.println(WiFi.localIP());

  daniel.setCallback(greencallback);
  jessica.setCallback(bluecallback);
  emily.setCallback(redcallback);
  
  mqtt.subscribe(&daniel);
  mqtt.subscribe(&jessica);
  mqtt.subscribe(&emily);
}

uint32_t x=0;

void loop() {
  // Ensure the connection to the MQTT server is alive (this will make the first
  // connection and automatically reconnect when disconnected).  See the MQTT_connect
  // function definition further below.
  MQTT_connect();

  // this is our 'wait for incoming subscription packets and callback em' busy subloop
  // try to spend your time here:
  mqtt.processPackets(10000);

  updateLEDs();
  
  // ping the server to keep the mqtt connection alive
  // NOT required if you are publishing once every KEEPALIVE seconds
  if(! mqtt.ping()) {
    mqtt.disconnect();
  }
}

void updateLEDs() {
  sprintf(hex,"#%02X%02X%02X",red,green,blue);

  Serial.print("Setting LED strip to: ");
  Serial.println(hex);

  for(int i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, strip.Color(red,green,blue));
  }
  strip.show();
}

// Function to connect and reconnect as necessary to the MQTT server.
// Should be called in the loop function and it will take care if connecting.
void MQTT_connect() {
  int8_t ret;

  // Stop if already connected.
  if (mqtt.connected()) {
    return;
  }

  Serial.print("Connecting to MQTT... ");

  uint8_t retries = 3;
  while ((ret = mqtt.connect()) != 0) { // connect will return 0 for connected
       Serial.println(mqtt.connectErrorString(ret));
       Serial.println("Retrying MQTT connection in 10 seconds...");
       mqtt.disconnect();
       delay(10000);  // wait 10 seconds
       retries--;
       if (retries == 0) {
         // basically die and wait for WDT to reset me
         while (1);
       }
  }
  Serial.println("MQTT Connected!");
}
