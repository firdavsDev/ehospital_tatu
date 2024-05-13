from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'))
    website = models.URLField(_('website'), blank=True, null=True)
    phone = models.CharField(
        _('phone number'), max_length=15, blank=True, null=True)
    message = models.TextField(_('message'))
    is_asnwered = models.BooleanField(_('is answered'), default=False)
    # Timestamps
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        ordering = ('-created',)
