import time

from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from blog.models import Blog


@cache_page(5 * 60)
def blog_view(request, blog_id: int):
    time.sleep(3)
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "blog.html", {"blog": blog})