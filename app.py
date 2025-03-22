from flask import Flask, request, render_template
from scipy.io.wavfile import write
import numpy as np
import io

app = Flask(__name__)
SAMPLERATE = 44100

@app.route("/", methods=['get', 'post'])
def index():
    fm = request.form
    if w_input:=fm.get("wave"):
        tfreq = int(fm.get("tfreq"))
        wave = [float(i) for i in w_input.split(",")[:-1]]*tfreq
        amplitude = np.iinfo(np.int16).max
        sound = np.array(amplitude)*wave
        # bytes_wav = bytes()
        # byte_io = io.BytesIO(bytes_wav)
        write("static/custom.wav", len(wave), sound.astype(np.int16))
    return render_template("create_waveform.html")

if __name__ == "__main__":
    app.run("0.0.0.0", 5002, True)