from django.urls import path
from . import views

urlpatterns = [
    path('alumni/', views.alumni_list),
    path('students/', views.student_list),
    path('students/<int:id>', views.student_detail),

]