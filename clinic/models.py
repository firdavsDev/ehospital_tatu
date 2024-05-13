from django.db import models


class ClinicCompany(models.Model):
    name = models.CharField(max_length=250, verbose_name='Company Name')
    official_name = models.CharField(
        max_length=250, verbose_name='Official Name')
    brand_name = models.CharField(max_length=250, verbose_name='Brand Name')
    sector_category = models.CharField(
        max_length=250, verbose_name='Sector Category')
    address = models.CharField(max_length=250, verbose_name='Address')
    phone = models.CharField(max_length=250, verbose_name='Phone')
    email = models.EmailField(max_length=250, verbose_name='Email')
    faks = models.CharField(max_length=250, verbose_name='Faks')
    city_code = models.CharField(max_length=250, verbose_name='City Code')
    is_checked = models.BooleanField(
        default=False, verbose_name='Is Checked by Admin')
    # common fiels
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Clinic Company'
        verbose_name_plural = 'Clinic Companies'
