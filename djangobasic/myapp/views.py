from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel
from django_plotly_dash import DjangoDash
from streamlit_app import streamlit_app

# Create your views here.

def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})

def merhabaindex(request):     
    return HttpResponse("Merhaba, dünya!")  

def selamindex(request):     
    return HttpResponse("Selam, dünya!")  

def home(request):     
    return render(request, 'home.html')  

def index(request):     
    return render(request, 'index.html') 


def my_view(request):
    my_data = MyModel.objects.all()
    context = {'my_data': my_data}
    return render(request, 'my_template.html', context)
