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

#Create exe file 
pyinstaller --clean --name=movie manage.py


#change directory to dist/movie
cd dist/movie 
#execute file 


