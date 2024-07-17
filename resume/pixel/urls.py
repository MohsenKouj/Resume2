from django.urls import path,include
from pixel.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from pixel import sitemaps

from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import StaticViewSitemap,BlogSitemap
from . import views


sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}
app_name = 'pixel'
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
    path('sendComment/<int:post>',single,name='sendComment'),
    
    path('sitemaps.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    
    path('robots.txt', include('robots.urls')),
    path('captcha/', include('captcha.urls')),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)