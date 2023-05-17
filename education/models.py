from django.db import models
import uuid
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

    #Model choice for class level like SS3, SS2, and SS1
    SENIOR_CLASS_ONE = 'SS1'
    SENIOR_CLASS_TWO = 'SS2'
    SENIOR_CLASS_THREE = 'SS3'

    SENIOR_CLASS_LEVEL = [
        (SENIOR_CLASS_ONE, "Senior Scondary I"),
        (SENIOR_CLASS_TWO, "Senior Scondary II"),
        (SENIOR_CLASS_THREE, "Senior Scondary III"),
    ]

    #Model Discipline Choice

     #Model choice for class level like SS3, SS2, and SS1
    ART_CLASS = 'ART'
    COMMERCIAL_CLASS = 'CMR'
    SCIENCE_CLASS = 'SCI'

    DISCIPLINE_CHOICE = [
        (ART_CLASS, "Art Study"),
        (COMMERCIAL_CLASS, "Commercial Study"),
        (SCIENCE_CLASS, "Science Study"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # profile_image = models.ImageField(null=True)
    student_identification_number = models.UUIDField(default=uuid.uuid4, editable=False)
    class_level = models.CharField(max_length=3, 
                                   choices=SENIOR_CLASS_LEVEL, 
                                   default=SENIOR_CLASS_ONE )
    discipline = models.CharField(max_length=3, 
                                  choices=DISCIPLINE_CHOICE, 
                                  default=COMMERCIAL_CLASS)
    email = models.EmailField(unique=True, null=True)
    address = models.CharField(max_length=255)
    birthday = models.DateField()
    gender = models.CharField(max_length=2, 
                              choices=SEX_TYPE_CHOICE, 
                              default=PREFER_NOT_TO_SAY_TYPE)


#Database Model for Courses

class Course(models.Model):

    course_choice = [
        ('ENG', 'English Language'),
        ('MTS', 'Mathematics'),
         ('PHY', 'Physics'),
          ('CHEM', 'Chemistry'),
          ('BIO', 'Biology'),
         ('AGRIC', 'Agricultural Science'),
          ('ECON', 'Economics'),
          ('GOVT', 'Government'),
         ('CIVIC', 'Civic Education'),
          ('CRS', 'Christian Religious Studies'),
          ('IRK', 'Islamic Religious Studies'),
         ('LIT', 'Literature in English'),
          ('GEO', 'Geography'),
          ('HIST', 'History'),
          ('COMMC', 'Commerce'),
          ('ACCT', 'Accounting'),
         ('COMP', 'Computer Science'),
          ('FMST', 'Further Mathematics'),
          ('TD', 'Technical Drawing'),
         ('FART', 'Fine Arts'),
          ('MSC', 'Music'),
          ('FCH', 'French'),
         ('SPN', 'Spanish'),
          
    ]
    course_name = models.CharField(max_length=8, choices=course_choice)
    description = models.TextField(null=True)
    # instructor = models.OneToOneField('stafff')
    score = models.ManyToManyField('ComputerBaseTest',default=None)
    

class NewsAndEvent(models.Model):
    author = models.CharField(max_length=255)                              
    news_title = models.CharField(max_length=255)
    description = models.CharField(max_length=350)
    content = models.TextField()
    # image = models.ImageField()
    news_date = models.DateField()
    news_time = models.TimeField()

class ComputerBaseTest(models.Model):

    examination_type_choice = [
        ('E1', 'First Test'),
        ('E2', 'Second Test'),
        ('E3', 'Examination'),

    ]

    grade_choice = [
        ('A', 'Distinction'),
        ('B', 'Very Good'),
        ('C', 'Credit'),
        ('D', 'Pass'),
        ('E', 'Fair'),
        ('F', 'Fail'),    
    ]

    examination_name = models.CharField(max_length=255, choices=examination_type_choice, default=None)
    student = models.ManyToManyField(Student)
    test_date = models.DateField()
    grade = models.CharField(max_length=20, choices=grade_choice, default=None)
    score = models.IntegerField()

class AcedemicReport (models.Model):
    school_term_choice = [
        ('T1', 'First Term'),
        ('T2', 'Second Term'),
        ('T3', 'Third Term'),
    ]
    school_term = models.CharField(max_length=20, choices=school_term_choice, default='T1')
    report_date = models.DateField(auto_now_add=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, default=None)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, default=None)

class Alumni(models.Model):
    
    student = models.OneToOneField(Student, on_delete=models.PROTECT, default=None)
    phone_number = models.CharField(max_length=20)
    awards = models.TextField()
    graduation_year = models.DateField()
    current_occupation = models.CharField(max_length=255)
