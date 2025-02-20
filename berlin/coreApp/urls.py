from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'coreApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_change/', views.password_change, name='password_change'),
    path('profile/', views.profile, name='profile'),
    path('product_detail/', views.product_list, name='product_list'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)