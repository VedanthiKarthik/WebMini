from django.shortcuts import render
# from django.http import HttpResponse
from .models import Courses
# Create your views here.
# def add(request):
#     val1=int(request.POST['num1'])
#     val2=int(request.POST['num2'])
#     res=val1+val2
#     return render(request,'result.html',{'result':res})

def home(request):

    crs1 = Courses()
    crs1.title = 'Django project'
    crs1.rating = 5.0

    crs2 = Courses()
    crs2.title = 'React project'
    crs2.rating = 4.5

    crs3 = Courses()
    crs3.title = 'Angular project'
    crs3.rating = 4.0
    crs_list=[crs1,crs2,crs3]
    return render(request,'home.html',{'courses':crs_list})

