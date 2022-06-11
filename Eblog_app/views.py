from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    '''Renders the homepage'''
    my_blog = Blog.objects.all()
    return render(request,"index.html",{'key': my_blog})

def edit(request):
    '''Renders the editpage'''
    return render(request,"edit.html")

def email(request):
    '''Renders the emailpage'''
    return render(request,"email.html")

def content(request):
    '''Renders the contentpage'''
    return render(request,"content.html")

def profile(request):
    '''Renders the profilepage'''
    return render(request,"profile.html")

def login(request):
    '''Renders the loginpage'''
    return render(request,"log.html")

def signup(request):
    '''Renders the signuppage'''
    return render(request,"sign.html")

def add_email(request):
    add_email = request.Get.get('add_email')
    print(add_email)
    return render(request,"index.html")