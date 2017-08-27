#include <stdio.h>
#include <stddef.h>
#include <stdbool.h>

#define SUCCESS 0
#define BADLOGFILE 1
#define BADTEMPREADING 2

#define GPIO_PIN_LED 1

FILE *getLogFile(void);
void get_time (void);
void testTemp(void);
void initLed(void);
void testLed(void);
void led_on(int);
void led_off(int);
static bool wiringPiActive;
