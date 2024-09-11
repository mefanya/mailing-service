from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mailing.urls", namespace="mailing")),
    path("", include("client.urls", namespace="client")),
    path("", include("message.urls", namespace="message")),
    path("", include("attempt.urls", namespace="attempt")),
]
