py -m venv env
.\env\Scripts\activate
cd .\myproject\
pip install -r .\requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
