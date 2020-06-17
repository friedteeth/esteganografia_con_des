from django.contrib import admin
from django.urls import path
from esteganografia.views import ocultar, revelar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ocultar),
    path('ocultar', ocultar, name='ocultar'),
    path('revelar', revelar, name='revelar'),
]