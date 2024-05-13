from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Contact

admin.site.site_header = "ESchool Admin"
admin.site.site_title = "ESchool Admin Portal"
admin.site.index_title = "Welcome to ESchool Portal"
admin.site.empty_value_display = "Ma'lumot yo'q"
admin.site.unregister(Group)

admin.site.register(Contact)
