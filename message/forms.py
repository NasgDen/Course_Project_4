from django import forms

from .models import Distribution, MailingRecipient, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class MailingRecipientForm(StyleFormMixin, forms.ModelForm):
    """Класс реализующий интерфейс формы для получателя рассылки"""

    class Meta:
        model = MailingRecipient
        fields = [
            "email",
            "full_name",
            "comment",
        ]


class MessageForm(StyleFormMixin, forms.ModelForm):
    """Класс реализующий интерфейс формы для писем"""

    class Meta:
        model = Message
        fields = [
            "subject",
            "text",
            "comment",
        ]


class DistributionForm(StyleFormMixin, forms.ModelForm):
    """Класс реализующий интерфейс формы для писем"""

    class Meta:
        model = Distribution
        fields = [
            "message",
            "recipients",
        ]
