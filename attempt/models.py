from django.db import models
from mailing.models import Mailing

NULLEBLE = {"null": True, "blank": True}


class Attempt(models.Model):
    status = models.BooleanField(verbose_name="Статус попытки", **NULLEBLE)
    response = models.TextField(verbose_name="Ответ сервера", **NULLEBLE)

    mailing = models.ForeignKey(
        Mailing,
        verbose_name="Рассылки",
        on_delete=models.SET_NULL,
        related_name="attempts",
        **NULLEBLE
    )

    time_of_attempted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.status:
            return "Успешная попытка"
        return "Неуспешная попытка"

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"
