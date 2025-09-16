from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .models import MailingRecipient, Message, Distribution


class MailingRecipientCreateView(CreateView):
    """ Класс реализующий интерфейс для создания информации о получателе сообщения """

    model = MailingRecipient
    template_name = 'message/recipient_add.html'
    fields = ['email', 'full_name', 'comment',]
    context_object_name = 'recipient'
    success_url = reverse_lazy('message:recipient_list')


class MailingRecipientListView(ListView):
    """ Класс реализующий интерфейс для отображения информации о получателях сообщений """

    model = MailingRecipient
    template_name = 'message/recipient_list.html'
    context_object_name = 'recipients'


class MailingRecipientUpdateView(UpdateView):
    """ Класс реализующий интерфейс для изменения информации о получателе сообщения """

    model = MailingRecipient
    template_name = 'message/recipient_add.html'
    fields = ['email', 'full_name', 'comment',]
    context_object_name = 'recipient'
    success_url = reverse_lazy('message:recipient_list')


class MailingRecipientDeleteView(DeleteView):
    """ Класс реализующий интерфейс для удаления информации о получателе сообщения """

    model = MailingRecipient
    template_name = 'message/recipient_delete_confirm.html'
    context_object_name = 'recipient'
    success_url = reverse_lazy('message:recipient_list')


class MailingRecipientDetailView(DetailView):
    """ Класс реализующий интерфейс для отображения детальной информации о получателе сообщения """
    model = MailingRecipient
    template_name = "message/recipient_detail.html"
    context_object_name = 'recipient'


class MessageCreateView(CreateView):
    """ Класс реализующий интерфейс для создания сообщения """

    model = Message
    template_name = 'message/message_add.html'
    fields = ['subject', 'text',]
    context_object_name = 'message'
    success_url = reverse_lazy('message:message_list')


class MessageListView(ListView):
    """ Класс реализующий интерфейс для отобраения информации о сообщениях """

    model = Message
    template_name = 'message/message_list.html'
    context_object_name = 'messages'


class MessageUpdateView(UpdateView):
    """ Класс реализующий интерфейс для детельной информации о сообщений """

    model = Message
    template_name = 'message/message_add.html'
    fields = ['subject', 'text',]
    context_object_name = 'message'
    success_url = reverse_lazy('message:message_list')


class MessageDeleteView(DeleteView):
    """ Класс реализующий интерфейс для удаления информации о сообщений """

    model =  Message
    template_name = 'message/message_delete_confirm.html'
    context_object_name = 'message'
    success_url = reverse_lazy('message:message_list')

class MessageDetailView(DetailView):
    """ Класс реализующий интерфейс для отображения детальной информации о сообщении """
    model = Message
    template_name = "message/message_detail.html"
    context_object_name = 'message'


class DistributionCreateView(CreateView):
    """ Класс реализующий интерфейс для создания рассылки """

    model = Distribution
    template_name = 'message/distribution_add.html'
    fields = ['message', 'recipients',]
    context_object_name = 'distribution'
    success_url = reverse_lazy('message:distribution_list')


class DistributionListView(ListView):
    """ Класс реализующий интерфейс для отображения рассылки """

    model = Distribution
    template_name = 'message/distribution_list.html'
    context_object_name = 'distributions'


class DistributionUpdateView(UpdateView):
    """ Класс реализующий интерфейс для изменения рассылки """

    model = Distribution
    template_name = 'message/distribution_add.html'
    fields = ['message', 'recipients',]
    context_object_name = 'distribution'
    success_url = reverse_lazy('message:distribution_list')


class DistributionDeleteView(DeleteView):
    """ Класс реализующий интерфейс для удаления рассылки """

    model =  Distribution
    template_name = 'message/distribution_delete_confirm.html'
    context_object_name = 'distribution'
    success_url = reverse_lazy('message:distribution_list')


class DistributionDetailView(DetailView):
    """ Класс реализующий интерфейс для отображения детальной информации о рассылке """
    model = Distribution
    template_name = "message/distribution_detail.html"
    context_object_name = 'distribution'

