from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('possibilities', views.possibilities, name='possibilities'),
    path('success', views.success, name='success')
]
