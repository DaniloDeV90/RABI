from django.urls import path

from . import views


urlpatterns = [
   path ('criar/', views.criar_documento, name="criar_documento"),

]
