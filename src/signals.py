from django.db.models.signals import post_save
from . models import BLog
from django.dispatch import receiver
from django.core.mail import send_mail

from django.contrib.auth import get_user_model
from django.template.loader import render_to_string


User = get_user_model()


@receiver(post_save, sender=BLog)
def send_notifications_email(sender , instance , created, **kwargs):

    if created:
        suject = "nouvelle bloque disponible !"
        message = render_to_string('email_post.html', {'blog': instance})
        recipient_list = User.objects.values_list('email', flat=True)
        send_mail(suject, message, 'kouamou.noumejie@gmail.com', recipient_list )



