from django.shortcuts import (render, redirect,

get_object_or_404,  HttpResponseRedirect, HttpResponse)
from django.urls import reverse, reverse_lazy
# Create your views here.
from .forms import FormCreateUser, FormPost, FormComment
from src.models import BLog, Comment
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
User= get_user_model()

def index(request):
    post = BLog.objects.all()
    return render(request, 'index.html', {'post':post})


def user_register(request):
    if request.method == "POST":
        form = FormCreateUser(request.POST)
        if form.is_valid():

            form.save()
            return redirect('user_login')
    else:
        form = FormCreateUser()

    return render(request, 'user_register.html', {'form':form})



def dashboard(request):
    if request.user.is_authenticated:
        post = BLog.objects.filter(user=request.user)
        return render(request, 'dashboad.html',{'post':post})
    else:
        return redirect('user_login')    

def create_post(request):
    if request.method == 'POST':
        form = FormPost( request.POST, request.FILES)
        if form.is_valid():
            post= form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('dashboard')
    else:
        form = FormPost()        
    return render(request, 'create_post.html', {'form': form})

def update_post(request, pk):

    posts = get_object_or_404(BLog, id=pk)
    if  request.method == 'POST':
        form = FormPost(request.POST, request.FILES,instance=posts)
        if form.is_valid():
            form.save()
            return redirect('index')
    else :
        form = FormPost(instance=posts)
    return render(request, 'update_post.html', {'form': form})

    

def delete_post(request, pk):
    post = get_object_or_404(BLog, id=pk)
    post.delete()
    return redirect('dashboard')
     

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        
        else:
            messages.error(request, "username or password is not correct! ")

    return render(request, 'user_login.html')        


def user_logut(request):
    logout(request)

    return redirect('user_login')

@login_required(login_url="user_login")
def likes(request, pk):
    post = get_object_or_404(BLog, id=pk)
    
    if  request.user.is_authenticated:
        if request.user in post.likes.all():
            post.likes.remove(request.user)

        else: 
            post.likes.add(request.user)
        return  redirect(request.META.get('HTTP_REFERER', 'home'))
           



def comment_post(request, pk):
    post = get_object_or_404(BLog, id=pk)
    comment = Comment.objects.filter(post=post).order_by('created_at')

    if request.method == 'POST':
        form  = FormComment(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect(request.META.get('HTTP_REFERER', 'comment_post'))
     
               
    else:
       form = FormComment()
    
    return render(request, 'comment_post.html', {
     'post':post, 'comment':comment, 'form':form
    })