
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

def home(request):
    return render(request,'index.html')
 

def signup(request):

    
   if request.method == 'POST':
         username=request.POST['username']
         firstname=request.POST['firstname']
         lastname=request.POST['lastname']
         email=request.POST['email']
         pass1=request.POST['password']
         pass2=request.POST['confpassword']
       
    

        #  username=request.POST.get('username')
       

         myuser=User.objects.create_user(username,email,pass1)
         myuser.first_name=firstname
         myuser.last_name=lastname

         myuser.save()

         messages.success(request,'User Created Successfully')
         return redirect('signin')

    
   return render(request,'signup.html')
# user messages
   

def signin(request):

    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['password']

        user= authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return  render(request,'index.html',{'fname':fname})

        else:
            messages.error(request,'Invalid Credentials')
            return redirect('signup')

    return render(request,'signin.html')

def signout(request):
    return render(request,'signout.html')

