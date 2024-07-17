from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["pixel:house", "pixel:resume", "pixel:contact"]

    def location(self, item):
        return reverse(item)
    
from django.contrib.sitemaps import Sitemap
from .models import posts

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return posts.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.p_date