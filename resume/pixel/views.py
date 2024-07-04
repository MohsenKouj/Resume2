from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def house(req):
    return render(req,'index.html')

def resume(req):
    return render(req,'pages/resume.html')

def skills(req):
    return render(req,'pages/skills.html')

def projects(req):
    return render(req,'pages/projects.html')

def contact(req):
    return render(req,'pages/contact.html')


def testdb(req):
    from .models import Accounts
    acc = Accounts.objects.all()
    dic = {'accounts':acc}
    return render(req,'testdb.html',dic)

def blog(req):
    return render(req,'pages/blog.html')
def sin(req,number,number2,number3,acc):
    import math
    from .models import Accounts
    element = Accounts.objects.filter(id=acc)
    get_object_or_404(element)
    context = {'answer':math.sin(number),'answer2':math.cos(number2),'answer3':math.tan(number3)
               ,'obj':element[0]}
    return render(req,'testUD.htm',context)


