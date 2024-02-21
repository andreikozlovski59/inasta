from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя')
    phone = forms.CharField(label='Номер телефона')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)