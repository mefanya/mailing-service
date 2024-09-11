from django.contrib import admin

from mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "send_at",
        "frequency",
        "periodicity",
        "status",
        "created_at",
    )
    list_filter = (
        "status",
        "frequency",
        "periodicity",
    )
