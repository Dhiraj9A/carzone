from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.

                        #...............................login.............................#
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None: 
            auth.login(request, user)
            messages.success(request,'you are now logged in.')
            return redirect("dashboard")   
        else: 
            messages.error(request,'Invalid login Credentails ')
            return redirect("login")
    else:
        return render(request,'accounts/login.html')
    
                    #...............................Register.............................#
def register(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists(): 
                messages.error(request,'username already exists ')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exists ')
                    return redirect('register')
                else:
                    new_user = User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email, password=password)
                    auth.login(request,new_user)
                    messages.success(request,'you are now logged in.')
                    new_user.save()
                    messages.success(request,'you are registered successfully')
                    redirect('login')
        else:
            messages.error(request,'password do not match')
            print('this is post method')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

                    #...............................Dashboard.............................#
def dashboard(request):
    return render(request,'accounts/dashboard.html')

                    #...............................logout.............................#

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'you are successfully logged out')
        return redirect('home')
    
    return redirect('home')



