# django-rest_todo
#create virtual environment
python venv env
#activate virtual environment
env\Scripts\activate
#install django
pip install django
#install djangorestframework
pip install djangorestframework
cd Todo_django
#create djangoproject
django-admin startproject ToDo
cd ToDo
#creare djangoapp
python manage.py startapp Todo_app
#To run server
python manage.py runserver

This is a basic Todo Application Built using DjangoRestFramework
