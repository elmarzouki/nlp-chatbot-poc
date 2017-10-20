# create virtualenv
# virtualenv env
# source env/bin/activate       # if you're using linux :')
# env\Scripts\activate          # if you're using windows -_-

# Install dependencies
pip install -r requirements.txt

# install all en packages
python -m spacy.en.download all

python -m spacy.en.download parser
python -m spacy.en.download glove


# migrate
cd chatbot
python manage.py migrate