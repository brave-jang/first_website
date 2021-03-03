import math
from django.http.response import Http404
import requests
from accounts import mixins
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
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
    paginator = Paginator(post_list, 12)
    page_number = request.GET.get('page', 1)
    post_list = paginator.get_page(page_number)

    count = 5
    end_page = paginator.count / 5

    if int(page_number) % count == 0:
        start = (int(int(page_number) / count) * count + 1) - count
        end = int(page_number)
    elif page_number == end_page:
        start = (int(int(page_number) / count) * count) +1
        end = end_page
    else:
        start = (int(int(page_number) / count) * count)
        end = (math.ceil(int(page_number) / count) * count) -1
    
    page_obj = paginator.page_range[start:end]
    return render(request, "posts/posts_list.html", {'post_list':post_list, 'page_obj':page_obj})


def posts_politics(request):
    post_list = models.Posts.objects.filter(category = '0')
    return render(request, "posts/posts_list.html", {'post_list':post_list})


class CreatePosts(mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreatePostsForm
    template_name = "posts/posts_write.html"

    def form_valid(self, form):
        post = form.save()
        post.user = self.request.user
        url = form.cleaned_data.get("post_url")
        post.title = title_crawling(url)[0]
        post.image = title_crawling(url)[1]
        post.save()
        form.save_m2m()
        messages.success(self.request, "작성 완료!")
        return redirect(reverse("posts:posts_detail", kwargs={"pk":post.pk}))


# @login_required
# def post_write(request):
#     if request.method == "POST":
#         form = forms.PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             url = form.cleaned_data.get("post_url")
#             post.title = title_crawling(url)[0]
#             post.save()
#             form.save_m2m()
#             return redirect("posts:home")
#     else:
#         form = forms.PostForm()
    
#     return render(request, "posts/posts_write.html", {'forms':form})


class PostDetail(DetailView):
    model = models.Posts
    template_name = 'posts/posts_detail.html'
    context_object_name = 'forms'


@login_required
def post_edit(request, pk):
    post = get_object_or_404(models.Posts, pk=pk)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid:
            post = form.save(commit=False)
            if post.user == request.user:
                url = form.cleaned_data.get("post_url")
                post.title = title_crawling(url)[0]
                post.save()
                form.save_m2m()
                return redirect("posts:posts_detail", pk=pk)
            else:
                raise Http404
    else:
        if post.user == request.user:
            form = forms.PostForm(instance=post)
        else:
            raise Http404

    return render(request, "posts/posts_edit.html", {'forms':form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(models.Posts, pk=pk)
    if post.user == request.user:
        post.delete()
        return redirect("posts:home")
    else:
        Http404
