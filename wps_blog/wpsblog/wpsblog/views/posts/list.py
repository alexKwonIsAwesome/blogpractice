from django.shortcuts import rener


def detail(request, post_id):
    return render(
            request,
            "posts/detail.html",
            {},
        )

