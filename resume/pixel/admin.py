from django.contrib import admin
from .models import *
# Register your models here.
register = admin.site.register(users)
register = admin.site.register(cards)
register = admin.site.register(comments)
register = admin.site.register(pages)
register = admin.site.register(projects)
register = admin.site.register(skills)
register = admin.site.register(categorise)
register = admin.site.register(contact)
register = admin.site.register(Accounts)

from django_summernote.admin import SummernoteModelAdmin
from .models import posts

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('desc',)

admin.site.register(posts, PostAdmin)




