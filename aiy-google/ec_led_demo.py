#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('turn red on')
    recognizer.expect_phrase('turn red off')
    recognizer.expect_phrase('turn green on')
    recognizer.expect_phrase('turn green off')
    recognizer.expect_phrase('turn both on')
    recognizer.expect_phrase('turn both off')

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize()
        if text is None:
            print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
            if 'turn red on' in text:
                aiy.audio.say ('OK, I will turn red on')
                GPIO.output(26,True)
            elif 'turn red off' in text:
                aiy.audio.say ('OK, I will turn red off')
                GPIO.output(26,False)
            elif 'turn green on' in text:
                aiy.audio.say ('OK, I will turn green on')
                GPIO.output(6,True)
            elif 'turn green off' in text:
                aiy.audio.say ('OK, I will turn green off')
                GPIO.output(6,False)
            elif 'turn both on' in text:
                aiy.audio.say ('OK, I will turn both of them on')
                GPIO.output(26,True)
                GPIO.output(6,True)
            elif 'turn both off' in text:
                aiy.audio.say ('OK, I will turn both of them off')
                GPIO.output(26,False)
                GPIO.output(6,False)                
            elif 'goodbye' in text:
                aiy.audio.say ('All finished. That was really exciting.')
                GPIO.output(26,False)
                GPIO.output(6,False)  
                break


if __name__ == '__main__':
    main()
