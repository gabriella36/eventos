from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View, DetailView
from django.urls import reverse_lazy
from .models import *

class MeusEventos(ListView):
    model = Evento
    template_name = 'eventos/meus-eventos.html'

    def get_context_data(self, **kwargs):
        kwargs['eventos'] = Evento.objects.filter(dono = self.request.user)
        return super(MeusEventos, self).get_context_data(**kwargs)

class EventosDisponiveis(ListView):
    model = Evento
    template_name = 'eventos/eventos-disponiveis.html'

    def get_context_data(self, **kwargs):
        kwargs['eventos'] = Evento.objects.all().exclude(dono = self.request.user)
        return super(EventosDisponiveis, self).get_context_data(**kwargs)

class AddEvento(CreateView):
    template_name = 'eventos/add-evento.html'
    model = Evento
    fields = ['dono', 'nome']
    success_url = reverse_lazy('eventos:meus-eventos')

class EditarEvento(UpdateView):
    model = Evento
    fields = ['nome']
    template_name = 'eventos/editar-evento.html'
    success_url = reverse_lazy('eventos:meus-eventos')

class DetalhesEvento(DetailView):
    model = Evento
    template_name = 'eventos/detalhes-evento.html'

    def get_context_data(self, **kwargs):
        kwargs['minicursos'] = MiniCurso.objects.filter(evento = self.object)
        kwargs['palestras'] = Palestra.objects.filter(evento = self.object)
        return super(DetalhesEvento, self).get_context_data(**kwargs)

class DeletarEvento(DeleteView):
    model = Evento
    success_url = reverse_lazy('eventos:meus-eventos')

class AddMinicurso(CreateView):
    model = MiniCurso
    fields = ['evento', 'nome', 'palestrante', 'duracao', 'data', 'horario']
    success_url = reverse_lazy('eventos:meus-eventos')
    template_name = 'eventos/add-minicurso.html'

class AddPalestra(CreateView):
    model = Palestra
    fields = ['evento', 'nome', 'palestrante', 'duracao', 'data', 'horario']
    success_url = reverse_lazy('eventos:meus-eventos')
    template_name = 'eventos/add-minicurso.html'

class InscreverMinicurso(View):
    def get(self, request, pk):
        minicurso = MiniCurso.objects.filter(id = pk).first()
        minicursos = MiniCurso.objects.filter(evento = minicurso.evento)
        aux = 0
        for atividade in minicursos:
            if self.request.user in atividade.inscritos.all():
                aux += 1
        if aux != 2:
            minicurso.inscritos.add(self.request.user)
            return redirect('eventos:meus-eventos')
        else:
            eventos = Evento.objects.filter(dono = self.request.user)
            return render(request, 'eventos/meus-eventos.html', {'mensagem': 'Você já está inscrito em 2 minicursos', 'eventos': eventos})

class InscreverPalestra(View):
    def get(self, request, pk):
        palestra = Palestra.objects.filter(id = pk).first()
        palestra.inscritos.add(self.request.user)
        return redirect('eventos:meus-eventos')

class GerarListaMinicurso(DetailView):
    model = MiniCurso
    template_name = 'eventos/lista.html'

class GerarListaPalestra(DetailView):
    model = Palestra
    template_name = 'eventos/lista.html'

class AddPalestrante(CreateView):
    model = Palestrante
    fields = ['nome']
    success_url = reverse_lazy('eventos:meus-eventos')
    template_name = 'eventos/add-palestrante.html'
