from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list),
    path('students/<int:id>', views.student_detail),
]