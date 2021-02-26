from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields = ["post_url", "content", "content_img", "comment", "country","category"]
        widgets = {
            "post_url" : forms.URLInput(),
            "category" : forms.CheckboxSelectMultiple()
        }


class CreatePostsForm(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields = ["post_url", "content", "content_img", "comment", "country","category"]
        widgets = {
            "post_url" : forms.URLInput(),
            "category" : forms.CheckboxSelectMultiple()
        }

    def save(self, *args, **kwargs):
        post = super().save(commit=False)
        return post