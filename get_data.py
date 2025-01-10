import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Load the audio file
audio_path = 'path_to_your_audio_file.wav'
sample_rate, audio_data = wav.read(audio_path)

# If the audio data has two channels (stereo), convert it to mono by averaging the channels
if audio_data.ndim > 1:
    audio_data = np.mean(audio_data, axis=1)

# Define the number of samples for the FFT and the time point to analyze
n_samples = 2048  # Number of samples for FFT
time_point = 1.0  # Time point in seconds

# Get the audio data segment at the specified time point
start_sample = int(time_point * sample_rate)
end_sample = start_sample + n_samples
audio_segment = audio_data[start_sample:end_sample]

# Perform FFT to get the frequency spectrum
freq_spectrum = np.abs(fft(audio_segment))

# Get the frequencies corresponding to the FFT result
freqs = np.fft.fftfreq(n_samples, 1/sample_rate)

# Plot the amplitude of each frequency band
plt.plot(freqs[:n_samples//2], freq_spectrum[:n_samples//2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum at {:.2f} seconds'.format(time_point))
plt.show()
