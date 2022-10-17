from django.db import models


class CmsSlider(models.Model):
    # default dir for img is 'media', lets change it to 'media/sliderimage'
    cms_img = models.ImageField(upload_to='sliderimage/', verbose_name='Картинки для слайдера')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Текст')
    # атрибут нужен для работы "карусели". В админке только одному обьекту установим "cms_css = active"
    # в шаблоне для обьекта : <div class="carousel-item {{ slide.cms_css }}">...</div>
    cms_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS class')

    # строковое представление обьекта
    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
