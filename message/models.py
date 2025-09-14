from django.db import models

class MailingRecipient(models.Model):
    """ Описание полей модель - Получатель рассылки """
    email = models.CharField(max_length=100, unique=True, help_text='Адрес электронной почты', verbose_name='email')
    full_name = models.CharField(max_length=150, verbose_name='Ф. И. О.', help_text='Ф. И. О.')
    comment = models.TextField(verbose_name='Коментарий', help_text='Коментарий')


class Message(models.Model):
    """ Описание полей модель - Сообщение """
    subject = models.CharField(max_length=250, verbose_name='Тема письма', help_text='Тема письма')
    text = models.TextField(verbose_name='Тело письма', help_text='Тело письма')


class Distribution(models.Model):
    """ Описание полей модель - Рассылка """
    datatime_first_sending = models.DateTimeField(verbose_name='Дата и время первой отправки', help_text='Дата и время первой отправки')
    datetime_end_sending = models.DateTimeField(verbose_name='Дата и время окончания отправки', help_text='Дата и время окончания отправки')
    status = models.CharField(max_length=15, verbose_name='Статус', help_text='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='distributions', verbose_name='Сообщение')
    recipients = models.ManyToManyField(MailingRecipient, related_name='distributions', verbose_name='Получатели')

