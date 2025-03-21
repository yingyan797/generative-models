from scipy.io.wavfile import write
import numpy as np

SAMPLERATE = 44100

def create_wave(loudness, freq, dur):
    t = np.linspace(0., dur, int(SAMPLERATE*dur))
    amplitude = np.iinfo(np.int16).max * loudness
    data = amplitude * np.sin(2. * np.pi * freq * t)
    return data

sound = None
freq = 220
while freq < 880:
    data = create_wave(0.1, freq, 0.2) + create_wave(0.1, freq*1.5, 0.2)
    if sound is None:
        sound = data
    else:
        sound = np.concatenate((sound, data), axis=0)    
    freq *= np.power(2, 1/6)

write("sine.wav", SAMPLERATE, sound.astype(np.int16))