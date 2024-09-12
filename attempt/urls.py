from django.urls import path
from attempt.views import attempt_list
from attempt.apps import AttemptConfig

app_name = AttemptConfig.name

urlpatterns = [
    path("attempts/", attempt_list, name="attempt_list"),
]
