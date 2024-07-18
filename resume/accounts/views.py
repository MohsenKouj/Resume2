from django.shortcuts import render

# Create your views here.
def login(req):
    return render(req, 'pages/login.html')

def signup(req):
    return render(req, 'pages/signup.html')