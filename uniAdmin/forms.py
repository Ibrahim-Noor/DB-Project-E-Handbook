from django import forms


class adminLoginForm(forms.Form):
    username = forms.CharField(label = "Roll Number: ", max_length=10)
    password = forms.CharField(label = "Password: ",max_length=32, widget=forms.PasswordInput) 