from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Contact

admin.site.site_header = "EHospital Admin"
admin.site.site_title = "EHospital Admin Portal"
admin.site.index_title = "Welcome to EHospital Portal"
admin.site.empty_value_display = "Ma'lumot yo'q"
admin.site.unregister(Group)

# Register Contact model
admin.site.register(Contact)
