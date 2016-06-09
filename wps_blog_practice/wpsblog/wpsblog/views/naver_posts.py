from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_posts_list(requests):
    keyword = request.GET.get("keyword")
    query = reqeust.GET.get("query")
    naver_posts = NaverPost.objects.all()

    if keyword:
        naver_posts = naver_posts.filter(keyword=keyword)
    
    if query:
        naver_posts = naver_posts.filter(title__contains=query)
    
    return render(
        request,
        "naver_posts/list.html",
        {
            "keyword" : keyword,
            "query" : query,
            "naver_posts": naver_posts,
        },
    )
