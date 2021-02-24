from django import forms
from . import models


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "username", "first_name", "avatar", "bio"
        )

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    def clean_passwrord(self):
        password = self.cleaned_data.get("password")
        password1 = self.changed_data.get("password1")
        if password != password1 :
            raise forms.ValidationError("패스워드가 일치하지 않습니다.")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.save()