Git repository- Shruti Sharma

https://github.com/shrushh/django-caps2.git

Docker hub repository

docker pull shrush/django-caps2



RUN BUILD

git clone https://github.com/shrushh/django-caps2.git

cd django-caps2
cd caps2

docker-compose build 
docker-compose up

OR
(To keep running the Django web app in background)

docker-compose up -d 


(BROWSE TO THE http://localhost:8000/ )

RUN IN VS CODE OR YOU LOCAL MACHINE

Go to settings.py file

IN DATABASES - Change the host from ‘db’ to ‘localhost’

Source venv/bin/activate
cd capst2
pip install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage,py runserver


  