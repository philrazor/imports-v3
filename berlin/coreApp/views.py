from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Product
from .forms import CustomUserCreationForm
from django.http import JsonResponse

def home(request):
    products = Product.objects.all()[:8]
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
            return redirect('coreApp:login_user')
    else:
        form = CustomUserCreationForm()
    return render(request, 'coreApp/register.html', {'form': form})

def login_user(request):
    # Login logic
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('coreApp:home')
        else:
            return JsonResponse({'error': 'Invalid credentials'})
    return render(request, 'coreApp/login_user.html')

def logout_user(request):
    # Logout logic
    logout(request)
    return redirect('coreApp:login_user')


def product_list(request):
    parts = Product.objects.all()
    return render(request, 'coreApp/product_list.html', {'parts': parts})


def detail(request, pk):
    part = Product.objects.get(pk=pk)
    if part is None:
        return JsonResponse({'error': 'Part not found'})
    return render(request, 'coreApp/detail.html', {'part': part})




def brands(request):
    return render(request, 'coreApp/brands.html')

def finances(request):
    return render(request, 'coreApp/finances.html')

def about(request):
    return render(request, 'coreApp/about.html')

def contact(request):
    return render(request, 'coreApp/contact.html')


