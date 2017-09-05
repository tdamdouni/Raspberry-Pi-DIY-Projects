// Multi Channel Music Streamer
// Matt Gorr
// 6/28/2017
// Based on examples from http://learn.adafruit.com/adabox004

#include <SD.h>
#include <SPI.h>
#include <ESP8266WiFi.h>
#include <Adafruit_VS1053.h>

#define VS1053_RESET   -1     // VS1053 reset pin (not used!)
#define VS1053_CS      16     // VS1053 chip select pin (output)
#define VS1053_DCS     15     // VS1053 Data/command select pin (output)
#define VS1053_DREQ     0     // VS1053 Data request, ideally an Interrupt pin

#define VOLUME_KNOB    A0
#define CHANNEL_SWITCH  4
#define NUM_MODES 3

int mode = 1;
const char* credentialsFileName = "CREDITS.TXT";
Adafruit_VS1053 musicPlayer =  Adafruit_VS1053(VS1053_RESET, VS1053_CS, VS1053_DCS, VS1053_DREQ);
int lastvol = 30;
const int chipSelect = 2;
char bfr[80];
unsigned int channel;
uint8_t mp3buff[32];   // vs1053 likes 32 bytes at a time
int loopcounter = 0;
boolean playing = false;
WiFiClient client;
char* channelFile = "URLS.TXT";

void setup() {
  Serial.begin(115200);
  Serial.println("\n\nAdafruit VS1053 Feather WiFi Radio");

  if (! musicPlayer.begin()) { // initialise the music player
    Serial.println(F("Couldn't find VS1053, do you have the right pins defined?"));
    while (1) delay(10);
  }

  Serial.println(F("VS1053 found"));
  //musicPlayer.sineTest(0x44, 500);    // Make a tone to indicate VS1053 is working

  musicPlayer.setVolume(lastvol, lastvol);

  pinMode(CHANNEL_SWITCH, INPUT_PULLUP);
  if (initializeSDCard()) {
    if (connectToNetwork()) {
      getSavedChannel();
      if (setStation()) {
        playing = true;
      }
    }
  }
}

void loop() {
  //Serial.print("Looping"); Serial.println(loopcounter);
  checkButton();
  if (!playing || !(boolean)mode) {
    //Serial.println("NotLooping");
    return;
  }
  streamMusic();
}

void streamMusic() {
  loopcounter++;
  if (musicPlayer.readyForData()) {
    if (client.available() > 0) {
      uint8_t bytesread = client.read(mp3buff, 32);
      musicPlayer.playData(mp3buff, bytesread);
    }
  } else {
    if (loopcounter >= 1000) {
      loopcounter = 0;
      checkVolumeKnob();
    }
  }
}

boolean initializeSDCard() {
  Serial.print("Initializing SD card...");
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    return false;
  }
  Serial.println("card initialized.");
  return true;
}

boolean connectToNetwork() {
  File dataFile = SD.open(credentialsFileName);
  if (dataFile) {
    while (dataFile.available()) {
      dataFile.readStringUntil('\n').toCharArray(bfr, 80);
      char* ssid = strtok(&bfr[0], ",");
      char* key = strtok(NULL, "\n");

      Serial.print("Connecting to SSID "); Serial.println(ssid);
      WiFi.begin(ssid, key);
      long startMillis = millis();
      while (WiFi.status() != WL_CONNECTED && millis() < startMillis + 10000) {
        delay(500);
        Serial.print(".");
      }
      if (WiFi.status() != WL_CONNECTED) {
        Serial.println("Connection Failed :(");
        continue;
      }
      Serial.println("WiFi connected");
      Serial.println("IP address: ");
      Serial.println(WiFi.localIP());
      dataFile.close();
      return true;
    }
    dataFile.close();
    return false;
  } else {
    Serial.println("error opening file");
    return false;
  }
}
void getSavedChannel() {
  File dataFile = SD.open("LASTCHAN");
  if (dataFile) {
    channel = dataFile.parseInt();
    Serial.print("channel:");
    Serial.println(channel);
    dataFile.close();
  }
  dataFile.close();
}

boolean setStation() {
  char* host = strtok(getChannelString(), ":");
  char* portStr = strtok(NULL, "/");
  char* path = strtok(NULL, "");
  int port = atoi(portStr);

  //Serial.print(host); Serial.print(":"); Serial.print(port); Serial.print("/"); Serial.println(path);

  Serial.print("connecting to ");  Serial.println(host);
  if (!client.connect(host, port)) {
    Serial.println("Connection failed");
    return false;
  }
  Serial.print("Requesting URL: ");
  Serial.println(path);
  if (path == NULL) path = " ";
  client.print(String("GET /") + path + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" +
               "Connection: close\r\n\r\n");
  SD.remove("lastChan");
  File myFile = SD.open("lastChan", FILE_WRITE);
  if (myFile) myFile.println(channel);
  myFile.close();
  return true;
}

void changeMode() {
  mode = (mode + 1) % NUM_MODES;
  //musicPlayer.sineTest(0x44, 250);
  switch (mode) {
    case 0:   //  Turn Off
      Serial.println("Off");
      break;
    case 1:   //  Low Volume
      setStation();
      lastvol = 30;
      musicPlayer.setVolume(lastvol, lastvol);
      Serial.println("Low");
      break;
    case 2:   //  High Volume
      lastvol = 0;
      musicPlayer.setVolume(lastvol, lastvol);
      Serial.println("High");
      break;
  }
  delay(500);
}

void checkButton() {
  if (!digitalRead(CHANNEL_SWITCH)) {
    delay(20);
    long delta;
    long startMillis = millis();
    while (!digitalRead(CHANNEL_SWITCH)) {
      //if ((playing && (boolean)mode)) streamMusic();
      delay(20);
      delta = millis() - startMillis;
      /*if (delta>1000) {
        changeMode();
        return;
      }*/
    }
    if ((playing && (boolean)mode)) {
      if (delta < 100) {
        ; //  Do nothing
      } else if (delta < 1000) {
        delay(250);
        channel++;
        setStation();
        //Serial.println("Channel Changed");
      }
    }
  }
}

char * getChannelString() {
  if (channel >= getNumChannels()) {
    channel = 0;
  }
  File dataFile = SD.open(channelFile);
  if (dataFile) {
    uint8_t currentChannel = 0;
    while (dataFile.available() && currentChannel < channel + 1) {
      dataFile.readStringUntil('\n').toCharArray(bfr, 80);
      currentChannel++;
    }
    dataFile.close();
    return &bfr[0];
  } else {
    Serial.println("error opening file");
    return NULL;
  }
}

uint8_t getNumChannels() {
  uint8_t numChannels = 0;
  File dataFile = SD.open(channelFile);
  if (dataFile) {
    while (dataFile.available()) {
      if (dataFile.read() == '\n') {
        numChannels++;
      }
    }
  }
  dataFile.close();
  return numChannels;
}

void checkVolumeKnob() {
  int vol = 0;
  vol = analogRead(VOLUME_KNOB);
  vol /= 10;
  if (abs(vol - lastvol) > 3) {
    Serial.println(vol);
    lastvol = vol;
    musicPlayer.setVolume(lastvol, lastvol);
  }
}

