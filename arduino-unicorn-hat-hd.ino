#include <SPI.h>

const int slaveSelectPin = D8;
  
uint8_t buffer[16][16][3] = { 0 };
unsigned long step = 0;

//------------------demos------------------------

void gradient(uint8_t x, uint8_t  y, unsigned long  step) {
  uint8_t g = x * 16;
  uint8_t b = y * 16;
  uint8_t r = 255 - (x * 16);  
  setPixelU(x, y, r, g, b);
}

void run(uint8_t x, uint8_t  y, unsigned long  step) {
  uint8_t g = x * 16;
  uint8_t b = y * 16;
  uint8_t r = 255 - (x * 16);
  uint8_t v = step / 16 % 16 == y && step % 16 == x ? 1 : 0;  
  setPixelU(x, y, r * v, g * v, b * v);
}

void swirl(uint8_t x, uint8_t y, unsigned long step) {
  float fx = x - 7.5;
  float fy = y - 7.5;
  float dist = sqrt(fx * fx + fy * fy) * 0.5;
  //float dist = (fx + fy) * 0.5;
  //float dist = 5;
  float angle = (step * 0.1) + (dist * 1.5);
  float s = sin(angle);
  float c = cos(angle);
  float xs = x * c - y * s;
  float ys = x * s + y * c;
  float r = abs(xs + ys) * 12.0 - 20;
  float g = r + (s * 130);
  float b = r + (c * 130);
  setPixel(x, y,
    r,
    g,
    b
  );
}

void rainbowSearch(uint8_t x, uint8_t y, unsigned long step) {
  float xs = sin((step) * 0.01) * 20.0;
  float ys = cos((step) * 0.01) * 20.0;
  float scale = ((sin(step / 60.0) + 1.0) * 0.2) + 0.2;
  float r = sin((x + xs) * scale) + cos((y + xs) * scale);
  float g = sin((x + xs) * scale) + cos((y + ys) * scale);
  float b = sin((x + ys) * scale) + cos((y + ys) * scale);
  setPixel(x, y,
    r * 255,
    g * 255,
    b * 255
  );
}

void checker(uint8_t _x, uint8_t _y, unsigned long step) {
  
  float x = _x - 8;
  float y = _y - 8;
  float angle = step / 5.0;
  float s = sin(angle);
  float c = cos(angle);
  float xs = x * c - y * s;
  float ys = x * s + y * c;
  xs -= sin(step / 200.0) * 40.0;
  ys -= cos(step / 200.0) * 40.0;
  float scale = step % 20;
  scale /= 20.0;
  scale = (sin(step / 50.0) / 8.0) + 0.25;
  xs *= scale;
  ys *= scale;
  float xo = abs(xs) - int(abs(xs));
  float yo = abs(ys) - int(abs(ys));
  //  l = 0 if @ else 1 if xo > .1 and  else .5
  float l = int(floor(xs) + floor(ys)) % 2 ? 0 : (xo > 0.1 && yo > .1 ? 1 : 0.5);
  float r, g, b;
  HSVtoRGB(r, g, b, (step % 255) / 255.0, 1, 1);
  setPixel(_x, _y,
    r * (l * 255),
    g * (l * 255),
    b * (l * 255)
  );
}

void (*demoFuncs[])(uint8_t x, uint8_t  y, unsigned long step) = {
  run,
  gradient,
  swirl,
  rainbowSearch,
  checker
};

//-----------------------------------------------

void setPixelU(uint8_t x, uint8_t y, uint8_t r, uint8_t g, uint8_t b) {
  buffer[y][x][0] = r;
  buffer[y][x][1] = g;
  buffer[y][x][2] = b;
}

void setPixel(uint8_t x, uint8_t y, float r, float g, float b) {
  buffer[y][x][0] = uint8_t(max(0, min(255, r)));
  buffer[y][x][1] = uint8_t(max(0, min(255, g)));
  buffer[y][x][2] = uint8_t(max(0, min(255, b)));
}

void sendBuffer() {
  SPI.beginTransaction(SPISettings(9000000, MSBFIRST, SPI_MODE0));
  digitalWrite(slaveSelectPin, LOW);
  SPI.transfer(0x72); 
  for (int x = 0; x < 16; x++) {
    for (int y = 0; y < 16; y++) {
      for (int c = 0; c < 3; c++) {
        SPI.transfer(buffer[x][y][c]);  
      }
    }
  }
  digitalWrite(slaveSelectPin, HIGH);
  SPI.endTransaction();
}

void HSVtoRGB(float& r, float& g, float& b, float h, float s, float v) {
  if (s == 0.0) {
    r = v;
    g = v;
    b = v;
  }
  int i = int(h * 6.0); // XXX assume int() truncates!
  float f = (h * 6.0) - i;
  float p = v * (1.0 - s);
  float q = v * (1.0 - s * f);
  float t = v * (1.0 - s * (1.0 - f));
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


void setup() {
  Serial.begin(9600);
  pinMode(slaveSelectPin, OUTPUT);
  SPI.begin();
  
}
void (*curFunc)(uint8_t x, uint8_t  y, unsigned long step) = demoFuncs[0];

unsigned long now = 0;
unsigned long diff = 0;
void loop() {
  now = millis();
  uint8_t i = (now / 5000) % 5;
  curFunc = demoFuncs[i];
  for (uint8_t x = 0; x < 16; x++) {
    for (uint8_t y = 0; y < 16; y++) {
      curFunc(x, y, step);  
    }
  }
  diff = millis() - now;
  //Serial.println(diff);
  sendBuffer();
  step++;
  if (diff < 8) {
    delay(8 - diff);
  }
}

