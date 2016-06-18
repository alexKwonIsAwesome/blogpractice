from wpsblog.models import Post
from django.views.generic import View


class PostBaseView(View):
    model = Post
