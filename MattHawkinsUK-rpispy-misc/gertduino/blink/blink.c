/*
* blink.c
*
* Created: 23/09/2013 21:04:02
* Author: G.J. van Loo
* Simple example program to 'walk' the LEDs
*/

#include <avr/io.h>
#define DELAY 250
#define F_CPU 16000000

// Some macros that make the code more readable
#define output_low(port,pin) port &= ~(1<<pin)
#define output_high(port,pin) port |= (1<<pin)
#define set_input(portdir,pin) portdir &= ~(1<<pin)
#define set_output(portdir,pin) portdir |= (1<<pin)

// Outputs are:
// LED0 = PB5
// LED1 = PB1
// LED2 = PB2
// LED3 = PD3
// LED4 = PD5
// LED5 = PD6

void delay_ms(unsigned int ms)
{
  uint16_t delay_count = F_CPU / 17500;
  volatile uint16_t i;
  
  while (ms != 0) {
    for (i=0; i != delay_count; i++);
    ms--;
  }
} // delay_ms

void delay()
{ long d;
  unsigned char oldb,oldd;
  for (d=0; d<DELAY; d++)
  {
    delay_ms(1);
    if ((PINC & 0b00001000)==0)
    {
      oldb = PORTB; 
      20 | Page
      oldd = PORTD;
      PORTB = 0xFF;
      PORTD = 0xFF;
      delay_ms(1);
      PORTB = oldb;
      PORTD = oldd;
      d--;
    }
    else
    { if ((PINC & 0b00000100)==0)
        d--;
      else
        delay_ms(1);
    } // if button pressed
  } // if button pressed
} // delay

int main(void)
{ // int b;
    // Set all LED connections to output
  DDRB = 0b00100110;
  DDRD = 0b01101000;
  PORTB = 0x00;
  PORTD = 0x00;
  // Set button (port C) to input
  DDRC = 0b00000000;
  // pull-up on C2 & C3:
  PORTC = 0b00001100;
  while(1)
  { // convoluted but simple walk the leds
    output_high(PORTB,5);
    delay();
    output_low (PORTB,5);
    output_high(PORTB,1);
    delay();
    output_low (PORTB,1);
    output_high(PORTB,2);
    delay();
    output_low (PORTB,2);
    output_high(PORTD,3);
    delay();
    output_low (PORTD,3);
    output_high(PORTD,5);
    delay();
    output_low (PORTD,5);
    output_high(PORTD,6);
    delay();
    output_low (PORTD,6);
    output_high(PORTD,5);
    delay();
    output_low (PORTD,5);
    output_high(PORTD,3);
    delay();
    output_low (PORTD,3);
    output_high(PORTB,2); 
    21 | Page
    delay();
    output_low (PORTB,2);
    output_high(PORTB,1);
    delay();
    output_low (PORTB,1);
  } // forever
} // main