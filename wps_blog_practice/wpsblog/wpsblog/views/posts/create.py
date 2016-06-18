from django.shortcuts import redirect
from wpsblog.models import Post

from .base import PostBaseView
from django.views.generic.edit import CreateView


class PostCreateView(PostBaseView, CreateView):


    fields = [
            "title",
            "content",
            "image",
        ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


