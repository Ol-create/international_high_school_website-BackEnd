from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_victor),
    path('create_student/', views.create_student),
]
