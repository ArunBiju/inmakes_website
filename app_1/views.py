from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import home_page_db_1, home_page_db_2
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_protect
# Create your views here.


def home(request):

    places = home_page_db_1.objects.all()
    ceo = home_page_db_2.objects.all()
    return render(request, "app_1/index.html", {'places': places, 'ceo': ceo})

@csrf_protect
def registration(request):

    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail taken')
            else:
                new_user = User.objects.create_user(
                username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                messages.info(request, 'User Created, Log in to Continue')
                return render(request, r'app_1/sign_in.html')

        else:
            messages.info(request,'Passwords Did Not Match')
            return render(request, r'app_1/registration.html')
            
    return render(request, r'app_1/registration.html')
       
@csrf_protect
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
           auth.login(request, user)
           return redirect('/')

        else:
            messages.info(request,'Invalid Credentials')
            return render(request, r'app_1/sign_in')
            
    return render(request, 'app_1/sign_in.html')

def logout(request):
    auth.logout(request)
    return redirect('/')