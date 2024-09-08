from django.db import models

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

    send_at = models.DateTimeField(
        **NULLEBLE,
        DATETIME_FORMAT="%d.%m.%y %H:%M",
        verbose_name="Дата и время отправки"
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
