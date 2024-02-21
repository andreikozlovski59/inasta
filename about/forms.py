from typing import Any
from django import forms
from .models import About
from django.forms import ModelForm, TextInput, DateTimeInput
from django.core.exceptions import ValidationError

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['name', 'message','date']
        widgets = {
            'message': forms.Textarea( attrs={
                                             'style': 'width: 100%; height: 150px; border-style: solid;'
            }),
            'name': forms.TextInput( attrs={
                         'style': 'width: 100%; height: 40px; border-style: solid;'
            }),
            'date': forms.DateTimeInput(attrs={'readonly': 'readonly'})
        }
