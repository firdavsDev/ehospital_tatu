
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Add this import
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # index page
    path('', home, name='home'),
    # contact app
    path('contact/', include('contact.urls')),
    # clinic app
    path('clinic/', include('clinic.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
