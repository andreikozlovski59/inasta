from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = 'Новое сообщение с сайта'
            message = f'Имя: {name}\nНомер телефона: {phone}\nEmail: {email}\nСообщение: {message}'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = 'andreikozlovski59@gmail.com'

            send_mail(subject, message, from_email, [to_email])
            form = ContactForm()
            return render(request,'main/index.html',{'form': form})
    else:
        form = ContactForm()
    return render(request, 'main/index.html', {'form': form})

def about(request):
    return render(request,'main/about.html')

def possibilities(request):
    return render(request,'main/possibilities.html')

def success(request):
    return render(request, 'main/success.html')
