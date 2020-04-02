import pyaudio
import numpy

p = pyaudio.PyAudio()

volume 0.5
samp_rate = 44100
duration = 1.0
f = 100

samples = (numpy.sin(2*numpy.pi*numpy.arange(samp_rate*duration)*f/samp_rate)).astype(numpy.float32)

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sample_rate
                output=True)

stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()

