from django.contrib import admin
from django.urls import path
from .views import ocultar, revelar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ocultar', ocultar, name='ocultar'),
    path('revelar', revelar, name='revelar'),
]