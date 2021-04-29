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
      _, _, filenames = next(os.walk(path_name))
      if len(filenames) > 0 :
        path_name = os.path.join(ROOT_PATH, word, filenames[0])
        path_wav = path_name[:-4] + '.wav'
        
        print("--Gettig audioFile for sound: ", path_wav)
        if os.path.isfile(path_wav):
          res = make_response(send_file(
              path_wav, 
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
        path_img = path_name[:-4]+'.png'
        path_wav = path_name[:-4]+'.wav'

        print("--Gettig spectogram: ", path_img)
        if not os.path.isfile(path_img):
          # # not saving every specto
          # path_img = './specto.png'
          # print("--Creating specto img: ", path_img)
          # path_img = spe.get_spectogram( dir_save=path_img, audio_file=path_wav)
          
          # saving every specto
          print("--Creating specto img: ", path_img)
          path_img = spe.get_spectogram( audio_file=path_wav)
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

  print('--- Cheking ENV os var: ', os.environ)
  # app.run(debug=True)
  app.run(debug=False)

