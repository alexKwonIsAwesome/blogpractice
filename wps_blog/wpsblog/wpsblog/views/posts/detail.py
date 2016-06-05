from django.shortcuts import rende


def list(requets):
    return render(
            request,
            "posts/list.html",

            {},
        )
