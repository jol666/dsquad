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



from django.contrib import messages

import resend
import os
from django.shortcuts import render, redirect

resend.api_key = os.environ.get("RESEND_API_KEY")


def contact(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        try:
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

        except Exception as e:
            print("RESEND ERROR:", e)

        return redirect('contact')

    return render(request, 'main/contact.html')
