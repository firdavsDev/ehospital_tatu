from django.shortcuts import render


def home(request):
    """A view that displays a main page."""

    return render(request, 'index.html')
