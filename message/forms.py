from django import forms

from .models import MailingRecipient, Message, Distribution


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"
            if fild_name == 'name':
                field.widget.attrs['placeholder'] = "Введите название товара"
            elif fild_name == 'description':
                field.widget.attrs['placeholder'] = "Введите описание товара"
            elif fild_name == 'is_published':
                field.widget.attrs['class'] = "form-check-input"


class MailingRecipientForm(StyleFormMixin, forms.ModelForm):
    """ Класс реализующий интерфейс формы для получателя рассылки """
    class Meta:
        model = MailingRecipient
        fields = ['email', 'full_name', 'comment',]


class MessageForm(StyleFormMixin, forms.ModelForm):
    """ Класс реализующий интерфейс формы для писем """
    class Meta:
        model = Message
        fields = ['subject', 'text', 'comment',]


class DistributionForm(StyleFormMixin, forms.ModelForm):
    """ Класс реализующий интерфейс формы для писем """
    class Meta:
        model = Distribution
        fields = ['message', 'recipients',]