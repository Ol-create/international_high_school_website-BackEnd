from django.shortcuts import render
from .models import Parent

# Create your views here.

def hello_victor(request):
    return render(request , 'hello.html' , {"name": "Akande"})

