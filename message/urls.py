from django.urls import path
from django.conf.urls.static import static
from mailing.apps import MailingConfig

from congig import settings

app_name = MailingConfig.name

urlpatterns = [
    path(),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)