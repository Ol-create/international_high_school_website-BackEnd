from rest_framework import serializers
from .models import Student, ComputerBaseTest, Course, AcedemicReport, Alumni, NewsAndEvent

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'student_identification_number', 
                  'class_level', 'discipline', 'email', 'address', 'birthday', 'gender']
    

