from django.shortcuts import render

from wpsblog.models import Post


def edit(request, post_id):
    return render(
            request,
            "edit.html",
            {
                "post": Post.objects.get(id=post_id)
            }
        )
