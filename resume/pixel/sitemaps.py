from django.contrib.sitemaps import Sitemap
from .models import posts

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return posts.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.p_date