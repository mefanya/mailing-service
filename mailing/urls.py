from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import (
    MailingListView,
    MailingDetailView,
    MailingCreateView,
    MailingUpdateView,
    MailingDeleteView,
)

app_name = MailingConfig.name

urlpatterns = [
    path("", MailingListView.as_view(), name="mailing_list"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing/create", MailingCreateView.as_view(), name="mailing_create"),
    path(
        "mailing/<int:pk>/update/", MailingUpdateView.as_view(), name="mailing_update"
    ),
    path(
        "mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing_delete"
    ),
]
