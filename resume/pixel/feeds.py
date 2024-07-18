from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import posts


class LatestEntriesFeed(Feed):
    title = "New posts"
    link = "/rss/feed"
    description = "new posts feed documentation"

    def items(self):
        return posts.objects.filter(status=True)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.desc[:20]