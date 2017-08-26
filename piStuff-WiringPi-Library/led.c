#include <sys/types.h>
#include <unistd.h>
#include <assert.h>

#include "pump.h"
#include "wiringPi.h"

#define LOGGING "/tmp/gettemp.log"


/**
**/

static bool wiringPiActive = false;
void wiringPiInit(void) {
    if (!wiringPiActive) {
        wiringPiSetup();
        wiringPiActive = true;
    }
}

void led_on(int pin) {
    bool result = false;
    assert(wiringPiActive == true);
    digitalWrite(pin,HIGH);
}

void led_off(int pin) {
    bool result = false;
    assert(wiringPiActive == true);
    digitalWrite(pin,LOW);
}

void gpio_pin_mode(int pin, int mode) {
    assert(wiringPiActive == true);
    pinMode(pin,mode);
}

void initLed() {
    wiringPiInit();
    pinMode(GPIO_PIN_LED,OUTPUT);
}

void testLed() {
    pinMode(GPIO_PIN_LED,OUTPUT);
    digitalWrite(GPIO_PIN_LED,HIGH);
    sleep(2);
    digitalWrite(GPIO_PIN_LED,LOW);    
}
