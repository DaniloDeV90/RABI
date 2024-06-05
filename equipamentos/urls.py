from django.urls import path

from . import views

urlpatterns = [
   path ('criar/', views.criar_equipamento, name="criar_equipamento"),
   path('<int:id>/editar/', views.editar_equipamento, name="editar_equipamento"),
  path('<int:id>/deletar/', views.deletar_equipamento, name="deletar_equipamento")
]
