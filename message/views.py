
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, View

from .models import MailingRecipient, Message, Distribution, AttemptedMailing
from .services import send_message, attempted_mailing


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


class SendMessageView(View):
    """ Класс ревлизующий интерфейс для отправки сообщения """

    def post(self, request,  *args, **kwargs):
        distribution_id = kwargs["pk"]
        error = send_message(distribution_id)
        attempted_mailing(distribution_id, error)
        return redirect('message:distribution_list')

class IndexListView(ListView):
    """ Класс ревлизующий интерфейс главной страницы """

    model = Distribution
    template_name = "message/index.html"
    context_object_name = 'distribution'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['distribution_count_launched'] = Distribution.objects.filter(status='Запущена').count()
        context['recipient_count'] = MailingRecipient.objects.count()
        return context


class StatisticView(ListView):
    """ Класс реализующий интерфейс для отобраения информации о попытках рассылок для зарегистрированного пользователя """

    model = Distribution
    template_name = "message/statistic.html"
    context_object_name = 'distribution'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        attempted = AttemptedMailing.objects.filter(distribution__owner=self.request.user)
        context['attempted_mailing_filter_by_user_successful'] = attempted.filter(status='Успешно').count()
        context['attempted_mailing_filter_by_user_not_successful'] = attempted.filter(status='Не успешно').count()
        context['distribution_count_сompleted'] = Distribution.objects.filter(status='Завершена' ,owner=self.request.user).count()
        return context



