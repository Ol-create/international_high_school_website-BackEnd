from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student, Alumni
from .serializers import StudentSerializer, AlumniSerializer

# Create your views here.
#Get all student data
@api_view()
def student_list(request):
    students = Student.objects.all()
    serialiser = StudentSerializer(students, many=True)
    return Response(serialiser.data)

# View Details about a Student
@api_view()
def student_detail(request, id):   
    student = get_object_or_404(Student, pk=id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

#Get all alumni data
@api_view()
def alumni_list(request):
    alumni = Alumni.objects.all()
    serialiser = AlumniSerializer(alumni, many=True)
    return Response(serialiser.data)


    
    