import sys
import wave
import alsaaudio as aa
from struct import unpack
import numpy as np
import unicornhat as uh

# Open the wav file
wavfile = wave.open(sys.argv[1], 'r')
print "Playing " + sys.argv[1] + " ..."
sample_rate = wavfile.getframerate()
no_channels = wavfile.getnchannels()
chunk = 4096

# Setup the output
output = aa.PCM(aa.PCM_PLAYBACK, aa.PCM_NORMAL)
output.setchannels(no_channels)
output.setrate(sample_rate)
output.setformat(aa.PCM_FORMAT_S16_LE)
output.setperiodsize(chunk)

# FFT parameters
matrix    = [0, 0, 0, 0, 0, 0, 0, 0]
power     = []
weighting = [1, 1, 2, 4, 8, 8, 8, 8]

# Display config
max_height    = 8
max_width     = 8
display_count = 0                               
refresh_rate  = 2
peak_timeout  = 1
peaks         = [0] * len(matrix)
peak_counters = [0] * len(matrix)
uh.rotation(90)                             
uh.brightness(0.4)
blue = (4,180,255)
pink = (251,68,246)

def power_index(val):
    return int(2 * chunk * val / sample_rate)

def compute_fft(data, chunk, sample_rate):
    global matrix
    data = unpack("%dh" % (len(data) / 2), data)
    data = np.array(data, dtype='h')

    # Perform FFT
    fourier = np.fft.rfft(data)
    fourier = np.delete(fourier, len(fourier) - 1)

    # Create bins
    power = np.abs(fourier)
    matrix[0] = int(np.mean(power[power_index(0)    :power_index(156) :1]))
    matrix[1] = int(np.mean(power[power_index(156)  :power_index(313) :1]))
    matrix[2] = int(np.mean(power[power_index(313)  :power_index(625) :1]))
    matrix[3] = int(np.mean(power[power_index(625)  :power_index(1000) :1]))
    matrix[4] = int(np.mean(power[power_index(1000) :power_index(2000) :1]))
    matrix[5] = int(np.mean(power[power_index(2000) :power_index(3000) :1]))
    matrix[6] = int(np.mean(power[power_index(3000) :power_index(4000) :1]))
    matrix[7] = int(np.mean(power[power_index(4000) :power_index(5000) :1]))

    # Weight the bins
    matrix = np.divide(np.multiply(matrix, weighting), 1000000)
    matrix = matrix.clip(0, max_height)

    return matrix

def draw_levels():
    global peak_counters, peaks

    uh.clear() 
    
    # Output to UnicornHat
    for i in range(0, max_width):
        
        level = matrix[i]
        if level >= peaks[i]:
            # Reset peak
            peaks[i] = level
            peak_counters[i] = 0
        else:
            peak_counters[i] = peak_counters[i] + 1

        if peak_counters[i] > peak_timeout:
            # Reduce peak
            peak_counters[i] = 0

            if peaks[i] > level:
                peaks[i] = peaks[i] - 1
                        
        for j in range(level):
            # Draw level
            uh.set_pixel(max_height-1-i,j,blue[0],blue[1],blue[2])   

        # Draw peak
        uh.set_pixel(max_height-1-i,peaks[i]-1,pink[0],pink[1],pink[2])
        
    uh.show()

# Read in first chunk of data
data = wavfile.readframes(chunk)

while data != '':
    # Write the audio data
    output.write(data)

    if len(data) != 4*chunk:
        # Don't FFT final chunk
        break

    matrix = compute_fft(data, chunk, sample_rate)

    draw_levels()

    # Read the next chunk of data           
    data = wavfile.readframes(chunk)
