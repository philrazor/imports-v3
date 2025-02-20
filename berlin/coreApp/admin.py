from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Make, Model, Product , ProductImage
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'address')}),
    )


class ProductImageInline(admin.TabularInline):  # Use StackedInline for a vertical layout
    model = ProductImage
    extra = 1  # Number of empty image slots by default

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Make)
admin.site.register(Model)


