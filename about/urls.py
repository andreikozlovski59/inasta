from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name = 'about'),
path('add_comment', views.add_comment, name = 'add_comment')

]
