from django.shortcuts import render

# Create your views here.
from .models import Contact


def contact(request):
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            website = request.POST.get('website')
            message = request.POST.get('message')
            Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                website=website,
                message=message
            )
            return render(request, 'contact.html', {'success': True})
        return render(request, 'contact.html', {'success': False})
    except Exception as e:
        print(e)
        return render(request, 'contact.html', {'success': False})
