from django.urls import path

from . import views

urlpatterns = [
   path ('criar/', views.criar_operadora, name="criar_operadora"),

]
