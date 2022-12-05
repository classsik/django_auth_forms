from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import *


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if email == 'User1' and password == '12345678':
                return HttpResponse('Поздравляю с успешным входом')
            else:
                return redirect('register')

    return render(request, 'main/login.html', {"form": form})


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            return HttpResponse(f"""{name}, поздравляю с регистрацией!
                                    Указанные вами данные: Имя - {name}, Email - {email}, Пароль - {password}""")

    return render(request, 'main/register.html', {'form': form})
