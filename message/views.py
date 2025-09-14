from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

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

