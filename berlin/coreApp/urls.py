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
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_change/', views.password_change, name='password_change'),
    path('profile/', views.profile, name='profile'),
    path('product_detail/', views.product_list, name='product_list'),
    path('<int:pk>/', views.detail, name='detail'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)