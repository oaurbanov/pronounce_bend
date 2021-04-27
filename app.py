'''
localhost:5000/words
localhost:500/audio/plus
localhost:500/spec/plus

TODOs:
  get_specto(name) - TODO stantarize image
'''

from flask import Flask, jsonify, send_file, make_response, abort
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

  path_name = os.path.join(ROOT_PATH,word)
  print("\n-----Looking for audio: ", path_name)

  try:

    if os.path.isdir(path_name):
      _, _, filenames = next(os.walk(os.path.join(ROOT_PATH, word)))
      if len(filenames) > 0 :
        path_name = os.path.join(ROOT_PATH, word, filenames[0])
        print("--Gettig audioFile for sound: ", path_name)

        file = open(path_name, "rb")
        values = {"file": (path_name, file, "audio/wav")}

        res = make_response(send_file(
            path_name, 
            mimetype="audio/wav", 
            as_attachment=True, 
            attachment_filename="audio_word.wav"))
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res

    print("--Audio file does not exist:", path_name)
    abort(404)

  except Exception as ex:
    print("--get_audio Exception ocurred: ", ex)
    print(type(ex))
    abort(ex)


@app.route("/spec/<string:word>", methods=["GET"])
def get_specto(word):

  path_name = os.path.join(ROOT_PATH,word)
  print("\n-----Looking for specto: ", path_name)

  try:

    if os.path.isdir(path_name):
      _, _, filenames = next(os.walk(path_name))
      if len(filenames) > 0 :
        path_name = os.path.join(ROOT_PATH, word, filenames[0])
        print("--Gettig spectogram for sound: ", path_name)

        path_img = path_name[:-4]+'.png'
        print("--Checking if img exists: ", path_img)
        if not os.path.isfile(path_img):
          print("--Creating specto img: ", path_img)
          path_img = spe.get_spectogram(audio_file=path_name)
        else:
          print("--Img already created: ", path_img)

        res = make_response(send_file(
            path_img, 
            mimetype="image/png", 
            as_attachment=True, 
            attachment_filename="spec.png"))
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    
    print("--Sound file does not exist:", path_name)
    abort(404)

  except Exception as ex:
    print("--get_specto Exception ocurred: ", ex)
    print(type(ex))
    abort(ex)


@app.route("/words", methods=["GET"])
def get_words():
  
  try:
    dataset_path = "./DataSet"
    # loop through all sub-dirs
    for dirpath, dirnames, filenames in os.walk(dataset_path):
      break
    return jsonify(dirnames)
  
  except Exception as ex:
    print("--get_words Exception ocurred: ", ex)
    print(type(ex))
    abort(ex)

if __name__ == "__main__":
  app.run(debug=True)

