from django.urls import path

from . import views

urlpatterns = [
   path ('criar/', views.criar_equipamento, name="criar_equipamento"),

]
