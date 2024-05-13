from django.contrib import admin

# Register your models here.
from .models import ClinicCompany


class ClinicCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'official_name', 'brand_name', 'sector_category', 'address',
                    'phone', 'email', 'faks', 'city_code', 'is_checked', 'created_at', 'updated_at')
    list_filter = ('is_checked', 'created_at', 'updated_at')
    search_fields = ('name', 'official_name', 'brand_name',
                     'sector_category', 'address', 'phone', 'email', 'faks', 'city_code')
    list_per_page = 25
    list_editable = ('is_checked',)
    list_display_links = ('name', 'official_name', 'brand_name',
                          'sector_category', 'address', 'phone', 'email', 'faks', 'city_code')


admin.site.register(ClinicCompany, ClinicCompanyAdmin)
