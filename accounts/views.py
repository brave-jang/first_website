from django.contrib.auth import authenticate, login
from django.urls.base import reverse_lazy
from django.views.generic import FormView
from . import models, forms


class UserLoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy("posts:home")



class SignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = forms.SignupForm
    success_url = reverse_lazy("posts:home")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)