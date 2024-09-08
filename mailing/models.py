from django.db import models

from client.models import Client
from message.models import Message

NULLEBLE = {"null": True, "blank": True}


class Mailing(models.Model):
    PERIODICITY_CHOICES = [
        ("day", "День"),
        ("week", "Неделя"),
        ("month", "Месяц"),
        ("year", "Год"),
    ]
    STATUS_CHOICES = [
        ("completed", "Завершена"),
        ("created", "Создана"),
        ("running", "Запущена"),
    ]

    clients = models.ManyToManyField(
        Client, verbose_name="Клиенты", related_name="mailing_list"
    )
    messages = models.OneToOneField(
        Message, on_delete=models.CASCADE, verbose_name="Сообщения"
    )

    send_at = models.DateTimeField(
        **NULLEBLE,
        verbose_name="Дата и время отправки",
    )
    frequency = models.PositiveIntegerField(default=1, verbose_name="Частота отправки")
    periodicity = models.CharField(
        max_length=10,
        choices=PERIODICITY_CHOICES,
        verbose_name="Периодичность отправки",
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="created", verbose_name="Статус"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Рассылка {self.status} на {self.send_at}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
