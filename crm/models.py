from django.db import models


class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name="Название статуса")

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = "Cтатус"
        verbose_name_plural = "Cтатусы"


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name="Телефон")
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Статус")

    # так отобразится в админке
    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class CommentCrm(models.Model):
    # On_delete=cascade  - при удалении заказа будут удалены комментарии к нему
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    coment_text = models.TextField(verbose_name='Текст комментария')
    coment_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    # так отобразится в админке
    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
