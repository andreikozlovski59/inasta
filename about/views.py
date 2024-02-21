import datetime

from django.shortcuts import render, redirect
from .models import About
from .forms import AboutForm

def about(request):
    comment = About.objects.all()
    return render(request,'about/about.html', {'comment': comment})

def add_comment(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            comment_entry = form.save(commit=False)
            comment_entry.issued = datetime.datetime.now()
            comment_entry.save()
            return redirect('about')
    else:
        form = AboutForm()
    return render(request, 'about/add_comment.html', {'form': form})
