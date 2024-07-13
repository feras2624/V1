from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth,messages
def login(request):
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=auth.authenticate(email=email,password=password)
        print(email,"   ",password,"    ",user)
        if user is not None:
            messages.success(request,"Wellcome")
        else:
            messages.error(request,"Invalid Email or Password",extra_tags="danger")
        return render(request,"users/index.html")
    else:
        return render(request,"users/index.html")