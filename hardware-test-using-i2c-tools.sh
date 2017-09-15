#!/bin/bash
addr="0x74"
ISET='i2cset -y 1'

echo "switch to configuration bank"
${ISET} $addr 0xfd 0x0b i

echo "switch to picture mode"
${ISET} $addr 0 0 i

echo "disable audio sync"
${ISET} $addr 0x06 0 i

echo "switch to bank 1"
${ISET} $addr 0xfd 1 i

${ISET} $addr 0xfd 0 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 i

echo "switch to bank 0"
${ISET} $addr 0xfd 0 i

echo "enable all leds"
${ISET} $addr 0xfd 0 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 255 i

echo "show some pixels"
${ISET} $addr 0x24 0x00 $(seq 1 31 | tr '\n' ' ') i