#include <stdio.h>
#include <time.h>

#include "pump.h"

/**
#include <memory.h>
**/
int main(int argc, char *argv[]) {
    int result = SUCCESS;
    int step = 0;
    const int lastStep = 4;
    
    FILE *logger = getLogFile();
    for (step = 0; lastStep >= step && SUCCESS == result; step++) {
        switch (step) {
        case 0: 
            if (NULL==logger)
                result = BADLOGFILE; 
            break;
        case 1:
            get_time(); 
            break;
        case 2:
            testTemp();
            break;
        case 3:
            testLed();
            break;
        case 4:
            get_time();
            break;
        }
    }
    fclose(logger);
    return result;
}
