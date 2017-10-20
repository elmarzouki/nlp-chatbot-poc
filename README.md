# nlp-chatbot-poc
Simple chat bot using natural language processing.

## Technologies used:
+ Django.
+ django-restframework
+ Angular2
+ spaCy

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


Start the client app:

```
cd ChatRoom
ng serve
```

## testing the parser using CLI
```
cd helper/
# test nlp parser logic
python parser.py
```

## References:
- [elitedatascience.com](https://elitedatascience.com/python-nlp-libraries)
- [spacy.io](https://spacy.io/docs/usage/models)
- [djangoproject.com](https://www.djangoproject.com/)
- [django-rest-framework.org](http://www.django-rest-framework.org)
- [angular.io](https://cli.angular.io/)

