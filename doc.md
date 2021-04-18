virtualenv venv
source venv/bin/activate

pip install flask librosa matplotlib gunicorn

python app.py