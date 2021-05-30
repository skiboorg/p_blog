
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect
from .forms import *
from django.contrib import messages
from .models import *
def index(request):
    allPosts = BlogPost.objects.all()
    return render(request, 'pages/index.html', locals())

def links(request):
    return render(request, 'pages/links.html', locals())

def about(request):
    return render(request, 'pages/about.html', locals())

def course(request):
    return render(request, 'pages/course.html', locals())

def profile(request):
    return render(request, 'pages/profile.html', locals())

def works(request):
    return render(request, 'pages/works.html', locals())

def signin(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Проверьте введеные данные')
            return HttpResponseRedirect('/signin')
    return render(request, 'pages/signin.html', locals())

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        data = {'email': email,'username': email, 'first_name': first_name, 'password2': password2, 'password1': password1}
        form = SignUpForm(data=data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'pages/signup.html', locals())

def reset(request):

    return render(request, 'pages/reset.html', locals())

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def post(request):
    return render(request, 'pages/post.html', locals())

def search(request):
    return render(request, 'pages/search.html', locals())

def blogpost(request,name_slug):
    post = BlogPost.objects.get(name_slug=name_slug)
    return render(request, 'pages/post_page.html', locals())
