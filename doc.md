virtualenv venv
source venv/bin/activate

pip install -r ./requirements.txt
#pip install flask librosa matplotlib gunicorn flask_cors
pip list

pip freeze > ./requirements.txt

python app.py


# Heroku deployment

www.heroku.com for seting up a server to host the page, install it
heroku login

pip3.7 install gunicorn
pip3.7 freeze > requirements.txt

touch Procfile:
"web: gunicorn app:app" > Procfile

git init 
git add .
git commit -m "Init app"

heroku create flaskcrudapptutorial
git push heroku master

heroku logs --tail


my page:
https://pronouncebend.herokuapp.com/

