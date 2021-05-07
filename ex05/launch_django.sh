#! /usr/local/bin/zsh

python3 -m venv django_venv
PWD=`pwd`
echo $PWD
activate () {
    source $PWD/django_venv/bin/activate
}
activate
python3 -m pip install -r requirement.txt
django-admin startproject myfirstapp
cd myfirstapp
python3 manage.py startapp helloworld
cd helloworld
echo "from django.http import HttpResponse
def index(request):
    return HttpResponse('<h1>Hello World !</h1>')" >> views.py

touch urls.py
echo "from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index')
]" > urls.py
cd ../myfirstapp
echo "from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', include('helloworld.urls')),
]" > urls.py
cd ..
python3 manage.py runserver