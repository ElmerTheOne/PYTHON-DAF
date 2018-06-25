"""PyAudio Example: Play a WAVE file."""
import time
import pyaudio

import sys

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100

if len(sys.argv) < 2:
    print("delay_milliseconds" % sys.argv[0])
    sys.exit(-1)


delay = float(sys.argv[1])/1000.0


p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)
print("The delay is roughly :",delay * 1000,"ms.")

frames = []

for i in range(0, int(RATE / CHUNK * delay)):
    data = stream.read(CHUNK)
    frames.append(data)






for i in range(0, int(RATE / CHUNK * 3600)):
    data = stream.read(CHUNK)
    frames.append(data)
    stream.write(frames[i], CHUNK)

stream.stop_stream()
stream.close()
p.terminate()
