from email.policy import HTTP
import http
from tkinter import Variable
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Course
from .serializer import CourserSerializer


# Create your views here.

def Welcome (request : HttpRequest):
    name = {'name': 'Wojod'}
    return render(request, 'courses/index.html', name  ) 

def course_info(request : HttpRequest):
    course = Course.objects.all()
    return render(request, 'courses/courses.html', {'course' : course, 'name': 'Wojod'})