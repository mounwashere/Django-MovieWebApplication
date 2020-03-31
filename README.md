# Django-MovieWebApplication


#change directory to your project
cd movies_project

#install requirements.txt
pip install -r requirements.txt

#Create super user
python manage.py createsuperuser

python manage.py makemigrations

#apply migration 
python manage.py migrate

#start the django server
python manage.py runserver

#the link to the website
 http://127.0.0.1:8000/movies


#Create exe file 
pyinstaller --clean --name=movie manage.py


#change directory to dist/movie
cd dist/movies_register
#execute file 
movies_register.exe runserver localhost:8000
