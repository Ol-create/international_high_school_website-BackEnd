from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student, Alumni
from .serializers import StudentSerializer, AlumniSerializer

# Create your views here.
#Get all student data
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.select_related('alumni_student').all()
        serialiser = StudentSerializer(students, many=True, context={'request': request})
        return Response(serialiser.data)
    elif request.method == 'POST':
        serialiser = StudentSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.validated_data
            return Response("OK")
        else:
            return Response (serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

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


    
    