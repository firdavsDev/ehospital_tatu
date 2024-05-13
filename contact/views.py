from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import Contact


def contact(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            Contact.objects.create(
                name=name, email=email, subject=subject, phone=phone, message=message
            )
            messages.success(
                request, 'Your message has been sent successfully')
            return redirect('contact')
        return render(request, 'contact.html', {'success': False})
    except Exception as e:
        print(e)
        messages.error(request, 'Failed to send message')
        return render(request, 'contact.html', {'success': False})
