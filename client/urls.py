from django.urls import path
from django.conf.urls.static import static
from mailing.apps import MailingConfig

from congig import settings
from mailing.views import MailingListView

app_name = MailingConfig.name

urlpatterns = [
    path("", MailingListView.as_view(), name="mailing_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
