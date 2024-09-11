from django.contrib import admin

from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fio",
        "email",
    )
    list_filter = (
        "fio",
        "email",
    )
    search_fields = (
        "fio",
        "email",
    )
