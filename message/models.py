from django.db import models

class MailingRecipient(models.Model):
    """ Описание полей модель - Получатель рассылки """
    email = models.CharField(max_length=100, unique=True, help_text='Адрес электронной почты', verbose_name='email')
    full_name = models.CharField(max_length=150, verbose_name='Ф. И. О.', help_text='Ф. И. О.')
    comment = models.TextField(verbose_name='Коментарий', help_text='Коментарий')

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

    def __str__(self):
        return f"{self.recipients} - {self.message} - {self.status}"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status',]

