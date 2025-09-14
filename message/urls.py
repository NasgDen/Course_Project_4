from django.urls import path
from message.apps import MessageConfig

from .views import MailingRecipientListView, MailingRecipientCreateView, MailingRecipientUpdateView, MailingRecipientDeleteView

app_name = MessageConfig.name

urlpatterns = [
    path('recipient_list/',MailingRecipientListView.as_view(), name='recipient_list'),
    path('recipient_add/', MailingRecipientCreateView.as_view(), name='recipient_add'),
    path('recipient_update/<int:pk>/', MailingRecipientUpdateView.as_view(), name='recipient_update'),
    path('recipient_delete/<int:pk>/', MailingRecipientDeleteView.as_view(), name='recipient_delete'),
]