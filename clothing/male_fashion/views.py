from django.contrib.auth import login,authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import SignupForm,LoginForm
# Create your views here.
def index(request):
    return render(request,'male_fashion/index.html',{})
def shop(request):
    print(request.user)
    return render(request,'male_fashion/shop.html',{})
def login_view(request):
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request.POST)
        user = authenticate(request, email=form.cleaned_data.get('email'), password=form.cleaned_data.get('password'))
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect(reverse('home-page'))
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request,'male_fashion/login.html',{'form':form})
def signup_view(request):
    form=SignupForm()
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            if User.objects.filter(email=form.cleaned_data.get('email')).exists():
                messages.error(request, 'EmailAddress already exists')
            user.password1=form.cleaned_data.get('password1').lower()
            user.save()
            login(request, user)
            return redirect(reverse('shop-page'))
        else:
            messages.error(request,'Something happened during Signup')
    return render(request,'male_fashion/signup.html',{'form':form})
@login_required(login_url='/login')
def cart(request):

    return render(request,'male_fashion/shopping-cart.html',{})
@login_required(login_url='/login')
def add_to_cart(request):

    return redirect(request.META.get('HTTP_REFERER'))


def single_shop(request):

    return render(request,'male_fashion/shop-details.html',{})
def blog(request):

    return render(request,'male_fashion/blog.html',{})
def single_blog(request):

    return render(request,'male_fashion/blog-details.html',{})
@login_required(login_url='/login')
def checkout(request):

    return render(request,'male_fashion/checkout.html',{})
def about(request):

    return render(request,'male_fashion/about.html',{})
def contact(request):

    return render(request,'male_fashion/contact.html',{})