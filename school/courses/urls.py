from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',views.Welcome, name="welcome"),
    path('course_info/',views.course_info, name="course_info"),
    
    
]
