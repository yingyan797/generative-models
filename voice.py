from scipy.io.wavfile import write
import numpy as np

SAMPLERATE = 44100

def create_wave(loudness, freq, dur):
    t = np.linspace(0., dur, int(SAMPLERATE*dur))
    amplitude = np.iinfo(np.int16).max * loudness
    data = amplitude * np.sin(2. * np.pi * freq * t)
    return data

sound = create_wave(0.2, 440, 1)
write("static/sine.wav", SAMPLERATE, sound.astype(np.int16))