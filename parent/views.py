from django.shortcuts import render
from .models import Parent
from education.models import Student, Course, AcedemicReport, Alumni

# Create your views here.

# def hello_victor(request):
#     students = []
#     score = AcedemicReport.objects.filter(course__course_name='French', student__id__range=(30, 1000))
#     # for student in query_set:
#     #     students.append(student)
#     return render(request , 'hello.html' , {"name": "Akande", "scores": list(score)})

# def hello_victor(request):
#     scores = AcedemicReport.objects.prefetch_related('student', 'course').filter(student__id__range=(30, 1000))
#     return render(request, 'hello.html', {"name": "Akande", "scores": scores})
    

def hello_victor(request):
    alumni_queryset = Alumni.objects.all()
    return render(request, 'hello.html', {"alumni_dataset": list(alumni_queryset)})
    