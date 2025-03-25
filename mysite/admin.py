from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserType, UserRole, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profil'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    list_per_page = 10

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    list_per_page = 10

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_user_full_name', 'user', 'phone_number', 'user_type')
    list_filter = ('user_type', 'user_roles')
    search_fields = ('user__username', 'user__email', 'phone_number', 'user__first_name', 'user__last_name')
    filter_horizontal = ('user_roles',)
    list_per_page = 10  

    def get_user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_user_full_name.short_description = 'Ad Soyad'
    get_user_full_name.admin_order_field = 'user__first_name'  # Sıralama için

