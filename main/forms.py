from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(required=True, label='Введите имя', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.CharField(required=True, label='Введите Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), label='Введите пароль')


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Введите Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), label='Введите пароль')
