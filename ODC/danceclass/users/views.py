from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate

from .form import *
from .models import *


# Create your views here.
#landing page
def home(request):
    return render(request, 'landing_page/home.html')

def signup(request):
    return render(request, 'landing_page/signup.html')

# registration for user
def userSignup(request):
    form = UserForm()

    if request.method == 'POST': # If the form has been submitted...
        form = UserForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save()
            print("Registered User")
            return redirect('/login')

    context = {'form' : form}
    return render(request, 'user/user_signup.html', context)


# login user
def login(request):
    user = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("logged in")

            get_registered = Users.objects.filter(user_id=user.id).values()


            for registered in get_registered:
                if registered['user_id'] == user.id:
                    print("registered Dashboard")
                    break
                
            if user.is_superuser == True:
                print("This is admin dashboard")
                return redirect('/admin-panel')
        else:
            error_msg = "Invalid Username or Password"
            context = {
                "error_msg": error_msg
            }
            return render(request, 'landing_page/login.html', context)

    return render(request, 'landing_page/login.html')


def adminDashboard(request):
    is_admin = True
    count_users = Users.objects.all().count()

    context = {
        'total_users' : count_users,
        'is_admin' : is_admin
    }

    return render(request, 'user/admin/dashboard.html', context)

def blog(request):
    return render(request, 'landing_page/blog.html')

def blogtitle(request):
    return render(request, 'blog/blogtitle.html')

def blogtitle1(request):
    return render(request, 'blog/blogtitle1.html')


def logout(request):
    return render(request, 'user/user_logout.html')