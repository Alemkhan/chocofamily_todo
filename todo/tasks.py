from django.core.mail import send_mail

from celery import shared_task


@shared_task
def send_email(email: str):
    # deadline_arrives = Task.objects.filter(
    #     deadline__lte=timezone.now() - timedelta(hours=1)
    # )

    # emails = [x.created_by.email for x in deadline_arrives

    send_mail(
        'Your task deadline arrives',
        'Hey, checkout your tasks',
        'alem@gmail.com',
        [email, ],
    )
