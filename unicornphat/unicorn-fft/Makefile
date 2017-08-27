TARGET = unicorn-fft
LIBS = -lm -lws2811 -lfftw3
INCLUDES = -Iunicorn-hat/python/rpi-ws281x/lib
LFLAGS = -Lunicorn-hat/python/rpi-ws281x/lib
CC = gcc
CFLAGS = -g -Wall -O2
SOURCE = src

.PHONY: default all clean

default: $(TARGET)
all: lib default

OBJECTS = $(patsubst %.c, %.o, $(wildcard $(SOURCE)/*.c))
HEADERS = $(wildcard $(SOURCE)/*.h)

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

.PRECIOUS: $(TARGET) $(OBJECTS)

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) $(INCLUDES) -o $@ $(OBJECTS) $(LFLAGS) $(LIBS) 

lib:
	make -C unicorn-hat/python/rpi-ws281x/lib/ lib

clean:
	-rm -f $(SOURCE)/*.o
	-rm -f $(TARGET)
	make -C unicorn-hat/python/rpi-ws281x/lib/ clean
