from django.shortcuts import render
from djangolevelfive_app.forms import UserForm,Userprofileinfo_form
# Create your views here.
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout


def index(request):
    return render(request,'djangolevelfive_app/index.html',context={})

@login_required
def user_logout(request):
    logout(request)
    return render(request,'djangolevelfive_app/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = Userprofileinfo_form(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = Userprofileinfo_form()

    return render(request,'djangolevelfive_app/register.html',{'registered':registered,
                                                                'user_form':user_form,
                                                                'profile_form':profile_form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("login failed.. Username : {} and password : {}".format(username,password))
            return HttpResponse("invalid credentials")
    else:
        return render(request,'djangolevelfive_app/login.html',{})
