from django import forms

class UserForm(forms.Form):
    rol = forms.CharField(max_length=200)
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=200)
    correo = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput())