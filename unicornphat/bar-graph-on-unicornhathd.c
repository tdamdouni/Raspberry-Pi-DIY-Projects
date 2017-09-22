//
// A simulated (random) bar graph displayed on the Unicorn Hat HD from
// pimoroni (https://shop.pimoroni.com/products/unicorn-hat-hd)
// http://forums.pimoroni.com/t/c-example-for-unicorn-hat-hd/5149/5
//

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <time.h>
#include <unistd.h>
#include <wiringPiSPI.h>

#define SPI_CHANNEL 0
#define SPI_SPEED   9000000

#define PACKET_SIZE (1 + ( 16 * 16 * 3 ))

unsigned char buffer[PACKET_SIZE];

// With the exception of red, green and blue the color names are
// best guesses I could come up with. I was shooting for a reasonable
// gradient where each color was discernable from the next.
int colors[16][3] = {
    {255,153,255},  // light-pink
    {255,102,255},  // pink
    {255,0,255},    // fuschia
    {153,0,255},    // violet
    {102,0,255},    // indigo
    {0,0,255},      // blue
    {0,102,255},    // cyan
    {0,153,255},    // baby-blue
    {0,255,255},    // teal
    {0,255,102},    // seafoam
    {0,255,0},      // green
    {153,255,0},    // pale-green
    {255,255,0},    // yellow
    {255,153,0},    // orange
    {255,102,0},    // red-orange
    {255,0,0}       // red
};

// It took me a little while to work out how to properly address each
// pixel. Once I had the the (x,y) to array index formula worked out
// I used the following python script to generate a table to confirm.
//
// print('| {0:>2s} | {1:>2s} | {2:>3s} | {3:>3s} | {4:>3s} |'.format(
//     'x', 'y', 'r', 'g', 'b'))
// print('=============================')
// for x in range(16):
//     for y in range(16):
//         r = 1 + ((y * 16) + x) * 3
//         g = r + 1
//         b = r + 2
//         print('| {0:2d} | {1:2d} | {2:3d} | {3:3d} | {4:3d} |'.format(
//
// | Coords  | Color Indices   |
// |  x |  y |   r |   g |   b |
// =============================
// |  0 |  0 |   1 |   2 |   3 |
// |  0 |  1 |  49 |  50 |  51 |
// |  0 |  2 |  97 |  98 |  99 |
// |  0 |  3 | 145 | 146 | 147 |
// |  0 |  4 | 193 | 194 | 195 |
// |  0 |  5 | 241 | 242 | 243 |
//            .
//            .
//            .
// | 15 | 10 | 526 | 527 | 528 |
// | 15 | 11 | 574 | 575 | 576 |
// | 15 | 12 | 622 | 623 | 624 |
// | 15 | 13 | 670 | 671 | 672 |
// | 15 | 14 | 718 | 719 | 720 |
// | 15 | 15 | 766 | 767 | 768 |
//
// All this the bottom of the matrix along the GPIO edge of the RPi.
// If you swap x and y in the offset equation it will rotate the display
// 90 degrees widdershins (counter-clockwise) so the bottm of the graph
// is now along the Micro SD card edge.
//
// print('| {0:7s} | {1:15s} |'.format('Coords', 'Color Indices'))
// print('| {0:>2s} | {1:>2s} | {2:>3s} | {3:>3s} | {4:>3s} |'.format(
//     'x', 'y', 'r', 'g', 'b'))
// print('=============================')
// for x in range(16):
//     for y in range(16):
//         r = 1 + ((x * 16) + y) * 3
//         g = r + 1
//         b = r + 2
//         print('| {0:2d} | {1:2d} | {2:3d} | {3:3d} | {4:3d} |'.format(
//             x, y, r, g, b))
// | Coords  | Color Indices   |
// |  x |  y |   r |   g |   b |
// =============================
// |  0 |  0 |   1 |   2 |   3 |
// |  0 |  1 |   4 |   5 |   6 |
// |  0 |  2 |   7 |   8 |   9 |
//              .
//              .
//              .
// | 15 | 13 | 760 | 761 | 762 |
// | 15 | 14 | 763 | 764 | 765 |
// | 15 | 15 | 766 | 767 | 768 |

void set_pixel(int x, int y, int r, int g, int b) {
    // Sets specified pixel with an RGB value.
    // Find the starting position in the array.
    int offset = 1 + ((y * 16) + x) * 3;
    buffer[offset + 0] = r;         // led red value
    buffer[offset + 1] = g;         // led green value
    buffer[offset + 2] = b;        // led blue value
}

int main( int argc, char *argv[] )
{
    srand(time(0));
    if( wiringPiSPISetup( SPI_CHANNEL, SPI_SPEED ) == -1 )
    {
        printf("Could not initialise SPI\n");
        return( 1 );
    }
    // setup the buffer and set the Start of Frame byte.
    buffer[0] = 0x72; // SOF byte

    // Set buffer to zero so we start out with a blank matrix.
    for (size_t i = 1; i < 770; i++) {
        buffer[i] = 0;
    }

    // What follows just iterates over each column of LEDs (x) and
    // then picks a row height (y) for that column. Each x,y value is
    // then set to the appropriate color.
    while (1) {
        for (size_t x = 0; x < 16; x++) {
            buffer[0] = 0x72; // SOF byte
            int y_height = rand() / (RAND_MAX / 15) + 1;
            for (size_t y = 0; y < y_height; y++) {
                set_pixel(x, y, colors[x][0], colors[x][1], colors[x][2]);
            }
        }
        // Write the buffer to the Unicorn Hat HD via SPI.
        wiringPiSPIDataRW( SPI_CHANNEL, buffer, PACKET_SIZE );
        // Based on experimentation without sleeping updates to the
        // Unicorn Hat HD seem to happen too often for it to display
        // anything.
        usleep( (int)(1000) );
    }
}
