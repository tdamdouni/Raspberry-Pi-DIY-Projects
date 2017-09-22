/*
 --- nebulus UnicornHat HD test ---

 to compile cut and paste the following in a terminal,
 changing the filename as necessary:

 gcc test-uhhd.c -o test-uhhd -l wiringPi

 http://forums.pimoroni.com/t/c-example-for-unicorn-hat-hd/5149/4
 */

#include <stdio.h>
#include <strings.h>
#include <wiringPiSPI.h>

#define SPI_CHANNEL 0
#define SPI_SPEED   9000000

#define PACKET_SIZE (1 + ( 16 * 16 * 3 ))

int main( int argc, char *argv[] )
{
  if( wiringPiSPISetup( SPI_CHANNEL, SPI_SPEED ) == -1 )
  {
    printf("Could not initialise SPI\n");
    return( 1 );
  }

  // buffer for pixel data and pixel we address on each loop
  unsigned char buffer[PACKET_SIZE];
  int pixel = 0;

  while( 1 )
  {
    // calculate the address in the buffer the pixel we are going to paint
    int index = 1 + (pixel*3);

    // setup the buffer
    buffer[0] = 0x72;   // SOF byte

    // colour one pixel purple -> yellow depending upon pixel index
    buffer[index] = 255;          // Red
    buffer[index+1] = pixel;      // Green
    buffer[index+2] = 255-pixel;  // Blue

    // send off the buffer
    wiringPiSPIDataRW( SPI_CHANNEL, buffer, PACKET_SIZE ) ;

    // sleep a bit
    usleep( (int)(1000000/120) );

    // move to the next pixel
    pixel++;
    if( pixel >= 256 ) pixel = 0;
  }
}
