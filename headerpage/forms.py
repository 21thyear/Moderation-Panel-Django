from django import forms


class RegisterForm(forms.Form):
    register_name = forms.CharField(label="Имя", max_length=32)
    register_mail = forms.CharField(label="Имя", max_length=32)
    register_pass = forms.CharField(label="Имя", max_length=32)