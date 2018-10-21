from django.db import models
from app.core.models import UUIDUser, CreateUpdateModel

class Palestra(CreateUpdateModel):
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE, related_name='eventos', verbose_name='evento')
    nome = models.CharField(max_length=255, verbose_name='nome da palestra')
    palestrante = models.ForeignKey('Palestrante', on_delete=models.CASCADE, related_name='palestrante', verbose_name='palestrante')
    inscritos = models.ManyToManyField(UUIDUser, related_name='inscritos', verbose_name='inscritos', blank=True)
    duracao = models.TimeField(verbose_name='duração')
    data = models.DateField(verbose_name='data da atividade')
    horario = models.TimeField(verbose_name='hora da atividade')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

class MiniCurso(CreateUpdateModel):
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE, related_name='evento', verbose_name='evento')
    nome = models.CharField(max_length=255, verbose_name='nome do minicurso')
    palestrante = models.ForeignKey('Palestrante', on_delete=models.CASCADE, related_name='palestrantes', verbose_name='palestrante')
    inscritos = models.ManyToManyField(UUIDUser, related_name='inscrito', verbose_name='inscritos', blank=True)
    duracao = models.TimeField(verbose_name='duração')
    data = models.DateField(verbose_name='data da atividade')
    horario = models.TimeField(verbose_name='hora da atividade')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'minicurso'
        verbose_name_plural = 'minicursos'

class Evento(CreateUpdateModel):
    dono = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='users', verbose_name='dono do evento')
    nome = models.CharField(max_length=255, verbose_name='nome do evento')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'eventos'
        verbose_name = 'evento'

class Palestrante(CreateUpdateModel):
    nome = models.CharField(max_length=255, verbose_name='nome do palestrante')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'
