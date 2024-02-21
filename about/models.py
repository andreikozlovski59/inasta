from django.db import models
from django.utils import timezone

class About(models.Model):
    name = models.CharField('Введите своё имя',max_length=50)
    message = models.TextField('Напишите свой отзыв',max_length=500)
    date = models.DateTimeField('Дата',default=timezone.now)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'