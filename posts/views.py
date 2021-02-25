from django.shortcuts import redirect, render
from . import forms


def posts(request):
    return render(request, "posts/posts_list.html")


def post_write(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("posts:home")
    else:
        form = forms.PostForm()
    
    return render(request, "posts/posts_write.html", {'forms':form})