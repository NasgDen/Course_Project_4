from django.db import models

from users.models import CustomUser


class MailingRecipient(models.Model):
    """ Описание полей модель - Получатель рассылки """
    email = models.CharField(max_length=100, unique=True, help_text='Адрес электронной почты', verbose_name='email')
    full_name = models.CharField(max_length=150, verbose_name='Ф. И. О.', help_text='Ф. И. О.')
    comment = models.TextField(verbose_name='Коментарий', help_text='Коментарий')
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='mailing_recipient', verbose_name='Владелец',
                              blank=True, null=True)

    def __str__(self):
        return f"{self.email} - {self.full_name}"

    class Meta:
        verbose_name = 'Получатель рассылки'
        verbose_name_plural = 'Получатели рассылки'
        ordering = ['email',]


class Message(models.Model):
    """ Описание полей модель - Сообщение """
    subject = models.CharField(max_length=250, verbose_name='Тема письма', help_text='Тема письма')
    text = models.TextField(verbose_name='Тело письма', help_text='Тело письма')
    comment = models.TextField(verbose_name='Коментарий', help_text='Коментарий', null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='message', verbose_name='Владелец',
                              blank=True, null=True)


    def __str__(self):
        return f"{self.subject}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['subject',]


class Distribution(models.Model):
    """ Описание полей модель - Рассылка """
    COMPLETED = 'сompleted'
    CREATED = 'сreated'
    LAUNCHED = 'launched'

    STATUS_CHOICES = [
        (COMPLETED, 'Завершена'),
        (CREATED, 'Создана'),
        (LAUNCHED, 'Запущена'),
    ]
    datatime_first_sending = models.DateTimeField(verbose_name='Дата и время первой отправки', help_text='Дата и время первой отправки', null=True, blank=True)
    datetime_end_sending = models.DateTimeField(verbose_name='Дата и время окончания отправки', help_text='Дата и время окончания отправки', null=True, blank=True)
    status = models.CharField(max_length=10, verbose_name='Статус', help_text='Статус', choices=STATUS_CHOICES, default='Создана')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='distributions', verbose_name='Сообщение')
    recipients = models.ManyToManyField(MailingRecipient, related_name='distributions', verbose_name='Получатели')
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='distributions', verbose_name='Владелец',
                              blank=True, null=True)
    mailings_status = models.BooleanField(default=False, verbose_name='Статус отключения рассылки',)

    def __str__(self):
        return f"{self.recipients} - {self.message} - {self.status}"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status',]
        permissions = [('can_disabling_mailings_product', 'can disabling mailings product')]

class AttemptedMailing(models.Model):
    """ Описание полей модель - Попытка рассылка """
    SUCCESSFULLY = 'successful'
    NOTSUCCESSFULLLY = 'not successful'

    STATUS_CHOICES = [
        (SUCCESSFULLY, 'Успешно'),
        (NOTSUCCESSFULLLY, 'Не успешно'),
    ]


    attempt_datetime = models.DateTimeField(verbose_name='Дата и время попытки', help_text='Дата и время попытки', null=True, blank=True)
    status = models.CharField(max_length=20, verbose_name='Статус', help_text='Статус', choices=STATUS_CHOICES, default='')
    mail_server_response = models.TextField(verbose_name='Ответ почтового сервера', help_text='Ответ почтового сервера')
    distribution = models.ForeignKey(Distribution, on_delete=models.CASCADE, related_name='attempted_mailing', verbose_name='Рассылка')

    def __str__(self):
        return f"{self.attempt_datetime }: {self.status}"

    class Meta:
        verbose_name = 'Попытка рассылка'
        verbose_name_plural = 'Попытки рассылка'
        ordering = ['status',]