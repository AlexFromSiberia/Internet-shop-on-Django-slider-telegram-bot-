from django.contrib import admin
from .models import CmsSlider
from django.utils.safestring import mark_safe


class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_photo')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_photo')
    readonly_fields = ('get_photo', )

    # функция для отображения миниатюр изображений в админке
    # import mark_safe !
    # get_photo --> list_display
    def get_photo(self, obj):
        # избежать ошибки если фото не существует
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="150">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


# Register your apps here
admin.site.register(CmsSlider, CmsAdmin)
