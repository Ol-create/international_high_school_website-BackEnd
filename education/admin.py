from django.contrib import admin
from .models import Student, Course, NewsAndEvent, ComputerBaseTest, AcedemicReport, Alumni


# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(NewsAndEvent)
# admin.site.register(ComputerBaseTest)
admin.site.register(AcedemicReport)
admin.site.register(Alumni)

# ComputerBaseTest
class ComputerBaseTestAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'test_time', 'test_date', 'score'] # Customize the list of fields displayed in the list view
    list_filter = ['course__course_name','test_date', 'score'] # Add filters to the list view

admin.site.register(ComputerBaseTest, ComputerBaseTestAdmin) # Register the CBT model with the admin site
