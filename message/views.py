from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .models import MailingRecipient, Message, Distribution


class MailingRecipientCreateView(CreateView):
    model = MailingRecipient
    template_name = 'message/recipient_add.html'
    fields = ['email', 'full_name', 'comment',]
    context_object_name = 'recipient'
    success_url = reverse_lazy('message:recipient_list')


class MailingRecipientListView(ListView):
    model = MailingRecipient
    template_name = 'message/recipient_list.html'
    context_object_name = 'recipients'


class MailingRecipientUpdateView(UpdateView):
    model = MailingRecipient
    template_name = 'message/recipient_add.html'
    fields = ['email', 'full_name', 'comment',]
    context_object_name = 'recipient'
    success_url = reverse_lazy('message:recipient_list')


class MailingRecipientDeleteView(DeleteView):
    model = MailingRecipient
    template_name = 'message/recipient_delete_confirm.html'
    context_object_name = 'recipient'
    success_url = reverse_lazy('message:recipient_list')


class MailingRecipientDetailView(DetailView):
    """ Класс реализующий интерфейс для отображения детальной информации о товаре """
    model = MailingRecipient
    template_name = "'message/recipient_detail.html"
    context_object_name = 'recipient'


class MessageCreateView(CreateView):
    model = Message
    template_name = 'message/message_add.html'
    fields = ['subject', 'text',]
    context_object_name = 'message'
    success_url = reverse_lazy('message:message_list')


class MessageListView(ListView):
    model = Message
    template_name = 'message/message_list.html'
    context_object_name = 'messages'


class MessageUpdateView(UpdateView):
    model = Message
    template_name = 'message/message_add.html'
    fields = ['subject', 'text',]
    context_object_name = 'message'
    success_url = reverse_lazy('message:message_list')


class MessageDeleteView(DeleteView):
    model =  Message
    template_name = 'message/message_delete_confirm.html'
    context_object_name = 'message'
    success_url = reverse_lazy('message:message_list')


class DistributionCreateView(CreateView):
    model = Distribution
    template_name = 'message/distribution_add.html'
    fields = ['message', 'recipients',]
    context_object_name = 'distribution'
    success_url = reverse_lazy('message:distribution_list')


class DistributionListView(ListView):
    model = Distribution
    template_name = 'message/distribution_list.html'
    context_object_name = 'distributions'


class DistributionUpdateView(UpdateView):
    model = Distribution
    template_name = 'message/distribution_add.html'
    fields = ['message', 'recipients',]
    context_object_name = 'distribution'
    success_url = reverse_lazy('message:distribution_list')


class DistributionDeleteView(DeleteView):
    model =  Distribution
    template_name = 'message/distribution_delete_confirm.html'
    context_object_name = 'message'
    success_url = reverse_lazy('message:distribution_list')

