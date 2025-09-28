from django.contrib import admin

from .models import AttemptedMailing, Distribution, MailingRecipient, Message


@admin.register(MailingRecipient)
class MailingRecipientAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "full_name",
        "comment",
    )
    list_filter = ("email",)
    search_fields = (
        "email",
        "full_name",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
        "text",
    )
    list_filter = (
        "subject",
        "text",
    )
    search_fields = (
        "subject",
        "text",
    )


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = (
        "datatime_first_sending",
        "datetime_end_sending",
        "status",
    )
    list_filter = ("status",)
    search_fields = ("status",)


@admin.register(AttemptedMailing)
class AttemptedMailingAdmin(admin.ModelAdmin):
    list_display = (
        "attempt_datetime",
        "status",
        "mail_server_response",
    )
    list_filter = ("status",)
    search_fields = ("status",)
