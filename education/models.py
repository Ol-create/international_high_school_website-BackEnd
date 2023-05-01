from django.db import models

# Create your models here.
class Student(models.Model):
    
    MALE_SEX_TYPE = 'ML'
    FEMALE_SEX_TYPE = 'FM'
    PREFER_NOT_TO_SAY_TYPE = "BN"

    SEX_TYPE_CHOICE = [
        (MALE_SEX_TYPE, "Male"),
        (FEMALE_SEX_TYPE, "Female"),
        (PREFER_NOT_TO_SAY_TYPE, "Prefer not to say")
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(auto_now_add=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=SEX_TYPE_CHOICE, default=PREFER_NOT_TO_SAY_TYPE)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(auto_now=True)
    student = models.ManyToManyField(Student)

class NewsAndEvent(models.Model):
    news_title = models.CharField(max_length=255)
    description = models.TextField()
    news_date = models.DateField(auto_now_add=True)
    course = models.ManyToManyField(Course)

class ComputerBaseTest(models.Model):
    test_name = models.CharField(max_length=255)
    test_time = models.TimeField(auto_now_add=True)
    test_date = models.DateField(auto_now=True)
    score = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)

class AcedemicReport (models.Model):
    report_type = models.CharField(max_length=255)
    grade = models.CharField(max_length=1)
    report_date = models.DateField(auto_now_add=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, default=None)

class Alumni(models.Model):
    alumni_name = models.CharField(max_length=255)
    graduation_year = models.DateField(auto_now_add=True, verbose_name='Year')
    current_occupation = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.SET_DEFAULT, default=None)
