from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
#Authentication related views
def login_error_view(request):
    context = {}
    return render(request, 'contacts/login_error.html', context)

def login_view(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/contacts_list/')
                else:
                    return redirect('/login_error/')
            else:
                return redirect('/login_error/')
        else:
            return redirect('/login_error/')
    else:
        login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'contacts/login.html', context)

#Main application views
@login_required(login_url = '/')
def contacts_list_view(request):
    username = request.user.username
    context = {
        'username': username,
    }
    return render(request, 'contacts/contacts_list.html', context)
