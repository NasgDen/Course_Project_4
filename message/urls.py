from django.urls import path
from message.apps import MessageConfig

from .views import MailingRecipientListView, MailingRecipientCreateView, MailingRecipientUpdateView, \
    MailingRecipientDeleteView, MailingRecipientDetailView, MessageListView, MessageCreateView, MessageUpdateView, \
    MessageDeleteView

app_name = MessageConfig.name

urlpatterns = [
    path('recipient_list/',MailingRecipientListView.as_view(), name='recipient_list'),
    path('recipient_add/', MailingRecipientCreateView.as_view(), name='recipient_add'),
    path('recipient_update/<int:pk>/', MailingRecipientUpdateView.as_view(), name='recipient_update'),
    path('recipient_delete/<int:pk>/', MailingRecipientDeleteView.as_view(), name='recipient_delete'),
    path('recipient_detail/<int:pk>/', MailingRecipientDetailView.as_view(), name='recipient_detail'),
    path('message_list/',MessageListView.as_view(), name='message_list'),
    path('message_add/', MessageCreateView.as_view(), name='message_add'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
]