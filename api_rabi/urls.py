
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path ("equipamentos/", include("equipamentos.urls")),
    path ("documentos/", include("documentos.urls")),
    path ("operadora/", include("operadora.urls")),
]
