from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Product
from .services import EditProductNotificationService


@receiver(post_save, sender=Product)
def send_notication(sender, **kwargs):
    if not kwargs.get('created'):
        instance = kwargs.get('instance')
        EditProductNotificationService().send(product=instance)
