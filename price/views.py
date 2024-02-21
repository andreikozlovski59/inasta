from django.shortcuts import render
from .models import Service

def price(request):
    price_user = Service.objects.all()
    return render(request,'price/price.html', {'price_user': price_user})
