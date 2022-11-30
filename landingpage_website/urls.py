from django.contrib import admin
from django.urls import path
from crm import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    path('thanks/', views.thanks_page, name='thanks_page'),
]

# подключим картинки из папки 'media'
# Нужно только на этапе разработки, до деплоя (до момента py manage.py collectstatic)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
