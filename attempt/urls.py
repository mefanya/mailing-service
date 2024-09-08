from django.urls import path
from django.conf.urls.static import static
from attempt.views import attempt_list
from mailing.apps import MailingConfig

from congig import settings

app_name = MailingConfig.name

urlpatterns = [
    path("", attempt_list, name="attempt_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
