from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput({
		'class' : 'form-row username_input',
		'placeholder' : 'Username',
	}))

	password = forms.CharField(widget=forms.PasswordInput({
		'class' : 'form-row password_input',
		'placeholder' : 'Password',
	}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({
        'class' : 'form-row username_input',
        'placeholder' : 'Enter your new name',
    }))
    email = forms.EmailField(widget=forms.EmailInput({
        'class' : 'form-row email_input',
        'placeholder' : 'Enter your own email',
    }))
    password = forms.CharField(widget=forms.PasswordInput({
        'class' : 'form-row password_input',
        'placeholder' : 'Enter your new password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput({
        'class' : 'form-row password_input',
        'placeholder' : 'reapet your password',
    }), label='Password again')



    def clean_username(self):
        username = self.cleaned_data.get('username')
        mistake = User.objects.filter(username=username)
        if mistake.exists():
            raise forms.ValidationError('This username is busy')
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        mistake = User.objects.filter(email=email)
        if mistake.exists():
            raise forms.ValidationError('This email is busy')
        else:
            return email
    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2 and len(password) < 8:
            raise forms.ValidationError('This password is too short or they is not same')
