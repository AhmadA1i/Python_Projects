# Import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# set frequency
freq = 44100

#set duration
duration = 5

# start recording
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# time of recording
sd.wait()

# converting numpy array into audio file
write("recording0.wav", freq, recording)

# converting numpy array into audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)