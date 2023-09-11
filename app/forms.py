from django import forms
from django.core import validators

def Check_valid(value):
    if value[0].lower()=='s':
        raise forms.ValidationError('started with s')

def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('len is < 5')
    
class LibraryForms(forms.Form):
    BookName= forms.CharField(max_length=100, validators=[Check_valid, check_for_len])
    Author_name= forms.CharField(max_length=100)
    Mail= forms.EmailField(validators=[Check_valid])
    Publish= forms.DateField()