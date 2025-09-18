from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils import timezone

from config.settings import EMAIL_HOST_USER

from .models import Distribution, AttemptedMailing


def send_message(distribution_id):
    """ Функция реализует оправке письма """

    distribution = get_object_or_404(Distribution, id=distribution_id)

    recipient_list = []
    for recipient in distribution.recipients.all():
        recipient_list.append(recipient.email)

    subject = distribution.message.subject
    message = distribution.message.text
    from_email = EMAIL_HOST_USER
    distribution.status = "Запущена"
    distribution.datatime_first_sending = timezone.now()
    distribution.save()

    try:
        send_mail(subject, message, from_email, recipient_list)
        distribution.status = "Завершена"
        distribution.datetime_end_sending = timezone.now()
        distribution.save()
        return ""

    except Exception as error:
        return error


def attempted_mailing(distribution_id, error):
    """ Функция регистрирует попытки отправки рассылки """

    distribution = get_object_or_404(Distribution, id=distribution_id)
    if error:
        attempt = AttemptedMailing.objects.create(attempt_datetime=timezone.now(),
                                                  status='Не успешно',
                                                  mail_server_response=error,
                                                  distribution=distribution)
        attempt.save()
    else:
        attempt = AttemptedMailing.objects.create(attempt_datetime=timezone.now(),
                                                  status='Успешно',
                                                  mail_server_response='OK',
                                                  distribution=distribution)
        attempt.save()