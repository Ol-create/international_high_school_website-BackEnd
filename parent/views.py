from django.shortcuts import render
from .models import Parent
from education.models import Student

# Create your views here.

def hello_victor(request):
    query_set = Student.objects.all()
    return render(request , 'hello.html' , {"name": "Akande", "query_set": list(query_set)})

