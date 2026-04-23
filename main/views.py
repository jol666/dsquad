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

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect

def contact(request):
    if request.method == 'POST':
        return redirect('contact')   # ⬅️ skip everything

    return render(request, 'main/contact.html')
