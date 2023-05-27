from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from posts.models import Post

@receiver(post_save, sender=Post)
def send_post_creation_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Post Created'
        message = f'A new post "{instance.title}" has been created.'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = instance.author.email
        send_mail(subject, message, from_email, [to_email])
