from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
from .models import ClinicCompany


def clinic_company_list(request):
    try:
        # search and pagination start
        search = request.GET.get('search')
        if search:
            clinic_companies = ClinicCompany.objects.filter(
                name__icontains=search, is_checked=True)
        else:
            clinic_companies = ClinicCompany.objects.filter(is_checked=True)
        # pagination
        paginator = Paginator(clinic_companies, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # search and pagination end
        return render(request, 'clinic/list.html', {'page_obj': page_obj})
    except Exception as e:
        print(e)
        return render(request, 'clinic/list.html', {'page_obj': None})


def create_clinic_company(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            official_name = request.POST.get('official_name')
            brand_name = request.POST.get('brand_name')
            sector_category = request.POST.get('sector_category')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            faks = request.POST.get('faks')
            city_code = request.POST.get('city_code')
            ClinicCompany.objects.create(
                name=name, address=address, phone=phone, email=email,
                official_name=official_name, brand_name=brand_name,
                sector_category=sector_category, faks=faks, city_code=city_code
            )
            return render(request, 'clinic/create.html', {'message': 'Clinic company created successfully'})
        return render(request, 'clinic/create.html')
    except Exception as e:
        print(e)
        return render(request, 'clinic/create.html', {'message': 'Failed to create clinic company'})
