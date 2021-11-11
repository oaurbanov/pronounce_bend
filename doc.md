# Create virtual env and install from requirements.txt
virtualenv venv
source venv/bin/activate
pip install -r ./requirements.txt

# Create virtual env, install packs and creating requirements.txt
#pip install flask librosa matplotlib gunicorn flask_cors
pip list
pip freeze > ./requirements.txt

# Running the app
python app.py


# Deployment (Heroku)

## Full first time procedure
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


## Once page exists on Heroku
heroku login
git push heroku master
heroku logs --tail


## online backend page
https://pronouncebend.herokuapp.com/

