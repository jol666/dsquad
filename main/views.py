from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/home.html')

def services(request):
    return render(request, 'main/services.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

from django.shortcuts import render, redirect
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        return redirect('contact')

    return render(request, 'main/contact.html')
