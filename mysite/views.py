from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from mysite.models import UserType, UserRole,Profile
from mysite.forms import UserTypeForm, UserRoleForm, RegisterForm, ProfileUpdateForm, ProfileCreateForm, UserSettingsForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Varsayılan UserType'ı al veya oluştur
            default_user_type, created = UserType.objects.get_or_create(
                name='Standart Kullanıcı',
                defaults={'description': 'Varsayılan kullanıcı tipi'}
            )
            
            # Varsayılan UserRole'ü al veya oluştur
            default_user_role, created = UserRole.objects.get_or_create(
                name='Standart Rol',
                defaults={'description': 'Varsayılan kullanıcı rolü'}
            )
            
            # Profili oluştur
            profile = Profile.objects.create(
                user=user,
                phone_number='',
                profile_picture='',
                user_type=default_user_type
            )
            
            # Varsayılan rolü ekle
            profile.user_roles.add(default_user_role)
            profile.save()
            
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
            messages.error(request, 'Lütfen formu kontrol edin.')
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


@login_required(login_url='login')
def user_role_create(request):
    if request.method == 'POST':
        form = UserRoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kullanıcı rolü başarıyla oluşturuldu.')
            return redirect('user_role_list')
        else:
            messages.warning(request, 'Lütfen formu kontrol edin.')
            for field in form:
                if field.errors:
                    field.field.widget.attrs['class'] = field.field.widget.attrs.get('class', '') + ' is-invalid'
    else:
        form = UserRoleForm()
    
    return render(request, 'user_role_create.html', {'form': form})



@login_required(login_url='login')
def user_role_update(request, pk):
    try:
        user_role = UserRole.objects.get(pk=pk)
        if request.method == 'POST':
            form = UserRoleForm(request.POST, instance=user_role)
            if form.is_valid():
                form.save()
                messages.success(request, 'Kullanıcı rolü başarıyla güncellendi.')
                return redirect('user_role_list')
            else:
                messages.warning(request, 'Lütfen formu kontrol edin.')
                for field in form:
                    if field.errors:
                        field.field.widget.attrs['class'] = field.field.widget.attrs.get('class', '') + ' is-invalid'
        else:
            form = UserRoleForm(instance=user_role)
        
        return render(request, 'user_role_update.html', {
            'user_role': user_role,
            'form': form
        })
    except UserRole.DoesNotExist:
        messages.error(request, 'Kullanıcı rolü bulunamadı.')
        return redirect('user_role_list')




@login_required(login_url='login')
def user_role_delete(request, pk):
    try:
        user_role = UserRole.objects.get(pk=pk)
        user_role.delete()
        messages.success(request, 'Kullanıcı rolü başarıyla silindi.')
    except UserRole.DoesNotExist:
        messages.error(request, 'Kullanıcı rolü bulunamadı.')
    return redirect('user_role_list')


@login_required(login_url='login')
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})


@login_required(login_url='login')
def profile_create(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            messages.success(request, 'Yeni kullanıcı ve profil başarıyla oluşturuldu.')
            return redirect('profile_list')
        else:
            messages.warning(request, 'Lütfen form hatalarını düzeltin.')
            for field in form:
                if field.errors:
                    field.field.widget.attrs['class'] = field.field.widget.attrs.get('class', '') + ' is-invalid'
    else:
        form = ProfileCreateForm()
    
    roles = UserRole.objects.all()
    return render(request, 'profile_create.html', {'form': form, 'title': 'Yeni Kullanıcı ve Profil Oluştur', 'roles': roles})


@login_required(login_url='login')
def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    roles = UserRole.objects.all()
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil başarıyla güncellendi.')
            return redirect('profile_list')
        else:
            messages.warning(request, 'Lütfen form hatalarını düzeltin.')
            for field in form:
                if field.errors:
                    field.field.widget.attrs['class'] = field.field.widget.attrs.get('class', '') + ' is-invalid'
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'profile_update.html', {'form': form, 'title': 'Profil Düzenle', 'roles': roles})


@login_required(login_url='login')
def profile_delete(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
        profile.delete()
        messages.success(request, 'Profil başarıyla silindi.')
    except Profile.DoesNotExist:
        messages.error(request, 'Profil bulunamadı.')
    return redirect('profile_list')


@login_required(login_url='login')
def profile_settings(request):
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=request.user, user=request.user)
        if form.is_valid():
            user = form.save()
            # Eğer şifre değiştiyse yeniden giriş yap
            if form.cleaned_data.get('new_password'):
                update_session_auth_hash(request, user)  # Oturumu güncelle
            messages.success(request, 'Kullanıcı bilgileriniz başarıyla güncellendi.')
            return redirect('profile_settings')
        else:
            messages.warning(request, 'Lütfen form hatalarını düzeltin.')
            for field in form:
                if field.errors:
                    field.field.widget.attrs['class'] = field.field.widget.attrs.get('class', '') + ' is-invalid'
    else:
        form = UserSettingsForm(instance=request.user, user=request.user)
    
    return render(request, 'profile.html', {
        'form': form,
        'title': 'Kullanıcı Ayarları'
    })




