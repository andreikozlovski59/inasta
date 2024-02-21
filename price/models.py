from django.db import models

class Service(models.Model):
    title = models.CharField('Название услуги', max_length=150)
    value = models.DecimalField('Цена услуги', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
