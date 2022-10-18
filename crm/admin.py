from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


# Подключим комментарии к модели заказа (в OrderAdmin дописать "inlines")
class Coment(admin.StackedInline):
    model = CommentCrm
    fields = ('coment_text', 'coment_date', )
    readonly_fields = ('id', 'coment_date',)
    # number of extra comment fields
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'order_dt', 'order_name', 'order_phone', 'order_status', )
    list_display_links = ('id', 'order_dt',)
    list_editable = ('order_name', 'order_phone', 'order_status')
    search_fields = ('order_name', 'order_phone', )
    list_filter = ('order_status', )
    # в read only fields укажем неизменяемые поля, если мы хотим их видеть в fields ()
    # т.е. при переходе в карточку
    readonly_fields = ('id', 'order_dt',)
    fields = ('id', 'order_dt', 'order_name', 'order_phone', 'order_status', )

    # пагинация - по 10 записей на страницу
    list_per_page = 10
    # сколько можно максимально показать при нажатии кнопкт 'show all'
    list_max_show_all = 100
    # Подключим комментарии к модели заказа из "Coment"
    inlines = [Coment, ]


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
