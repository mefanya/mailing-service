from django.urls import path
from attempt.views import attempt_list
from mailing.apps import MailingConfig

from congig import settings

app_name = MailingConfig.name

urlpatterns = [
    path("", attempt_list, name="attempt_list"),
]
