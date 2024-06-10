from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('cadastrar/turma/', views.CadastrarTurma.as_view(), name='cadastrar_turma'),
    path('atividades/<int:pk>', views.ListarAtividades.as_view(), name='listar_atividades'),
    path('cadastrar/atividade/<int:pk>', views.CadastrarAtividade.as_view(), name='cadastrar_atividade'),
    path('deletar-turma/<int:pk>', views.DeletarTurma.as_view(), name='deletar_turma'),
]
