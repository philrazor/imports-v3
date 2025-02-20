from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Product
from .forms import CustomUserCreationForm
from django.http import JsonResponse

def index(request):
    products = Product.objects.all()[:10]
    context = {
        'products': products
    }
    return render(request, 'coreApp/index.html' , context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'coreApp/register.html', {'form': form})

def login_user(request):
    # Login logic
    return render(request, 'coreApp/login.html')

def logout_user(request):
    # Logout logic
    return redirect('login')

def password_reset(request):
    # Password reset logic
    return render(request, 'coreApp/password_reset.html')

def password_change(request):
    # Password change logic
    return render(request, 'coreApp/password_change.html')

def profile(request):
    # Profile management logic
    return render(request, 'coreApp/profile.html')

def product_list(request):
    parts = Product.objects.all()
    return render(request, 'coreApp/product_list.html', {'parts': parts})




