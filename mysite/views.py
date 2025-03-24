from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from mysite.models import UserType, UserRole
from mysite.forms import UserTypeForm, UserRoleForm, RegisterForm


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Hesabınız başarıyla oluşturuldu.')
            return redirect('index')
        else:
            messages.warning(request, 'Lütfen formu kontrol edin.')
            for field in form:
                if field.errors:
                    field.field.widget.attrs['class'] = field.field.widget.attrs.get('class', '') + ' is-invalid'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Başarıyla giriş yaptınız.')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı.')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Başarıyla çıkış yaptınız.')
    return redirect('index')


@login_required(login_url='login')
def user_type_list(request):
    search_query = request.GET.get('search', '')
    user_types = UserType.objects.all()
    
    if search_query:
        user_types = user_types.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    paginator = Paginator(user_types, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'user_types': page_obj,
        'search_query': search_query
    }
    return render(request, 'user_type_list.html', context)


@login_required(login_url='login')
def user_type_create(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kullanıcı tipi başarıyla oluşturuldu.')
            return redirect('user_type_list')
        else:
            messages.warning(request, 'Lütfen formu kontrol edin.')
            for field in form:
                if field.errors:
                    field.field.widget.attrs['class'] = field.field.widget.attrs.get('class', '') + ' is-invalid'
    else:
        form = UserTypeForm()
    
    return render(request, 'user_type_create.html', {'form': form})


@login_required(login_url='login')
def user_type_update(request, pk):
    try:
        user_type = UserType.objects.get(pk=pk)
        if request.method == 'POST':
            form = UserTypeForm(request.POST, instance=user_type)
            if form.is_valid():
                form.save()
                messages.success(request, 'Kullanıcı tipi başarıyla güncellendi.')
                return redirect('user_type_list')
            else:
                messages.warning(request, 'Lütfen formu kontrol edin.')
                for field in form:
                    if field.errors:
                        field.field.widget.attrs['class'] = field.field.widget.attrs.get('class', '') + ' is-invalid'
        else:
            form = UserTypeForm(instance=user_type)
        
        return render(request, 'user_type_update.html', {
            'user_type': user_type,
            'form': form
        })
    except UserType.DoesNotExist:
        messages.error(request, 'Kullanıcı tipi bulunamadı.')
        return redirect('user_type_list')


@login_required(login_url='login')
def user_type_delete(request, pk):
    try:
        user_type = UserType.objects.get(pk=pk)
        user_type.delete()
        messages.success(request, 'Kullanıcı tipi başarıyla silindi.')
    except UserType.DoesNotExist:
        messages.error(request, 'Kullanıcı tipi bulunamadı.')
    return redirect('user_type_list')


@login_required(login_url='login')
def user_role_list(request):
    search_query = request.GET.get('search', '')
    user_roles = UserRole.objects.all()
    
    if search_query:
        user_roles = user_roles.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    paginator = Paginator(user_roles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'user_roles': page_obj,
        'search_query': search_query
    }
    return render(request, 'user_role_list.html', context)

