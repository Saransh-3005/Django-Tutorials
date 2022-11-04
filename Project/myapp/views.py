from itertools import count
from django.shortcuts import render,redirect
import django.http 
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Feature
# Create your views here.

def index (request):
    features=Feature.objects.all()
    return render(request , 'index.html', {'features':features})


def counter(request):
     return render(request,'counter.html')

def result(request):
    word=request.POST['text1']
    count=len(word.split())
    return render(request,'result.html',{"word":count})

def blog(request):
    return render (request, 'blog.html')

def weather(request):
    return render(request,'weather.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user != None:
            auth.login(request,user)
            messages.info(request,"Credientials  valid")
            return redirect('index')
        else:
            messages.info(request,"Credientials not valid")
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        name=request.POST['username']
        email =request.POST['email']
        passsword = request.POST['password1']
        pass2 =request.POST['cnfpassword1']
        if passsword==pass2:
            if User.objects.filter(username=name).exists():
                messages.info(request,"Choose another username")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already registered")
            else:
                user = User.objects.create_user(username=name,email=email,password=passsword)
                user.save()
                return redirect('login')
                
        else:
            messages.info(request,"Password is not same")
            
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')