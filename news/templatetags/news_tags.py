from django import template
from news.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('news/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}

#@register.simple_tag(name='getposts')
#def get_posts(filter=None):
 #   if not filter:
#        return News.objects.all()
#    else:
#        return News.objects.filter(pk=filter)

##@register.inclusion_tag('news/list_posts.html')
#def show_posts(sort=None, cat_selected=0):
   # if not sort:
 #       posts = News.objects.all()
  #  else:
  #      posts = News.objects.order_by(sort)
  #  return {"posts": posts, "cat_selected": cat_selected}
