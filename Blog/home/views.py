from django.shortcuts import render
from django.http import HttpResponseRedirect
from home.forms import SignupForm,BlogForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from home.models import blog
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account created Successfully !')
            return HttpResponseRedirect('/login/')
    else:
        fm = SignupForm()
    return render(request,'home/signup.html',{'form':fm})

def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'logged in successfully !')
                return HttpResponseRedirect('/welcome/')
        else:
            messages.info(request,'user not exist, check your credentials!\nplease signup first!!!')
            return HttpResponseRedirect('/login/')
    else:
        fm = AuthenticationForm()
        return render(request,'home/login.html',{'form':fm})

@login_required(login_url='/login/')       
def user_logout(request):
    logout(request)
    messages.success(request,'you logout Now!')
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def welcome_view(request):
    if request.method == 'POST':
        username = request.POST['name']
        if User.objects.filter(username=username).exists():
            if request.user.username == username:
                posts = blog.objects.filter(owner=request.user)
            else:
                posts = blog.objects.filter(Q(owner__username=username) & Q(mode__name='public'))
        else:
            messages.info(request,' Author Not Exists!')
            posts = blog.objects.filter(owner=request.user)

            
    else:
        posts = blog.objects.filter(owner=request.user)
    return render(request,'home/welcome.html',{'posts':posts})

@login_required(login_url='/login/')
def add_blog(request):
    if request.method == 'POST':
        fm = BlogForm(request.POST,request.FILES)
        if fm.is_valid():
            title= fm.cleaned_data['title']
            description = fm.cleaned_data['description']
            image = request.FILES['image']
            mode = fm.cleaned_data['mode']
            b = blog(title=title,description=description,image=image,mode=mode,owner=request.user)
            b.save()
            return HttpResponseRedirect(reverse('welcome'))
    else:
        fm = BlogForm()
    return render(request,'home/add_blog.html',{'form':fm})

@login_required(login_url='/login/')
def read_more(request,id):
    p = blog.objects.get(id=id)
    return render(request,'home/read_blog.html',{'p':p})



