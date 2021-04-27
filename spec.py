import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


FRAME_SIZE = 4096#2048
HOP_SIZE = 128# 1024
SAMPLE_RATE = 44100#22050

def load_scaled(file_path):
  signal, sr = librosa.load(file_path, SAMPLE_RATE)
  signal_sfft = librosa.stft(signal, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
  print(signal_sfft.shape)
  signal_sfft_abs = np.abs(signal_sfft) ** 2
  signal_sftt_scaled = librosa.power_to_db(signal_sfft_abs)
  return signal_sftt_scaled, sr


def save_spectrogram(dir_save, Y, sr, hop_length, y_axis="linear"): # linear, log
  fig = plt.figure(figsize=(25, 10))
  librosa.display.specshow(Y, 
                            sr=sr, 
                            hop_length=hop_length, 
                            x_axis="time", 
                            y_axis=y_axis,
                          cmap='nipy_spectral')
  # plt.colorbar(format="%+2.f")
  plt.axis('off') # Removing axis from figure to save
  fig.savefig(dir_save, dpi=200, pad_inches=0, bbox_inches='tight' )


def get_spectogram(dir_save='', audio_file= "./DataSet/plus/0000.wav"):
  if not dir_save:
    dir_save = audio_file[:-4] + '.png'
    print("--Saving image: ", dir_save)
  ad_spec, _ =  load_scaled(audio_file)
  save_spectrogram(dir_save, ad_spec, sr=SAMPLE_RATE, hop_length=HOP_SIZE, y_axis="log")
  return dir_save

if __name__ == "__main__":
  get_spectogram('./DataSet/merci/0000.wav', './specto.png')