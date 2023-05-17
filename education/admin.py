from django.contrib import admin
from .models import Student, Course, NewsAndEvent, ComputerBaseTest, AcedemicReport, Alumni


# Register your models here.
admin.site.site_header = 'International School Administration'

# admin.site.register(Student)
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'discipline', 'class_level', 'gender']
    ordering = ['first_name']

    def full_name(self, student:Student):
        return f'{student.first_name} {student.last_name}'

@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ['get_student_name', 
                    'get_student_email',
                    'phone_number', 
                    'current_occupation'
                    ]
    
    list_per_page = 20

    def get_student_name(self, obj):
        return f'{obj.student.first_name} {obj.student.last_name}'

    get_student_name.short_description = 'Student Name'

    def get_student_email(self, obj):
        return obj.student.email
    
    get_student_email.short_description = 'Student Email'

admin.site.register(Course)
admin.site.register(AcedemicReport)

# ComputerBaseTest
class ComputerBaseTestAdmin(admin.ModelAdmin):
    list_display = ['examination_name', 'test_date', 'score', 'grade'] # Customize the list of fields displayed in the list view
    list_filter = ['course__course_name','test_date', 'score'] # Add filters to the list view

admin.site.register(ComputerBaseTest, ComputerBaseTestAdmin) # Register the CBT model with the admin site
