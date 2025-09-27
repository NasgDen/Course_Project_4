from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.cache import cache

from config.settings import EMAIL_HOST_USER, CACHE_ENABLE

from .models import Distribution, AttemptedMailing, MailingRecipient


class MessageService:
    """ Класс реализующий интерфейс сервисных функций """

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def get_mailing_recipient_from_cache():
        """ Функция получает данные о получателях рассылки из кеша, если кеш пуст, то из базы данных """
        if not CACHE_ENABLE:
            return MailingRecipient.objects.all()

        key_recipient = "mailing_recipient_list"
        mailing_recipient = cache.get(key_recipient)
        print("CACHE", mailing_recipient)
        if mailing_recipient is not None:
            return mailing_recipient
        else:
            mailing_recipient = MailingRecipient.objects.all()
            cache.set(key_recipient, mailing_recipient, 60 * 5)
            return mailing_recipient