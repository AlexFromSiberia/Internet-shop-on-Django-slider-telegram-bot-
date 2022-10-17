from django.contrib import admin
from .models import CmsSlider
from django.utils.safestring import mark_safe


class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_photo')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)

    # функция для отображения миниатюр изображений в админке
    # import mark_safe !
    # get_photo --> list_display
    def get_photo(self, obj):
        # избежать ошибки если фото не существует
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="100">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


# Register your apps here
admin.site.register(CmsSlider, CmsAdmin)
