from django.shortcuts import render
from .models import Parent
from education.models import Student, Course, AcedemicReport, Alumni, ComputerBaseTest

# Create your views here.  

def hello_victor(request):
    queryset = ComputerBaseTest.objects.all()
    return render(request, 'hello.html', {"dataset": list(queryset)})
    