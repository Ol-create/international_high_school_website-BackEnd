from django.contrib import admin
from .models import Student, Course, NewsAndEvent, ComputerBaseTest, AcedemicReport, Alumni


# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(NewsAndEvent)
admin.site.register(ComputerBaseTest)
admin.site.register(AcedemicReport)
admin.site.register(Alumni)
