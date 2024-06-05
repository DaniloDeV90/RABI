from django.urls import path

from . import views

urlpatterns = [
   path ('criar/', views.criar_convenio, name="criar_convenio"),

]