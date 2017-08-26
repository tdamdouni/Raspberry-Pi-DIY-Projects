#include "pump.h"

#define LOGGING "/tmp/gettemp.log"


FILE* getLogFile()
{ static FILE* myLogFile = NULL;
  if(myLogFile == NULL)
  { 
    myLogFile = fopen(LOGGING,"w");
    if(myLogFile == NULL) 
    {          // failure to open
      fprintf(stderr,"Unable to open logfile\n");
    }
  }
  return myLogFile;
}

