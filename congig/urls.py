from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mailing.urls", namespace="mailing")),
    path("client/", include("client.urls", namespace="client")),
    path("message/", include("message.urls", namespace="message")),
]
