from django import forms

# Create your models here.
class Userform(forms.Form):
    username = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=10)
    password = forms.CharField(max_length=40)