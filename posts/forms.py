from django import forms
from django.forms import widgets
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields = ["url", "content", "content_img", "comment", "country", "category",]
        widgets = {
            "category" : forms.CheckboxSelectMultiple()
        }