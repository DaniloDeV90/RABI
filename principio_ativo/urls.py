from django.urls import path

from . import views

urlpatterns = [
   path('criar/', views.criar_principio_ativo, name="criar_principio_ativo"),
]