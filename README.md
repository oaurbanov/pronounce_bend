# pronounce_bend

Backend of the pronounce app. It uses AI algorithms for evaluating the match between 2 samples of the same word (audio files)

## Getting Started

Running development server:

```bash
# create virtual env and install requirements
virtualenv venv
source venv/bin/activate
pip install -r ./requirements.txt

# start flask server application
python app.py
```

# REST api:

GET:

  /words -> json with the available words on DataSet

  /audio/word  -> returns .wav
  /spec/word   -> returns .png ( already created spectogram)


POST:

  /specfromaudio/new -> creates new pair wav and specto. Get them on:
    /audio/new
    /spec/new