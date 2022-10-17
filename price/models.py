from django.db import models


class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    # строковое представление обьекта
    def __str__(self):
        return self.pc_value

    # исправим название в админке
    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Услуга')
    pt_old_price = models.CharField(max_length=200, verbose_name='Старая Цена')
    pt_new_price = models.CharField(max_length=200, verbose_name='Новая Цена')

    # строковое представление обьекта
    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
