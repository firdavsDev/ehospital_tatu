from django.db.models.signals import post_save
from django.dispatch import receiver


from .alerter import Alerter
from .models import Contact


@receiver(post_save, sender=Contact)
def create_contact(sender, instance, created, **kwargs):
    if created:
        tg_alert = Alerter(bot_token='7052116225:AAE4TQYP5tZgudnHcCnNHxub3h579nqkXpA',
                           chat_id='-4203662842')
        tg_alert.custom_alert(
            text=f'New contact: {instance.name}\n\n Mavzu: {instance.subject} \n\nMessage: {instance.message}')
