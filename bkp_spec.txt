

FRAME_SIZE = 4096#2048
HOP_SIZE = 128# 1024
SAMPLE_RATE = 44100#22050


def get_spectogram(audio_file= "./DataSet/plus/0000.wav", dir_save='./specto.png'):
  return dir_save

if __name__ == "__main__":
  get_spectogram('./DataSet/merci/0000.wav', './specto.png')