from django import forms

class loginForm(forms.Form):
    roll_number = forms.CharField(label = "Roll Number: ", max_length=10)

class courseSelectForm(forms.Form):
    course = forms.CharField(widget=forms.Select)