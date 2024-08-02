from django import forms
from .models import User


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User 
        fields = ['id','name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
        }
