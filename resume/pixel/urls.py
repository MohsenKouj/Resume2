from django.urls import path
from pixel.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',house,name='house'),
    path('resume/',resume,name='resume'),
    path('skills/',skills_,name='skills'),
    path('projects/',projects_,name='projects'),
    path('contact/',contact_,name='contact'),
    path('blog/',blog,name='blog'),
    path('single/<int:post>',single,name='single'),
    path('blog/sort-by-category<str:name><int:typ>',blog,name='blogs'),
    path('blog/sort-by-author<str:p><int:typ>',blog,name='blogsn'),
    path('sendComment/<int:pos>',sendComment,name='sendComment'),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
