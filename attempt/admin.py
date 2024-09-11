from django.contrib import admin

from attempt.models import Attempt


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status",
        "mailing",
        "time_of_attempted",
    )
    list_filter = (
        "status",
        "mailing",
    )
