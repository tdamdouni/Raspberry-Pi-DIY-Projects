#!/bin/bash

echo -e "\ntesting audio"
speaker-test -l1 -c2 -t wav
sleep 1

if command -v mpg321 > /dev/null; then
    echo -e "\ntesting mp3 playback\n"
    mpg321 ./test.mp3
else
    echo -e "\ntesting basic wav playback\n"
    aplay ./test.wav
fi
sleep 1

echo
echo "testing gpio control..."
echo "press all buttons along the side of the pHAT..."
echo "press the power button on the pHAT to exit..."
sleep 1

echo -e "\ntesting VU meter"
python ./test.py
echo

exit 0
