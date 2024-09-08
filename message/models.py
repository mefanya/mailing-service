from django.db import models

NULLEBLE = {"null": True, "blank": True}

class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name='Тема')
    textbox = models.TextField(verbose_name='Текст сообщения')
    
    def __str__(self) -> str:
        return self.textbox
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
