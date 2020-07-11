from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
@csrf_protect
def login(request):   
    return(render(request,'accounts/login.html'))

@csrf_protect
def signup(request):
    if(request.method =='POST'):
        if(request.POST['password']==request.POST['confirmpassword']):
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'Username hass already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'Password must match'})

    else:     
        return(render(request,'accounts/signup.html'))    

def logout(request):
    if(request.method =='POST'):
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            render(request,'accounts/login.html',{'error':'Username or Password is wrong'})
    else:    
        return(render(request,'accounts/logout.html'))