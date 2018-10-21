from django.urls import path
from . import views as eventos

app_name = 'eventos'

urlpatterns = [
    path('', eventos.MeusEventos.as_view(), name='meus-eventos'),
    path('adicionar/evento', eventos.AddEvento.as_view(), name='add-evento'),
    path('deletar/evento/<pk>', eventos.DeletarEvento.as_view(), name='deletar-evento'),
    path('editar/evento/<pk>', eventos.EditarEvento.as_view(), name='editar-evento'),
    path('detalhes/evento/<pk>', eventos.DetalhesEvento.as_view(), name='detalhes-evento'),
    path('eventos/disponiveis', eventos.EventosDisponiveis.as_view(), name='eventos-disponiveis'),
    path('adicionar/minicurso', eventos.AddMinicurso.as_view(), name='add-minicurso'),
    path('adicionar/palestra', eventos.AddPalestra.as_view(), name='add-palestra'),
    path('inscrever/minicurso/<pk>', eventos.InscreverMinicurso.as_view(), name='inscrever-minicurso'),
    path('inscrever/palestra/<pk>', eventos.InscreverPalestra.as_view(), name='inscrever-palestra'),
    path('lista/minicurso/<pk>', eventos.GerarListaMinicurso.as_view(), name='gerar-lista-m'),
    path('lista/palestra/<pk>', eventos.GerarListaPalestra.as_view(), name='gerar-lista-p'),
    path('adicionar/palestrante', eventos.AddPalestrante.as_view(), name='add-palestrante'),
]
