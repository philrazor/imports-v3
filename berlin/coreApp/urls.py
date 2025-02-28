from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'coreApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('product_list/', views.product_list, name='product_list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('brands/', views.brands, name='brands'),
    path('finances/', views.finances, name='finances'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)