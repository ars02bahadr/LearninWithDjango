from django.urls import path
from . import views

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
]   