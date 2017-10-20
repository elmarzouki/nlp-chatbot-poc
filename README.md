# nlp-chatbot-poc
simple chatbot using natural language processing "spaCy"
## Setup

Create virtual environment, install dependencies and run migrations to setup the app:
```
# create virtualenv
virtualenv env
# activate env
source env/bin/activate         # if you're using linux :')
# env\Scripts\activate          # if you're using windows -_-

# install dependencies
chmod +x build.sh
./build.sh
```

## Run the application

Run the server:

```
cd chatbox/
# run the server
python manage.py runserver
# create superuser
python manage.py createsuperuser
```
## testing the parser on desktop
```
cd helper/
# test nlp parsing
python parser.py
```
