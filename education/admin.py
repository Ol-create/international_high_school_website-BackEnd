from django.contrib import admin
from .models import Student, Course, NewsAndEvent, ComputerBaseTest, AcedemicReport, Alumni


# Register your models here.
admin.site.site_header = 'International School Administration'

# admin.site.register(Student)
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'discipline', 'class_level', 'gender']
    ordering = ['first_name']
    list_filter = ['discipline', 'class_level', 'gender']
    list_per_page = 15
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    def full_name(self, student:Student):
        return f'{student.first_name} {student.last_name}'

@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ['get_student_name', 
                    'get_student_email',
                    'phone_number', 
                    'current_occupation',
                    ]
    
    list_per_page = 20

    list_filter = ['current_occupation','graduation_year',]

    def get_student_name(self, obj):
        return f'{obj.student.first_name} {obj.student.last_name}'

    get_student_name.short_description = 'Student Name'

    def get_student_email(self, obj):
        return obj.student.email
    
    get_student_email.short_description = 'Student Email'

    
   
# Course Admin
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name'] # Customize the list of fields displayed in the list view
    list_filter = ['course_name'] # Add filters to the list view
    search_fields = ('course_name',)

    
admin.site.register(AcedemicReport)

# ComputerBaseTest
class ComputerBaseTestAdmin(admin.ModelAdmin):
    list_display = ['examination_name', 'test_date', 'score', 'grade'] # Customize the list of fields displayed in the list view
    list_filter = ['examination_name','test_date'] # Add filters to the list view
    search_fields = ('examination_name',)

admin.site.register(ComputerBaseTest, ComputerBaseTestAdmin) # Register the CBT model with the admin site
