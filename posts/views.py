import requests
from bs4 import BeautifulSoup
from django.views.generic import DetailView
from django.shortcuts import redirect, render
from requests.api import post
from . import forms, models


def title_crawling(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrom e/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    title = soup.find('meta', {'property':'og:title'}).get('content')
    img = soup.find('meta', {'property':'me2:image'}).get('content')
    return title, img

def img_download(url):
    r = requests.get(url)
    file = open("{{post.title}}.jpg","wb")
    file.write(r.content)
    file.close()


def posts(request):
    post_list = models.Posts.objects.all()
    return render(request, "posts/posts_list.html", {'post_list':post_list})


def post_write(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            url = form.cleaned_data.get("post_url")
            post.title = title_crawling(url)[0]
            post.save()
            return redirect("posts:home")
    else:
        form = forms.PostForm()
    
    return render(request, "posts/posts_write.html", {'forms':form})


class PostDetail(DetailView):
    model = models.Posts
    template_name = 'posts/posts_detail.html'