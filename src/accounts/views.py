from django.shortcuts import render, reverse
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    if request.method == 'POST':
        # form = SignupForm(request.POST)
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            # return HttpResponseRedirect(reverse('_articles:list'))
        # signup_form = UserCreationForm()
        return render(request, 'accounts/signup.html',
                      {'signupForm': signup_form})

    else:
        signup_form = SignupForm()
        return render(request, 'accounts/signup.html',
                      {'signupForm': signup_form})
