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
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
