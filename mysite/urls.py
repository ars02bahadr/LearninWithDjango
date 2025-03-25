from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user-types/', views.user_type_list, name='user_type_list'),
    path('user-types/create/', views.user_type_create, name='user_type_create'),
    path('user-types/<int:pk>/update/', views.user_type_update, name='user_type_update'),
    path('user-types/<int:pk>/delete/', views.user_type_delete, name='user_type_delete'),
    path('user-roles/', views.user_role_list, name='user_role_list'),
    path('user-roles/create/', views.user_role_create, name='user_role_create'),
    path('user-roles/<int:pk>/update/', views.user_role_update, name='user_role_update'),
    path('user-roles/<int:pk>/delete/', views.user_role_delete, name='user_role_delete'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/create/', views.profile_create, name='profile_create'),
    path('profiles/<int:pk>/update/', views.profile_update, name='profile_update'),
    path('profiles/<int:pk>/delete/', views.profile_delete, name='profile_delete'),
    path('profile/settings/', views.profile_settings, name='profile_settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   