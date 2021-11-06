'''
localhost:5000/words
localhost:500/audio/plus
localhost:500/spec/plus

TODOs:
  get_specto(name) - TODO stantarize image
'''

from flask import Flask, jsonify, send_file, make_response, abort, Response
import os
import spec as spe

from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
            attachment_filename="spec2.png"))
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    
    print("--Sound file does not exist:", path_name)
    abort(404)

  except Exception as ex:
    print("--get_specto Exception ocurred: ", ex)
    print(type(ex))
    abort(ex)


@app.route("/specfromaudio/<string:word>", methods=["POST"])
def get_specto_from_audio(word):
  path_wav = os.path.join(ROOT_PATH, 'new', '0000.wav')
  path_img = os.path.join(ROOT_PATH, 'new', '0000.png') # not really needed
  if request.method == 'POST':
      print("Recieved Audio File")
      print(request)
      file = request.files['file']
      print('File from the POST request is: {}'.format(file))
      with open(path_wav, "wb") as aud:
            aud_stream = file.read()
            aud.write(aud_stream)
      print('audio file saved')
      path_img = spe.get_spectogram( dir_save= path_img, audio_file=path_wav)
      print('audio img saved')
      return "Success"
      # return Response("{'a':'b'}", status=201, mimetype='application/json')
  return 'Call from get'


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

