from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from contacts.models import Contact
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lName']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        username=request.POST['username']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"This username has been taken")
                return redirect('register')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'This email is already being used')
                    return redirect('register')
                else:
                    messages.success(request,f'Finally able to create {first_name}')
                    user=User.objects.create_user(username=username,email=email,password=pass1,first_name=first_name,last_name=last_name)
                    # login after registration
                    # messages.success(request, 'You are logged in')
                    # auth.login(request,user)
                    
                    user.save();
                    messages.success(request,' You are now registered and can log in')
                    return redirect('login')

                    # return redirect('index')
        else:
            messages.error(request,"Password doesn't match")
            return render(request,'accounts/register.html')

    else:
        return render(request,'accounts/register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            return redirect('dashboard') 
        else:
            messages.error(request,'Username or password is incorrect')
            return redirect('login')
            
    else:
        return render(request,'accounts/login.html')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        # messages.success(request,'You are now logged out')
        return redirect('index')

def dashboard(request):
    user_contacts=Contact.objects.order_by('-dated').filter(user_id=request.user.id)
    context={
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)