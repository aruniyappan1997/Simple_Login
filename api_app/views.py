from django.shortcuts import render, redirect, get_object_or_404
from .models import User_Details
from .forms import SigninForm, SignupForm, UpdateForm
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
# To avoid duplicate entries
from django.db import IntegrityError

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            mobile = form.cleaned_data["mobile"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]

            try:    
                if password == password2:
                    hashed_password = make_password(password)
                    User_Details.objects.create(first_name=first_name, last_name=last_name,email=email, mobile=mobile, password=hashed_password)
                    messages.success(request,"User Account Created Successfully")
                else:
                    messages.error(request,"Password and confirm password are not correct")
            except IntegrityError:
                messages.error(request, "User email Already Exists!")

        else:
            messages.info(request,"Please enter correct details")
    else:
        form = SignupForm()
    return render(request, "Signup.html", {"form":form})


def Signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                user = User_Details.objects.get(email=email)
                print(user.password)
                if check_password(password, user.password):
                    messages.success(request, "Logged in Successfully")
                    return redirect('home')
                else:
                    messages.error(request, "Password is not correct")
            except User_Details.DoesNotExist:
                messages.error(request, "User is not registered")
        else:
            messages.error(request, "Enter correct credentials")
    else:
        form = SigninForm()
    return render(request, "Signin.html", {'form': form})

def Home(request):
    Users = User_Details.objects.all()
    return render(request, "Home.html", {'Users':Users}) 

def Update(request, id):
    employee = get_object_or_404(User_Details, pk=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST or None, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "User Updated Successfully")
            return redirect('home')
        else:
            messages.error(request, "Check for errors in the form")
    else:
        form = UpdateForm(instance=employee)
    
    context = {
        'form': form,
        'employee': employee
    }
    return render(request, "update.html", context)

def Delete(request,id):
    user = User_Details.objects.get(pk=id)
    user.delete()
    messages.success(request, "User Deleted Successfully")
    return redirect('home')  