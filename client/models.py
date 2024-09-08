from django.db import models

NULLEBLE = {"null": True, "blank": True}

class Client(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', **NULLEBLE)
    
    fio = models.CharField(max_length=150, verbose_name='Ф.И.О.', editable=False)
    
    def save(self, *args, **kwargs):
        self.fio = f"{self.last_name} {self.first_name} {self.middle_name or ''}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
