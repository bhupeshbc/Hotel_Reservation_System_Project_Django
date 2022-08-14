from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
import rooms

def register(request):
    print(request.method)
    if request.method =='POST':
        User.objects.create_user(
            firstname=request.POST['First Name'],
            last_name=request.POST['Last Name'],
            email=request.POST['Email'],
            password=request.POST['Password'],
   
        )
        return redirect('login')
        
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
   
        user=authenticate(request, 
        username =request.POST.get('username'),
        password =request.POST.get('password')
        )
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('login')
        
    else:
        return render(request, 'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login')

# def login(request):
#     return render(request, "login.html")


# def register(request):
#     return render(request, "register.html")

# from django.shortcuts import  render, redirect
# from .forms import User
# from django.contrib.auth import login
# from django.contrib import messages

# def register(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("main:homepage")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="main/register.html", context={"register_form":form})