from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

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

def blog(req,name=None,p=None,typ=0):
    now = timezone.datetime.now()
    el = posts.objects.filter(status=True)
    if typ:
        if name:
            el = el.filter(category__name=name)
            els = [i for i in el if i.p_date.timestamp() < now.timestamp()]
        else:
            els = [i for i in el if i.p_date.timestamp() < now.timestamp()]
    else:
        if p:
            name = users.objects.get(username=p)
            name = f'{name.fname} {name.lname}'
            el = el.filter(uname__username=p)
            els = [i for i in el if i.p_date.timestamp() < now.timestamp()]
        else:
            els = [i for i in el if i.p_date.timestamp() < now.timestamp()]
    return render(req,'pages/blog.html',{'posts':els,'name':name,'typ':typ})

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
        now = timezone.datetime.now()
        if not p.status or p.p_date.timestamp() > now.timestamp():
            return HttpResponseNotFound(req)
        p.cview += 1
        p.save()
        com = comments.objects.filter(post__id=p.id)
        return render(req,'pages/single.html',{'post':p,'comments':com,'lengthc':len(com)})