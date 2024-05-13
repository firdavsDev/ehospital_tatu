from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Contact

admin.site.site_header = "ESchool Admin"
admin.site.site_title = "ESchool Admin Portal"
admin.site.index_title = "Welcome to ESchool Portal"
admin.site.empty_value_display = "Ma'lumot yo'q"
admin.site.unregister(Group)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'email', 'is_asnwered', 'created')
    list_filter = ('is_asnwered', 'created')
    search_fields = ('first_name', 'last_name', 'email', 'message')
    date_hierarchy = 'created'
    ordering = ('-created',)
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'website')
        }),
        ('Message', {
            'fields': ('message', 'is_asnwered')
        }),
    )
    list_per_page = 25
    list_editable = ('is_asnwered',)
    readonly_fields = ('created', 'updated')
    actions = ['mark_as_answered']

    def mark_as_answered(self, request, queryset):
        queryset.update(is_asnwered=True)
    mark_as_answered.short_description = 'Mark selected contacts as answered'
