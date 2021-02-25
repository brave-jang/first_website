from django import forms
from . import models


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("패스워드가 틀립니다."))
        except models.User.DoesNotExist:
            self.add_error("password", forms.ValidationError("아이디가 존재하지 않습니다."))



class SignupForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "username", "nickname", "avatar", "bio"
        )

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            models.User.objects.get(username=username)
            raise forms.ValidationError("해당 아이디는 이미 존재합니다.")
        except models.User.DoesNotExist:
            return username

    
    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")
        try:
            models.User.objects.get(nickname=nickname)
            raise forms.ValidationError("해당 닉네임 이미 존재합니다.")
        except models.User.DoesNotExist:
            return nickname


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