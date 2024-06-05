from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_colaborador, name="criar_colaborador"),

]
