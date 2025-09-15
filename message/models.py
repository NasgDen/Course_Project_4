from django.db import models

class MailingRecipient(models.Model):
    """ Описание полей модель - Получатель рассылки """
    email = models.CharField(max_length=100, unique=True, help_text='Адрес электронной почты', verbose_name='email')
    full_name = models.CharField(max_length=150, verbose_name='Ф. И. О.', help_text='Ф. И. О.')
    comment = models.TextField(verbose_name='Коментарий', help_text='Коментарий')

    class Meta:
        verbose_name = 'Получатель рассылки'
        verbose_name_plural = 'Получатели рассылки'
        ordering = ['email',]


class Message(models.Model):
    """ Описание полей модель - Сообщение """
    subject = models.CharField(max_length=250, verbose_name='Тема письма', help_text='Тема письма')
    text = models.TextField(verbose_name='Тело письма', help_text='Тело письма')

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
    datatime_first_sending = models.DateTimeField(verbose_name='Дата и время первой отправки', help_text='Дата и время первой отправки')
    datetime_end_sending = models.DateTimeField(verbose_name='Дата и время окончания отправки', help_text='Дата и время окончания отправки')
    status = models.CharField(max_length=10, verbose_name='Статус', help_text='Статус', choices=STATUS_CHOICES)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='distributions', verbose_name='Сообщение')
    recipients = models.ManyToManyField(MailingRecipient, related_name='distributions', verbose_name='Получатели')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status',]

