'''
localhost:5000/words
localhost:500/audio/plus
localhost:500/spec/plus

TODOs:
  get_specto(name) - TODO stantarize image
'''

from flask import Flask, jsonify, send_file, make_response
import os
import spec as spe

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = True

ROOT_PATH = "./DataSet"


@app.route('/', methods=["GET"])
def index():
  return "Hello Pronounce_bend app"

@app.route("/audio/<string:word>", methods=["GET"])
def get_audio(word):

  path_name = ''

  print(os.path.join(ROOT_PATH,word))
  _, _, filenames = next(os.walk(os.path.join(ROOT_PATH, word)))
  if len(filenames) > 0 :
    path_name = os.path.join(ROOT_PATH, word, filenames[0])
    print(path_name)

    file = open(path_name, "rb")
    values = {"file": (path_name, file, "audio/wav")}

    res = make_response(send_file(
        path_name, 
        mimetype="audio/wav", 
        as_attachment=True, 
        attachment_filename="test.wav"))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

  #result = { "name": "pourquio", "audio": "this is the audio"}
  #return jsonify(result)


@app.route("/spec/<string:word>", methods=["GET"])
def get_specto(word):

  path_name = ''

  print(os.path.join(ROOT_PATH,word))
  _, _, filenames = next(os.walk(os.path.join(ROOT_PATH, word)))
  if len(filenames) > 0 :
    path_name = os.path.join(ROOT_PATH, word, filenames[0])
    print(path_name)


    path_name = spe.get_spectogram(path_name, './spec_draw.png')

    # file = open(path_name, "rb")
    # values = {"file": (path_name, file, "audio/wav")}

    res = make_response(send_file(
        path_name, 
        mimetype="image/png", 
        as_attachment=True, 
        attachment_filename="spec.png"))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


@app.route("/words", methods=["GET"])
def get_words():
  
  dataset_path = "./DataSet"
  # loop through all sub-dirs
  for dirpath, dirnames, filenames in os.walk(dataset_path):
    break
  return jsonify(dirnames)

if __name__ == "__main__":
  app.run(debug=True)

