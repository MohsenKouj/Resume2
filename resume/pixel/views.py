from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def house(req):
    el = users.objects.get(id=1)
    return render(req,'index.html',{'user':el})

def resume(req):
    el = cards.objects.all()
    return render(req,'pages/resume.html',{'cards':el})

def skills_(req):
    el = skills.objects.all()
    return render(req,'pages/skills.html',{'skills':el})

def projects_(req):
    el = projects.objects.all()
    return render(req,'pages/projects.html',{'projects':el})

def contact_(req):
    el = users.objects.get(id=1)
    smstr = ""
    smstr.encode('utf-8')
    smstr = smstr.replace("","پیام شما ارسال شد")
    if req.POST:
        return HttpResponse('<script>alert("{}");location.href="/contact"</script>'.format(smstr))
    return render(req,'pages/contact.html',{'user':el})


def testdb(req):
    from .models import Accounts
    acc = Accounts.objects.all()
    dic = {'accounts':acc}
    return render(req,'testdb.html',dic)

def blog(req):
    el = posts.objects.all()
    return render(req,'pages/blog.html',{'posts':el})
def sin(req,number,number2,number3,acc):
    import math
    from .models import Accounts
    element = Accounts.objects.filter(id=acc)
    get_object_or_404(element)
    context = {'answer':math.sin(number),'answer2':math.cos(number2),'answer3':math.tan(number3)
               ,'obj':element[0]}
    return render(req,'testUD.htm',context)

def single(req,post):
        p = posts.objects.get(id=post)
        ps = posts.objects.all().order_by('p_date')[:6]
        return render(req,'pages/single.html',{'post':p,'recently':ps})