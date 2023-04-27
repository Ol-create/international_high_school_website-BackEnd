from django.db import models

# Create your models here.
class Student(models.Model):
    
    MALE_SEX_TYPE = 'Male'
    FEMALE_SEX_TYPE = 'Female'
    PREFER_NOT_TO_SAY_TYPE = "Prefer not to say"

    SEX_TYPE_CHOICE = [
        ("M", MALE_SEX_TYPE),
        ("F", FEMALE_SEX_TYPE),
        ("N", PREFER_NOT_TO_SAY_TYPE)
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_day = models.DateField(auto_now_add=True)
    class_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_TYPE_CHOICE, default=PREFER_NOT_TO_SAY_TYPE)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(auto_now=True)

class NewsAndEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

class ComputerBaseTest(models.Model):
    name = models.CharField(max_length=255)
    time = models.TimeField(auto_now_add=True)
    score = models.IntegerField()

class AcedemicReport (models.Model):
    report_type = models.CharField(max_length=255)
    grade = models.CharField(max_length=1)
    date = models.DateField(auto_now_add=True)

class Alumni(models.Model):
    name = models.CharField(max_length=255)
    graduation_year = models.DateField(auto_now_add=True)
    current_occupation = models.CharField(max_length=255)
