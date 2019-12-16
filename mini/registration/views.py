from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def registration(request):

    if request.method == 'POST':                      # check if it is get or post request
        name             = request.POST['name']
        email            = request.POST['email']
        password         = request.POST['pass']
        confirm_password = request.POST['re_pass']
        if password==confirm_password:
            if User.objects.filter(username=name).exists():
                messages.info(request,'Username already exist')
                return redirect('registration')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exist')
                return redirect('registration')

            else:
                user=User.objects.create_user(username=name,password=password,email=email)
                user.save()
            return redirect('/')
        else:
            messages.info(request,"Password don't match")
            return redirect('registration')

    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'User doesnot exist')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


    