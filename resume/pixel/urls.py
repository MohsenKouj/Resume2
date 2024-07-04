from django.urls import path
from pixel.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',house,name='house'),
    path('resume/',resume,name='resume'),
    path('skills/',skills,name='skills'),
    path('projects/',projects,name='projects'),
    path('contact/',contact,name='contact'),
    path('blog/',blog,name='blog'),   
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
