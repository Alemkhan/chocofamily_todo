from datetime import timedelta
from datetime import datetime
import pytz

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication.models import User

from .tasks import send_email


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='tasks')


class Task(BaseModel):
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    priority = models.PositiveSmallIntegerField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)


@receiver(post_save, sender=Task)
def deadline_celery_task(sender, instance, **kwargs):
    email = instance.created_by.login
    if instance.deadline:
        email_deadline = instance.deadline - timedelta(hours=1)
        if email_deadline > pytz.UTC.localize(datetime.now()):
            send_email.apply_async(eta=email_deadline, args=email)
        else:
            send_email.delay(email)
