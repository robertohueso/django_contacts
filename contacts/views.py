from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, NewContactForm
from .models import Contact
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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

def register_view(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            repeat_password = request.POST['repeat_password']
            if (password == repeat_password) and (password is not None) and not (User.objects.filter(username=username).exists()):
                user = User.objects.create_user(username, None, password)
                if user is not None:
                    user.save()
                    return redirect('/')
                else:
                    return redirect('/login_error/')
            else:
                return redirect('/register/')
        else:
            return redirect('/register/')
    else:
        register_form = RegisterForm()
    context = {
        'register_form': register_form,
    }
    return render(request, 'contacts/register.html', context)

#Main application views
@login_required(login_url = '/')
def contacts_list_view(request):
    user_id = request.user.id
    list_of_contacts = Contact.objects.filter(user_id = user_id)
    context = {
        'list_of_contacts': list_of_contacts,
    }
    return render(request, 'contacts/contacts_list.html', context)

@login_required(login_url = '/')
def add_contact_view(request):
    if request.method == "POST":
        new_contact_form = NewContactForm(request.POST)
        if new_contact_form.is_valid():
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            phone = request.POST['phone']
            user_id = request.user
            new_contact = Contact(firstname = firstname, lastname = lastname, phone = phone, user_id = user_id)
            new_contact.save()
            return redirect('/contacts_list/')
    else:
        new_contact_form = NewContactForm()
    context = {
        'new_contact_form': new_contact_form,
    }
    return render(request, 'contacts/add_contact_modal.html', context)
