from pyexpat import model
from socket import fromshare
from django import forms
from django.core import validators

from .models import  User

class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model =User 
        fields = ['Book_name','available_stock','writter']
        widgets={
            
            'Book_name':forms.TextInput(attrs={'class':'form-control','id':'Book_nameid'}),
            'available_stock':forms.TextInput(attrs={'class':'form-control','id':'available_stockid'}),
            'writter' :forms.TextInput(attrs={'class':'form-control','id':'writterid'}) ,    
        }
        
        
        
        
        
