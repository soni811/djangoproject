==============================================
Beginner level django projects
==============================================

# pip install django
# django-admin startproject projectname
# cd projectname
# python manage.py runserver
# python manage.py startapp appname

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appname',  # Add your app here
]


# python manage.py makemigrations
# python manage.py migrate

# Create a urls.py file inside myapp/ (if it doesn’t exist) and add:
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]

# after that link into main projectname
# Now, link this to the project's main urls.py file (myproject/urls.py):

# To create a GET API in Django, follow these step

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# myapp/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# pip install djangorestframework
# INSTALLED_APPS = [
    'rest_framework',
    'myapp',
]


"""sudo apt update
sudo apt install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient """

# after that the can be apply for a  
# python manage.py migrate
# python manage.py makemigrations  myapp


"""In Django, specifically Django REST Framework (DRF), serializers.py is a file where you define serializers, which convert complex data types (like Django models) into JSON (or other formats like XML) and vice versa."""

"""
Why Use Serializers?
Serializers help in:
✅ Converting Django model instances to JSON (for APIs).
✅ Validating and deserializing JSON input from API requests.
✅ Enforcing data validation rules before saving to the database.


ViewSet :  A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post() , and instead provides actions such as .list() and .create() .
"""


Auth:
    write in manage.py in project :
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django REST Framework
    'rest_framework',
    'rest_framework.authtoken',  # This enables token authentication
]

    python manage.py migrate


python manage.py createsuperuser



# python manage.py shell
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
user = User.objects.get(username="admin")
token, created = Token.objects.get_or_create(user=user)
print(token.key) # 6ce595e2f0367823b9d0a9222fcc2e06fd67c370
