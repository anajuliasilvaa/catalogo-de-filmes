from django.db import models
from genero.models import Genero
from django.db.models import Avg

class Filme(models.Model):
    
    titulo = models.CharField(max_length=300)
    sinopse = models.TextField()
    ano_publicacao = models.PositiveIntegerField()
    duracao = models.DurationField(help_text="Formato: hh:mm:ss")
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    generos = models.ManyToManyField(Genero, related_name='filmes')

    def __str__(self):
        return self.titulo

    def media_avaliacoes(self):
        media = self.avaliacoes.aggregate(Avg('nota'))['nota__avg']
        if media is None:
            return 0  # Caso não tenha avaliações
        return round(media, 1)