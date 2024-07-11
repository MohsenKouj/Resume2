from django import template
from pixel.models import *
from django.utils import timezone
register = template.Library()

@register.inclusion_tag('pages/inc.html')
def latest_post():
    now = timezone.datetime.now()
    ps = posts.objects.filter(status=1).order_by('p_date')[:6]
    els = [i for i in ps if i.p_date.timestamp() < now.timestamp()]
    return {'posts':els}

@register.inclusion_tag('pages/categoris.html')
def categoris():
    pass