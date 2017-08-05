#!/usr/bin/env python

# scrollphat_spectrum.py at https://gist.github.com/fvdbosch/45cd94bf056d218bc464c6966aa81782
# loopback_spectrum.conf at https://gist.github.com/fvdbosch/b08d5158f32a2a68ed5e71c9dde50b21#file-loopback_spectrum-conf
# Original script by Pimoroni: https://learn.pimoroni.com/tutorial/sandyj/scroll-phat-spectrum-analyser
# Modified to take audio stream from loopback device as input, instead of file

import sys
import wave
import alsaaudio as aa
from struct import unpack
import numpy as np
import scrollphat
import pyaudio

chunk      = 4096 # Change if too fast/slow, never less than 2**11
sample_rate = 32000

# CHANGE THIS TO CORRECT INPUT DEVICE
# Enable stereo mixing in your sound card
# to make you sound output an input
# Use list_devices() to list all your input devices
device = 0

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,
                channels = 1,
                rate = sample_rate,
                input = True,
                frames_per_buffer = chunk,
                input_device_index = device)

matrix    = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
power     = []
weighting = [1, 1, 2, 4, 8, 8, 8, 8, 16, 16, 16]

scrollphat.set_brightness(10)
#scrollphat.set_rotate(180)

# https://gist.github.com/limitedmage/2628477#file-soundlight-py
def list_devices():
    # List all audio input devices
    p = pyaudio.PyAudio()
    i = 0
    n = p.get_device_count()
    while i < n:
        dev = p.get_device_info_by_index(i)
        if dev['maxInputChannels'] > 0:
            print str(i)+'. '+dev['name']
        i += 1

def power_index(val):
    return int(2 * chunk * val / sample_rate)

def compute_fft(data, chunk, sample_rate):
    global matrix
    data = unpack("%dh" % (len(data) / 2), data)
    data = np.array(data, dtype='h')

    fourier = np.fft.rfft(data)
    fourier = np.delete(fourier, len(fourier) - 1)

    power = np.abs(fourier)
    matrix[0] = int(np.mean(power[power_index(0)    :power_index(156) :1]))
    matrix[1] = int(np.mean(power[power_index(156)  :power_index(313) :1]))
    matrix[2] = int(np.mean(power[power_index(313)  :power_index(625) :1]))
    matrix[3] = int(np.mean(power[power_index(625)  :power_index(1000) :1]))
    matrix[4] = int(np.mean(power[power_index(1000) :power_index(2000) :1]))
    matrix[5] = int(np.mean(power[power_index(2000) :power_index(3000) :1]))
    matrix[6] = int(np.mean(power[power_index(3000) :power_index(4000) :1]))
    matrix[7] = int(np.mean(power[power_index(4000) :power_index(5000) :1]))
    matrix[8] = int(np.mean(power[power_index(5000) :power_index(6000) :1]))
    matrix[9] = int(np.mean(power[power_index(6000) :power_index(7000) :1]))
    matrix[10] = int(np.mean(power[power_index(7000):power_index(8000) :1]))

    matrix = np.divide(np.multiply(matrix, weighting), 1000000)
    matrix = matrix.clip(0, 5)
    matrix = [float(m) for m in matrix]

    return matrix

list_devices()

while True:
    data = stream.read(chunk)
    matrix = compute_fft(data, chunk, sample_rate)
    scrollphat.graph(matrix, 0, 5)