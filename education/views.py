from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
@api_view()
def student_list(request):
    return Response("Student List")

# View Details about a Student
@api_view()
def student_detail(request, id):
    try:
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    