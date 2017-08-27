#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <memory.h>
#include <stdbool.h>
#include <time.h>
#include <ctype.h>

#include "pump.h"

#define TEMPSENSOR1 "/sys/bus/w1/devices/28-000005272154/w1_slave"
#define BUFFSIZE 76
#define CSIZE 1
#define NUMBERTEMPSTRCHARS 75

/**
**/

void get_time ()
{
  time_t rawtime;
  struct tm * timeinfo;

  time ( &rawtime );
  timeinfo = localtime (&rawtime);
  printf ( "Current time: %s", asctime (timeinfo) );
}

void print_buffer(char *buff,size_t maxlen) {
    char c;    
    size_t index = 0;
    do {
         c = buff[index++];
         printf("%c(%02X) ",(isprint(c)?c:'?'),c);
    }
    while(c != EOF && index < maxlen);
}

size_t get_reading(char buff[],size_t maxlen,char * device) {
    size_t result = 0;
    FILE *logger = getLogFile();
    fprintf(logger,"Read temp from %s\n",device);
    FILE *tfile = fopen(device,"r");
    if (NULL == tfile) {
        fprintf(stderr,"Unable to access temperature sensor: Check GPIO available\n");
        fprintf(stderr,"or try sudo 4755 gettemp\n");
        fprintf(stderr,"or try sudo modprobe w1-gpio\n");
        fprintf(stderr,"or try sudo modprobe w1-therm\n");
    } else {
        result = fread(buff, CSIZE, maxlen, tfile);
        fclose(tfile);
    }
    fprintf(logger,"Read %d bytes\n",result);
    return result;
}

bool parse_reading(char buff[],size_t maxlen, double* result) {
    bool valid = 0.0;
    size_t index = 0;
    bool found = false;
    // should be index+1 but use index+2 to protect the atof call below
    while ((index+2) < maxlen && !found) {
        found = (buff[index] == 't') && (buff[index+1] == '=');
        index++;
    }
    if (found) {
        index++;
        long int val = atol(&buff[index]);
        //printf("Long value = %ld,\nString value = %s", val, &buff[index]);        
        *result = (double)val/1000;
        valid = true;
    }
    // printf ( "Current temperature: %3.2fdegC\n", result );
    return result;
}

void testTemp(void) {
    double temp;
    char buff[BUFFSIZE];
    int index=0;
    size_t numbytes;
    bool valid_temp;
    FILE *logger = getLogFile();
    initLed();
    memset(buff,0,sizeof(buff));
    for(index=0; index < 1; index++) {
        led_on(GPIO_PIN_LED);
        numbytes = get_reading(buff,BUFFSIZE,TEMPSENSOR1);
        if (0 < numbytes) {
            valid_temp = parse_reading(buff,BUFFSIZE,&temp);
            fprintf(logger,"valid_temp=%c temp=%3.2fdegC\n",(valid_temp?'T':'F'),temp);
            // print_buffer(&buff[0],numbytes);
        }
        led_off(GPIO_PIN_LED);
    }
} 

