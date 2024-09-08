from django.db import models

NULLEBLE = {"null": True, "blank": True}

class Attempt(models.Model):
    status = models.BooleanField(verbose_name='Статус попытки', **NULLEBLE)
    response = models.TextField(verbose_name='Ответ сервера', **NULLEBLE)
    
    time_of_attempted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.status:
            return "Успешная попытка"
        return "Неуспешная попытка"
    
    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'
