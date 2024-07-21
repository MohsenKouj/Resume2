from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as log,logout as logt
from django.contrib.auth.models import User
from pixel.models import users
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
def login(req):
    if req.POST:                                                                 
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(request=req,username=username, password=password) 
        if user is not None:                              
            log(request=req,user=user)                                              
            messages.add_message(req,messages.SUCCESS,"خوش آمدید")                 
            return HttpResponseRedirect('/')                                    
        else:
            messages.add_message(req,messages.ERROR,"مشخصات ورودی اشتباه است")                              
        
    return render(req,'pages/login.html',)


def signup(req):
    cap = sinupForm()
    msg = ''
    if req.POST:
        cap = sinupForm(data=req.POST)
        if cap.is_valid():
            username = cap.cleaned_data('username')
            password = cap.cleaned_data('password')
            if password == cap.cleaned_data('password2'):
                User.objects.create_user(username,password)
                  
            
    return render(req, 'pages/signup.html',{'captcha':cap,'msg':msg})

@login_required
def logout(req):
    if req.user.is_authenticated:
        logt(req)
    return redirect('/')