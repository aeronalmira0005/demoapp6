from django.forms.widgets import PasswordInput
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from mysite.forms import entryForms

def index(request):
    return render(request, "pages/home.html")

def view_login(request):
    if request.user.is_authenticated:
        return redirect("userpage")
    else:
        forms = entryForms()
        if request.method == "POST":
            input_username = request.POST.get("input_username")
            input_password = request.POST.get("input_password")
            user = authenticate(username=input_username, password=input_password)
            if user is not None:
                login(request, user)
                return redirect('userpage')
            else:
                data = {
                    'forms': forms,
                    'message': 'Invalid Username or Password.',
                }
                return render(request, "pages/login.html", data)

        data = {
            'forms': forms,
        }
        return render(request, "pages/login.html", data)

def register(request):
    forms = entryForms()
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if(password1 != password2):
            data = {
                'forms': forms,
                'message': 'Password do not match',
            }
            return render(request, "pages/register.html", data) 
        elif(User.objects.filter(username=username).exists()):
            data = {
                'forms': forms,
                'message': 'Username already exists.',
            }
        else:
            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('login')

    data = {
        'forms': forms,
    }
    return render(request, "pages/register.html", data)

def userpage(request):
    user_data = User.objects.filter(username=request.user)
    data = {
        'data': user_data,
    }
    return render(request, "pages/userpage.html", data)

def view_logout(request):
    logout(request)
    return redirect('login')