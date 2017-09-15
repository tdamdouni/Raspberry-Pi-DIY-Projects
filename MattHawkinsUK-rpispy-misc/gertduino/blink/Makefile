	# Makefile:
	#  Make the GertDuino m328p firmware.
	# 
	# Copyright (c) 2013 Gordon Henderson <projects@drogon.net>
	#################################################################################
	# This file is part of gertduino-m328:
	# Software to run on the Atmega328p processor on the Gerduino board
	# Can be used for the Atmega328p processor on the GERTBOARD as well
	# This is free software: you can redistribute it and/or modify
	# it under the terms of the GNU General Public License as published by
	# the Free Software Foundation, either version 3 of the License, or
	# (at your option) any later version.
	# 
	# This is distributed in the hope that it will be useful,
	# but WITHOUT ANY WARRANTY; without even the implied warranty of
	# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
	# GNU General Public License for more details.
	# 
	# You should have received a copy of the GNU General Public License
	#   along with this. If not, see <http://www.gnu.org/licenses/>.
	#################################################################################
	TARGET=blink
	MCU=atmega328p
	FREWQ=16000000
	
	# Debug
	#DEBUG  = -gstabs
	
	# C flags
	CC=avr-gcc
	#CFLAGS = $(DEBUG) -O3 -Wall -std=gnu99 -mmcu=$(MCU) -DF_CPU=$(FREWQ) $(INCLUDE)
	CFLAGS=$(DEBUG) -O2 -mcall-prologues -Wall -std=gnu99 -mmcu=$(MCU) -DF_CPU=$(FREWQ) $(INCLUDE)

	LD  = avr-gcc
	#LDFLAGS2=-Wl,-uvfprintf -lprintf_flt
	LDFLAGS = -mmcu=$(MCU) $(DEBUG) $(LIBLOC) $(LDFLAGS2)
	#LIBS  = -ldross -lm
	SRC=$(TARGET).c
	OBJ=$(SRC:.c=.o)
	
	all:	$(TARGET).hex
	
	$(TARGET).hex: $(TARGET).elf
		@echo [hex] $< 
		@avr-objcopy -j .text -j .data -O ihex $(TARGET).elf $(TARGET).hex
	
	$(TARGET).elf:  $(OBJ) 
		@echo [Link] $<
		@$(LD) -o $@ $(OBJ) $(LDFLAGS) $(LIBS)
		@avr-size $(TARGET).elf
	
	# Generate .lst file rule
	%.lst : %.o
		@echo [lst] $<
		@avr-objdump -h -S $<> $@
	
	.c.o:
		@echo [CC] $<
		@$(CC) -c $(CFLAGS) $< -o $@

	.PHONEY:  clean
	clean:
		rm -f *.o *.elf *.hex *.lst Makefile.bak *~