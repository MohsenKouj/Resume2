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
from PersianEncode import DictOvPer as dop
import random as r

email_ = ""
absnumb = ""
fname = ""

class ops:
    non = False
    _blank = False
    tuser = False
# Create your views here.
do = False
sendmail = False
def new_pass(req):
    global do,fname,absnumb,email_
    if do:
        if req.POST:
            if req.POST["password"] == req.POST["password2"]:
                user = User.objects.get(username=ops.tuser)
                suser = users.objects.get(username=ops.tuser)
                user.delete()
                User.objects.create_user(username=suser.username, password=req.POST["password"], email=suser.email)
                suser.password = user.password
                suser.save()
                messages.add_message(req,messages.SUCCESS,"گذرواژه موقتی شما ارسال شد")
                do = False
                return HttpResponseRedirect(reverse('pixel:house'))
        
                
        return render(req,'pages/new_password.html',{'do':do})
    else:
        if req.POST:
            person = False
            #try:
            if int(req.POST['att']) == 1:
                profill = req.POST['available']
                person = User.objects.get(username=profill)
            elif int(req.POST['att']) == 2:
                profill = req.POST['available']
                person = users.objects.get(tellNumber=profill)
            #except:
             
             #   ''
            if person:
                email_ = person.email
                fname='کاربر'
                ops._blank = True
                ops.non = True
                ops.tuser = person
                messages.add_message(req,messages.INFO,"گذرواژه موقتی شما ارسال شد")
                return HttpResponseRedirect(reverse('accounts:send-email'))
                
            else:
                messages.add_message(req,messages.ERROR,"شخصی با این مشخصات یافت نشد")
                
            
        
        
    return render(req,'pages/new_password.html',{'do':do})
    

def login(req):
    if not req.user.is_authenticated:
        if req.POST:                                                                 
            
            password = req.POST.get('password')
            if req.POST.get('enter-mode') == '1': 
                username = req.POST.get('username')
                user = authenticate(username=username, password=password)
                if user is not None:                              
                    log(request=req,user=user)                                              
                    messages.add_message(req,messages.SUCCESS,"خوش آمدید")                 
                    return HttpResponseRedirect('/')                                    
                else:
                    messages.add_message(req,messages.ERROR,"مشخصات ورودی اشتباه است") 
            if req.POST.get('enter-mode') == '2':
                email = req.POST.get('email')
                user = User.objects.get(email=email)
                user = authenticate(username=user.username,password=req.POST.get('password')) 
                if user is not None:                              
                    log(request=req,user=user)                                              
                    messages.add_message(req,messages.SUCCESS,"خوش آمدید")                 
                    return HttpResponseRedirect('/')                                    
                else:
                    messages.add_message(req,messages.ERROR,"مشخصات ورودی اشتباه است") 
        return render(req,'pages/login.html')
           
    else:
        return HttpResponseRedirect(reverse('pixel:house'))

        


cap = sinupForm()
def signup(req):
    if not req.user.is_authenticated:
    
        global email_,absnumb,fname,cap
        msg = ''
        type_data = ''
        if req.POST:
            cap = sinupForm(data=req.POST)
            if cap.is_valid():
                password = cap.cleaned_data['password']
                type_data = type(cap.cleaned_data['username'])
                if password == cap.cleaned_data['password2']:
                    if cap.cleaned_data['tellnumber'].isdigit() and cap.cleaned_data['tellnumber'].__len__()  == 11:
                        ops.non = True
                        email_ = cap.cleaned_data['email']                        
                        fname = req.POST['fname']
                        messages.add_message(req,messages.INFO,"ایمیل تایید شما ارسال شد")
                        ops._blank = False
                        return HttpResponseRedirect(reverse('accounts:send-email'))
                    else:
                        messages.add_message(req,messages.ERROR,"شماره تلفن وارده اشتباه است")
                else:
                    messages.add_message(req,messages.ERROR,"گذرواژه ها برابر نیست")
            else:
                messages.add_message(req,messages.ERROR,"خطا در داده های وارد شده")
                
        return render(req, 'pages/signup.html',{'captcha':cap,'msg':msg,'type':type_data})
    else:
        return HttpResponseRedirect(reverse('pixel:house'))


@login_required
def logout(req):
    if req.user.is_authenticated:
        logt(req)
    return redirect('/')

def send_email(req):
    if ops.non:
        global email_,fname,absnumb
        absnumb = r.randint(100000,999999)
        context = {'fname':fname, 'absnumb':absnumb,'blank':ops._blank}
        html =  render_to_string(
        template_name="pages/email_window.html",
        context=context
        )
        sm(
            f"گذرواژه موقتی '{fname}'",
            "",
            settings.EMAIL_HOST_USER,
            [email_],
            fail_silently=False,
            html_message=html
        )
        return HttpResponseRedirect(reverse('accounts:e-code'))
    else:
        return HttpResponseRedirect(reverse('pixel:house'))
def non_space(text:str):
    letters = []
    text_split = list(text.split('%'))
    for l in text_split:
        if l != '{Sp01}':
            letters.append(l)
    return '%'.join(letters)
def enter_code_signup(req):
    global absnumb,cap,do
    if ops.non:
        if req.POST:
            try:
                int(req.POST.get('code'))
            except:
                messages.add_message(req,messages.ERROR,"گذرواژه موقتی اشتباه میباشد")
                return render(req,'pages/enterCode.html')
            if int(req.POST.get('code')) == absnumb:
                if ops._blank:
                    absnumb = ''
                    ops.non = False
                    do = True
                    return HttpResponseRedirect(reverse("accounts:newpass"))
                else:
                    absnumb = ''
                    ops.non = False
                    if cap.is_valid():
                        dops =  dop()
                        User.objects.create_user(username=cap.cleaned_data['username'],password=cap.cleaned_data['password'],email=cap.cleaned_data['email'],
                            )
                        users.objects.create(
                            username=cap.cleaned_data['username'],
                            password=User.objects.get(username=cap.cleaned_data['username']).password,
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
                            code_name_f = non_space(dops.Encode(cap.cleaned_data['fname'])),
                            code_name_l = non_space(dops.Encode(cap.cleaned_data['lname'])),
                            age=1
                        )
                        user = authenticate(request=req,username=cap.cleaned_data['username'], password=cap.cleaned_data['password']) 
                        log(request=req,user=user)
                        messages.add_message(req,messages.SUCCESS,f"{fname} جان خوش‌آمدید!")
                        return HttpResponseRedirect(reverse('pixel:house'))
                    else:
                        messages.add_message(request=req,level=messages.ERROR,message="خطا در مشخصات ورودی")
            else:
                messages.add_message(req,messages.ERROR,"گذرواژه موقتی اشتباه میباشد")
        return render(req,'pages/enterCode.html')
    else:
        return HttpResponseRedirect(reverse('pixel:house'))
    
    

