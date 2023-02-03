from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'index.html', context={})

def about(request):
    return render(request, 'about.html', context={})

def delete(request):
    return render(request, 'delete.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})
