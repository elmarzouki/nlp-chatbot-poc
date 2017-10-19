# create virtualenv
# virtualenv env
# source env/bin/activate       # if you're using linux :')
# env\Scripts\activate          # if you're using windows -_-

# Install dependencies
pip install -r requirements.txt

# migrate
cd chatbot
python manage.py migrate