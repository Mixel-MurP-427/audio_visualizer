import numpy as np
import librosa
import matplotlib.pyplot as plt

# Load the audio file
audio_path = 'C:/Users/jodim/Documents/Connor_Coding/audio_visualizer/Alan Walker - Dreamer [NCS Release].mp3'
y, sr = librosa.load(audio_path, sr=None)

# Define the number of frequency bands (bins)
n_fft = 2048  # Number of FFT components
hop_length = 512  # Number of samples between successive frames

# Compute the Short-Time Fourier Transform (STFT)
stft = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))

# Convert the STFT to dB scale
db_stft = librosa.amplitude_to_db(stft, ref=np.max)

# Get the amplitude of each frequency band at a given frame (time point)
frame = 100  # Example frame index
amplitude = db_stft[:, frame]

# Plot the amplitude of each frequency band at the given frame
freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
plt.plot(freqs, amplitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.title('Frequency Spectrum at Frame {}'.format(frame))
plt.show()
