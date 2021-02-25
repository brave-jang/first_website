from django import forms
from django.forms import widgets
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields = ["post_url", "content", "content_img", "comment", "country", "category",]
        widgets = {
            "post_url" : forms.URLInput(),
            "category" : forms.CheckboxSelectMultiple()
        }