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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        full_message = f"""
        New Contact Enquiry from D Squad Website:

        Name: {name}
        Email: {email}
        Phone: {phone}
        Message:
        {message}
        """

        send_mail(
            subject="New Enquiry - D Squad",
            message=full_message,
            from_email=email,
            recipient_list=['detailerssquad@gmail.com'],  # your receiving email
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'main/contact.html')

