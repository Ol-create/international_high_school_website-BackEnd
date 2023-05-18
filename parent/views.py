from django.shortcuts import render
from .models import Parent
from education.models import Student, Course, AcedemicReport, Alumni, ComputerBaseTest

# Create your views here.  

def hello_victor(request):
    queryset = ComputerBaseTest.objects.prefetch_selected('student').all()
    return render(request, 'hello.html', {"dataset": list(queryset)})
    

def create_student(request):
    student = Student()
    student.first_name = 'Paul'
    student.last_name = 'Oluyemi'
    student.address = '49, Ojido AdoEkiti'
    student.birthday = '2023-06-28'
    student.class_level = 'SS3'
    student.discipline = 'SCI'
    student.email = 'oluola96@gmail.com'
    student.gender = 'ML'
    student.id = 1001
    student.save()

    data = Student.objects.latest('id')

    return render(request, 'create_student.html', {'data': data})


