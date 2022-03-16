from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from blog.models import Post

class LastestPostFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.order_by('-updated')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 10)