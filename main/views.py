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

import resend
import os

resend.api_key = os.getenv("RESEND_API_KEY")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "detailerssquad@gmail.com",
            "subject": "New Enquiry - D Squad",
            "html": f"""
                <h3>New Contact Form Submission</h3>
                <p><b>Name:</b> {name}</p>
                <p><b>Email:</b> {email}</p>
                <p><b>Phone:</b> {phone}</p>
                <p><b>Message:</b><br>{message}</p>
            """
        })

        return redirect('contact')

    return render(request, 'main/contact.html')
