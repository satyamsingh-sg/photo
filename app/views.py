from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import HotelForm,Cpt
from .models import historial, Comment
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from  django.contrib.auth.models import Group
def hotel_image_view(request): 
    if request.user.is_authenticated:
  
        if request.method == 'POST': 
            form = HotelForm(request.POST, request.FILES) 
    
            if form.is_valid(): 
                form.save() 
                form = HotelForm() 
        else: 
            form = HotelForm() 
        return render(request, 's1.html', {'fm' : form}) 

    else:
        return HttpResponseRedirect('/login/')
    



def Show(request):
    st=historial.objects.all()
    t=Comment.objects.all()
    

    return render(request, 's2.html',context={'hotel_images' : st ,'stp':t}) 
  



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'conguatualation ! You have Created account Successfully ')
            user=form.save()
            
            
            return HttpResponseRedirect('/')
        
    else:
        form = SignUpForm()
    return render(request, 's3.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user= authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, ' Login Successfull  !!')
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request, 's3.html' ,{'form':form})
    else:
        return HttpResponseRedirect('/hotel_images/')


def comment(request):
    if request.user.is_authenticated:
      
        if request.method == 'POST':

            form = Cpt(request.POST) 
    
            if form.is_valid(): 
                form.save() 
                form = Cpt()
                HttpResponseRedirect('/') 
        else: 
            form = Cpt() 
        return render(request, 's5.html', {'fm' : form}) 

    else:
        return HttpResponseRedirect('/login/')
