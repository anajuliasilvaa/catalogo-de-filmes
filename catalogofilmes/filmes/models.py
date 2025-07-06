from django.db import models

class Filme(models.Model):
    
    titulo = models.CharField(max_length=300)
    sinopse = models.TextField()
    ano_publicacao = models.PositiveIntegerField()
    duracao = models.DurationField(help_text="Formato: hh:mm:ss")
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def __str__(self):
        return self.titulo
