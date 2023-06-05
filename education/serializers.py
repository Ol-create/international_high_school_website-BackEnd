from rest_framework import serializers
from .models import Student, ComputerBaseTest, Course, AcedemicReport, Alumni, NewsAndEvent

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'student_identification_number', 
                  'class_level', 'discipline', 'email', 'address', 'birthday', 'gender']
    

class CourseSerializer(serializers.ModelSerializer):
    class meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'score']

class NewsAndEventSerializer(serializers.ModelSerializer):
    class meta: 
        model = NewsAndEvent
        fields = ['id', 'author', 'news_title', 'description', 'content', 'news_date', '']

class ComputerBaseTestSerializer(serializers.ModelSerializer):
    class meta:
        model = ComputerBaseTest
        fields = ['id', 'examination_type_choice', 'grade_choice', 'examination_name', 'student',
                   'test_date', 'grade', 'score']
        
class AcedemicReportSerialiser(serializers.ModelSerializer):
    class meta:
        model = AcedemicReport
        fields = ['id', 'school_term_choice', 'school_term', 'report_date', 'student', 'course']
        
class AlumniSerializer(serializers.ModelSerializer):
    class meta:
        model = Alumni
        fields = ['student', 'phone_number', 'awards', 'graduation_year', 'current_occupation']