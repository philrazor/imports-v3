from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Product
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    products = Product.objects.all()[:8]
    context = {
        'products': products
    }
    return render(request, 'coreApp/index.html' , context)

from .models import Product, Make, Model

def search_products(request):
    query = request.GET.get('q', '')
    make_filter = request.GET.get('make', '')
    model = request.GET.get('model', '')

    products = Product.objects.all()

    if query:
        products = products.filter(product_name__icontains=query)

    if make_filter:
        products = products.filter(make__make_name__icontains=make_filter)

    if model:
        products = products.filter(model__model_name__icontains=model_filter)

    makes = Make.objects.all()
    models = Model.objects.all()

    return render(request, 'coreApp/search_results.html', {
        'products': products,
        'query': query,
        'makes': makes,
        'models': models,
        'make_filter': make_filter,
        'model_filter': model,
    })

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




@login_required
def profile(request):
    return render(request, 'coreApp/profile.html', {'user': request.user})

@login_required
def update_profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.phone_number = request.POST.get('last_name', user.phone_number)
        user.address = request.POST.get('address', user.address)
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('coreApp:profile')

    return render(request, 'coreApp/update_profile.html')

@login_required
def delete_profile(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('coreApp:register')

    return render(request, 'coreApp/delete_profile.html')

