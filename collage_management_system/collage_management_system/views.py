from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from collage_management_app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from collage_management_app.models import CustomUser


def base_view(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


def dologin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                # Handle unexpected user types here
                return HttpResponse('Unknown user type')
        else:
            messages.error(request, 'Email and password Are Invalid')
            return redirect('login')
    else:
        messages.error(request, 'Email and password Are Invalid')
        return redirect('login')


def dologout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user,
    }

    return render(request, 'profile.html', context)


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            if password:  # You can directly check if password is truthy
                customuser.set_password(password)

            if profile_pic:  # Similarly, check if profile_pic is provided
                customuser.profile_pic = profile_pic

            customuser.save()
            messages.success(request, 'Your profile updated successfully!')
            return redirect('profile')  # You need to return the redirect response
        except CustomUser.DoesNotExist:
            messages.error(request, 'Failed to update your profile')

    return render(request, 'profile.html')


def home_view(request ):

 return render(request, 'home.html')