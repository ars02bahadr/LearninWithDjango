from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserType, UserRole, Profile

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = UserType
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        required_fields = ['name', 'description']
        error_messages = {
            'name': {
                'required': 'Kullanıcı tipi adı zorunludur.',
                'max_length': 'Kullanıcı tipi adı çok uzun.',
                'min_length': 'Kullanıcı tipi adı çok kısa.',
            },
            'description': {
                'required': 'Açıklama zorunludur.',
                'max_length': 'Açıklama çok uzun.',
                'min_length': 'Açıklama çok kısa.',
            }
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Kullanıcı tipi adı en az 3 karakter olmalıdır.')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 3:
            raise forms.ValidationError('Açıklama en az 10 karakter olmalıdır.')
        return description


class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        required_fields = ['name', 'description']
        error_messages = {
            'name': {
                'required': 'Kullanıcı rolü adı zorunludur.',
                'max_length': 'Kullanıcı rolü adı çok uzun.',
                'min_length': 'Kullanıcı rolü adı çok kısa.',
            },
            'description': {
                'required': 'Açıklama zorunludur.',
                'max_length': 'Açıklama çok uzun.',
                'min_length': 'Açıklama çok kısa.',
            }
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Kullanıcı rolü adı en az 3 karakter olmalıdır.')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 3:
            raise forms.ValidationError('Açıklama en az 10 karakter olmalıdır.')
        return description


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bu e-posta adresi zaten kullanılıyor.')
        return email


class ProfileCreateForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Profile
        fields = ['username', 'password', 'password_confirm', 'phone_number', 'profile_picture', 'user_type', 'user_roles']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
            'user_roles': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        username = cleaned_data.get('username')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError('Şifreler eşleşmiyor.')

        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu kullanıcı adı zaten kullanılıyor.')

        return cleaned_data

    def save(self, commit=True):
        # Önce User oluştur
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )

        # Sonra Profile oluştur
        profile = super().save(commit=False)
        profile.user = user
        
        if commit:
            profile.save()
            self.save_m2m()
        return profile


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number', 'profile_picture', 'user_type', 'user_roles']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
            'user_roles': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'phone_number': {
                'required': 'Telefon numarası zorunludur.',
                'max_length': 'Telefon numarası en fazla 20 karakter olabilir.',
            },
            'user_type': {
                'required': 'Kullanıcı tipi zorunludur.',
            },
            'user_roles': {
                'required': 'En az bir rol seçilmelidir.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.user:
            instance.user = self.instance.user
        
        # User modelini güncelle
        user = instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        if commit:
            instance.save()
            self.save_m2m()
        return instance


class UserSettingsForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )
    new_password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.exclude(pk=self.user.pk).filter(email=email).exists():
            raise forms.ValidationError('Bu e-posta adresi zaten kullanılıyor.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        new_password_confirm = cleaned_data.get('new_password_confirm')

        if new_password or new_password_confirm or current_password:
            if not current_password:
                raise forms.ValidationError('Mevcut şifrenizi girmelisiniz.')
            if not self.user.check_password(current_password):
                raise forms.ValidationError('Mevcut şifreniz yanlış.')
            if not new_password:
                raise forms.ValidationError('Yeni şifre girmelisiniz.')
            if not new_password_confirm:
                raise forms.ValidationError('Yeni şifrenizi tekrar girmelisiniz.')
            if new_password != new_password_confirm:
                raise forms.ValidationError('Yeni şifreler eşleşmiyor.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        
        if self.cleaned_data.get('new_password'):
            user.set_password(self.cleaned_data['new_password'])
        
        if commit:
            user.save()
        return user  