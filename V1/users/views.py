from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth,messages
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
def login_view(request):
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=auth.authenticate(email=email,password=password)
        print(email,"   ",password,"    ",user)
        if user is not None:
            login(request,user)
            return redirect('home_view')
        else:
            messages.error(request,"Invalid Email or Password",extra_tags="danger")
        return render(request,"users/index.html")
    else:
        return render(request,"users/index.html")

@login_required(login_url='login_view')
def home_view(request):
    return render(request,"users/home.html")

@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    messages.error(request,"You Were Logged Out",extra_tags="danger")
    return redirect("login_view")