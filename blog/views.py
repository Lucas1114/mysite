from django.shortcuts import render
from datetime import date
# Create your views here.
all_posts=[
    {
        "slug":"hike-in-the-mountains1",
        "image":"mountains.jpg",
        "author":"Maximilian",
        "date": date(2021,7,21),
        "title": "Mountain Hiking1",
        "excerpt": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "content": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    },
    {
        "slug": "hike-in-the-mountains2",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 9, 21),
        "title": "Mountain Hiking2",
        "excerpt": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "content": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    },
    {
        "slug": "hike-in-the-mountains3",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2022, 7, 21),
        "title": "Mountain Hiking3",
        "excerpt": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "content": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    },
    {
        "slug": "hike-in-the-mountains4",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2022, 10, 21),
        "title": "Mountain Hiking4",
        "excerpt": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "content": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    },
]

def get_date(post):
    return post.get('date')

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts": latest_posts,
    })

def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts
    })


def post_detail(request,slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/post-detail.html",{
        "post": identified_post
    })