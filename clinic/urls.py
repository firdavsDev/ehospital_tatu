from django.urls import path

from .views import clinic_company_list, create_clinic_company

urlpatterns = [
    path('list/', clinic_company_list, name='clinic-list'),
    path('create/', create_clinic_company, name='clinic-create'),
]
