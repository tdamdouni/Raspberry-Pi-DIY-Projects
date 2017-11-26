/**
 * On a Raspberry Pi 2 compile with:
 *
 * g++ -Ofast -mfpu=vfp -mfloat-abi=hard -march=armv7-a -mtune=arm1176jzf-s -I/usr/local/include -L/usr/local/lib -lrf24-bcm PL1167_nRF24.cpp MiLightRadio.cpp send_cmd.cpp -o send_cmd
 *
 * sudo ./send_cmd "B0 F2 EA 6D B0 02 f0"
 */

#include <cstdlib>
#include <iostream>
#include <string.h>

using namespace std;

#include <RF24/RF24.h>

#include "PL1167_nRF24.h"
#include "MiLightRadio.h"

RF24 radio(RPI_V2_GPIO_P1_22, RPI_V2_GPIO_P1_24, BCM2835_SPI_SPEED_1MHZ);

PL1167_nRF24 prf(radio);
MiLightRadio mlr(prf);


static int dupesPrinted = 0;
static bool receiving = false;
static bool escaped = false;
static uint8_t outgoingPacket[7];
static uint8_t outgoingPacketPos = 0;

static uint8_t nibble;

static enum {
  IDLE,
  HAVE_NIBBLE,
  COMPLETE,
} state;

void send(const char* message)
{
  memset(outgoingPacket, 0, 7);

  // convert input into bytes
  int index = 0;
  for (int counter = 0; *message; ++message) {
    int n = 0;
    if (*message >= 'a' && *message <= 'f') {
      n = *message - 'a' + 10;
    } else if (*message >= 'A' && *message <= 'F') {
      n = *message - 'A' + 10;
    } else if (*message >= '0' && *message <= '9') {
      n = *message - '0';
    } else if (*message == ' ') {
      index++;
    } else {
      cout << "cannot decode" << endl;
      exit(1);
    }
    outgoingPacket[index] = outgoingPacket[index] * 16 + (unsigned long) n;
 
    // printf("sending packet\n");
    // for (int i = 0; i < 7; i++) {
    //   printf("%02X ", outgoingPacket[i]);
    // }
    // printf("\n");

    mlr.write(outgoingPacket, sizeof(outgoingPacket));
    delay(10);
    mlr.resend();
    delay(10);
    outgoingPacket[6] += 8;
  }
}

main(int argc, char** arguments)
{
  if (argc < 2) {
		cout << "usage: sudo ./send_cmd \"B0 F2 EA 6D B0 02 f0\"";
		exit(1);
  }
  mlr.begin();

  char* message = 0;
  message = arguments[1];
  // printf("sending: %s\n", message);
  send(message);
  return 0;
}
