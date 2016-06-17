from wpsblog.models import Post
from django.views.generic.list import ListView


class PostListView(ListView):

    model = Post
    template_name = "posts/list.html"
    context_objects_name = "posts"

