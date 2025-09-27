from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.cache import cache

from config.settings import EMAIL_HOST_USER, CACHE_ENABLE

from .models import Distribution, AttemptedMailing, MailingRecipient, Message


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
        if mailing_recipient is not None:
            return mailing_recipient
        else:
            mailing_recipient = MailingRecipient.objects.all()
            cache.set(key_recipient, mailing_recipient, 60 * 5)
            return mailing_recipient

    @staticmethod
    def set_mailing_recipient_to_cache():
        """ Функция обновляет данные о получателях рассылки в кеше при их создании или изменении """

        if CACHE_ENABLE:
            key_recipient = "mailing_recipient_list"
            mailing_recipient = MailingRecipient.objects.all()
            cache.set(key_recipient, mailing_recipient, 60 * 5)

    @staticmethod
    def get_message_from_cache():
        """ Функция получает данные о письмах из кеша, если кеш пуст, то из базы данных """

        if not CACHE_ENABLE:
            return Message.objects.all()

        key_message = "message_list"
        message = cache.get(key_message)
        if message is not None:
            return message
        else:
            message = Message.objects.all()
            cache.set(key_message, message, 60 * 5)
            return message

    @staticmethod
    def set_message_to_cache():
        """ Функция обновляет данные о письмах в кеше при их создании или изменении """

        if CACHE_ENABLE:
            key_message = "message_list"
            message = Message.objects.all()
            cache.set(key_message, message, 60 * 5)

    @staticmethod
    def get_distribution_from_cache():
        """ Функция получает данные о рассылках из кеша, если кеш пуст, то из базы данных """

        if not CACHE_ENABLE:
            return Distribution.objects.all()

        key_distribution = "distribution_list"
        distribution = cache.get(key_distribution)
        if distribution is not None:
            return distribution
        else:
            distribution = Distribution.objects.all()
            cache.set(key_distribution, distribution, 60 * 5)
            return distribution

    @staticmethod
    def set_distribution_to_cache():
        """ Функция обновляет данные о письмах в кеше при их создании или изменении """

        if CACHE_ENABLE:
            key_distribution = "distribution_list"
            distribution = Distribution.objects.all()
            cache.set(key_distribution, distribution, 60 * 5)