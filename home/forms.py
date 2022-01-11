from django import forms
from django.contrib.auth.forms import UserCreationForm
from usermember.models import MyUser
from .models import Contact
from django.forms import ValidationError

class registerForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data['email']

        user = MyUser.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('Email này đã có người sử dụng.'))

        return email
    class Meta:
        model = MyUser
        fields = ['username','email','password1','password2',]

class loginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)

class ContactForm(forms.ModelForm):
    fullname = forms.CharField(label='Họ tên', required=True,max_length=55,
                widget=forms.TextInput(attrs={'placeholder': 'Họ tên:'}))
    email = forms.CharField(label='Email', required=True,max_length=55,
                widget=forms.EmailInput(attrs={'placeholder': 'Email:'}))
    phone = forms.CharField(label='Số điện thoại', required=True,max_length=11,
                widget=forms.TextInput(attrs={'placeholder': 'Số điện thoại:'}))
    address = forms.CharField(label='Địa chỉ', required=True,max_length=255,
                widget=forms.Textarea(attrs={'placeholder': 'Địa chỉ:','rows':4, 'cols':40}))
    content = forms.CharField(label='Nội dung', required=True,max_length=255,
                widget=forms.Textarea(attrs={'placeholder': 'Nội dung:','rows':7, 'cols':40}))
    class Meta:
        model = Contact
        fields = '__all__'