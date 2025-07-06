from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addFilme', views.adicionar_filme, name='addFilme'),
    path("editar_filme/<int:id>", views.editar_filme, name ='editar_filme'),
    path('filme/<int:id>/deletar', views.deletar_filme, name='delete'),
    path('filme/<int:id>/', views.detalhar_filme, name='detalhes_filme'),
]