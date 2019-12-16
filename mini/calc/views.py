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

    crs_list=Courses.objects.all()[::-1]
    cre=crs_list[:4]
    return render(request,'home.html',{'courses':cre})

