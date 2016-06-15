from django.shortcuts import render
from django.core.paginator import Paginator

from wpsblog.models import Post

def list(request):
    page = request.GET.get("page",1)
    previous_page = int(page) - 1
    next_page = int(page) + 1
    per = request.GET.get("per", 5)

    paginator = Paginator(Post.objects.public(), per)
    posts = paginator.page(page)

    return render(
            request,
            "posts/list.html",
            {
                "posts": posts,
                "previous_page":previous_page,
                "next_page":next_page,
            },
        )

