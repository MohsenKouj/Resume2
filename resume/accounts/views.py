from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as log,logout as logt
from django.contrib.auth.models import User
from pixel.models import users,Accounts as ac
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.mail import send_mail as sm
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
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

email_ = ""
absnumb = ""
fname = ""
def signup(req):
    global email_,absnumb,fname
    cap = sinupForm()
    msg = ''
    type_data = ''
    if req.POST:
        cap = sinupForm(data=req.POST)
        #if cap.is_valid():
        username = req.POST['username']
        password = req.POST['password']
        email_ = req.POST['email']
        import random as r
        absnumb = r.randint(100000,999999)
        fname = req.POST['fname']
        
        #type_data = type(cap.cleaned_data['username'])
        #if password == cap.cleaned_data['password2']:
                #if cap.cleaned_data['tellnumber'].isdigit():
        '''User.objects.create_user(username=username,password=password,email=cap.cleaned_data['email']
                                    ,)
        users.objects.create(
            username=username,
            password=User.objects.get(username=username),
            email=cap.cleaned_data['email'],
            fname=cap.cleaned_data['fname'],
            lname=cap.cleaned_data['lname'],
            codeacc = ac.objects.get(id=2),
            tellNumber=cap.cleaned_data['tellnumber'],
            location=cap.cleaned_data['location'],
            birthday=cap.cleaned_data['birthday'],
            about=cap.cleaned_data['subject'],
            education=cap.cleaned_data['education'],
            langs=cap.cleaned_data['langs'],
            t_p=cap.cleaned_data['t_p'],
            cod_posti=cap.cleaned_data['cod_posti'],
            age=1
            
        )
            '''
        return HttpResponseRedirect(reverse('accounts:send-email'))
                 
            
    return render(req, 'pages/signup.html',{'captcha':cap,'msg':msg,'type':type_data})

@login_required
def logout(req):
    if req.user.is_authenticated:
        logt(req)
    return redirect('/')

def send_email(req):
    global email_,fname,absnumb
    context = {'fname':fname, 'absnumb':absnumb}
    html =  render_to_string(
    template_name="pages/email_window.html",
    context=context
)
    sm(
        f"گذرواژه موقتی '{fname}'",
        f"سلام ♥{fname}♥ خوش آمدید<br>گذرواژه ورود شما: '{absnumb}'",
        settings.EMAIL_HOST_USER,
        [email_],
        fail_silently=False,
        html_message=html
    )
    return HttpResponse('<h1>success</h1>')