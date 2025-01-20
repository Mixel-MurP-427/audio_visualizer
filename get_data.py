import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.fftpack import fft
#from pydub import AudioSegment
#for pngs
from PIL import Image, ImageDraw


# Function to convert audio to WAV format
def convert_to_wav(audio_path):
    audio = AudioSegment.from_file(audio_path)
    audio.export("temp_audio.wav", format="wav")

# Convert the audio file to WAV format
#convert_to_wav("/Users/westcoast/Music/Connor_mp3s/Portal2-03-999999.mp3")

# Load the converted WAV file
#sample_rate, audio_data = wav.read("temp_audio.wav")
sample_rate, audio_data = wav.read("/Users/westcoast/Downloads/Adventure_core_singing02.wav")

# If the audio data has two channels (stereo), convert it to mono by averaging the channels
if audio_data.ndim > 1:
    audio_data = np.mean(audio_data, axis=1)

# Define the number of samples for the FFT and the time point to analyze
n_samples = 128  # Number of samples for FFT. Other parts of the code are hotwired to just use the value 128.
time_point = 14.0  # Time point in seconds

# Get the audio data segment at the specified time point
start_sample = int(time_point * sample_rate)
end_sample = start_sample + n_samples
audio_segment = audio_data[start_sample:end_sample]

# Perform FFT to get the frequency spectrum
freq_spectrum = np.abs(fft(audio_segment))

# Get the frequencies corresponding to the FFT result
freqs = np.fft.fftfreq(n_samples, 1/sample_rate)

freq_spectrum = freq_spectrum[:n_samples//2]
freqs = freqs[:n_samples//2]

# Plot the amplitude of each frequency band
plt.plot(freqs, freq_spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum at {:.2f} seconds'.format(time_point))
plt.show()


def process_freqs(pfFreqs):
    magicNumber = 1875 #this scales down the freq values to fit in the 64x64 grid
    pfWhite = (230, 230, 255)
    pfColor1 = (255, 127, 0)
    pfColor2 = (0, 0, 200)
    pfColorRange = 0.2
    myImage = Image.new("RGB", (64, 64))
    drawn = ImageDraw.Draw(myImage)
    drawn.rectangle([0, 0, 64, 64], fill="#000000")

    for pfX, pfBar in enumerate(pfFreqs):
        pfY = 63 - round(pfBar / magicNumber)
        drawn.rectangle([pfX, pfY+1, pfX, 64], fill=pfColor1)#special effects
        pfHalfHeight = 63 - round(pfBar/magicNumber*pfColorRange)
        drawn.rectangle([pfX, pfHalfHeight, pfX, 64], fill=pfColor2)#extra special effects
        myImage.putpixel((pfX, pfY), pfWhite)#tops



    myImage.save("audio_spectrum.png", "PNG")

process_freqs(freq_spectrum)