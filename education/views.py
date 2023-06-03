from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def student_list(request):
    return Response("Student List")

# View Details about a Student
@api_view()
def student_detail(request, id):
    return Response(id)