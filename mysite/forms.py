from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserType, UserRole

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = UserType
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Kullanıcı Tipi Adı'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Açıklama',
                'rows': 4
            }),
        }
        fields = ['name', 'description']
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
        if len(description) < 10:
            raise forms.ValidationError('Açıklama en az 10 karakter olmalıdır.')
        return description


class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Kullanıcı Rolü Adı'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Açıklama',
                'rows': 4
            }),
        }
        fields = ['name', 'description']
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
        if len(description) < 10:
            raise forms.ValidationError('Açıklama en az 10 karakter olmalıdır.')
        return description


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'E-posta Adresi'
        })
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ad'
        })
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Soyad'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kullanıcı Adı'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Şifre'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Şifre (Tekrar)'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bu e-posta adresi zaten kullanılıyor.')
        return email  