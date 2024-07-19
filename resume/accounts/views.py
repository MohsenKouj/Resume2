from django.shortcuts import render
from .forms import *
# Create your views here.
def login(req):
    return render(req, 'pages/login.html')

def signup(req):
    cap = captcha()
    return render(req, 'pages/signup.html',{'captcha':cap})