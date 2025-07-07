from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'sinopse', 'ano_publicacao', 'duracao', 'poster', 'generos']
        labels = {
            'titulo': 'Título',
            'sinopse': 'Sinopse',
            'ano_publicacao': 'Ano de Publicação',
            'duracao': 'Duração',
            'poster': 'Pôster',
            'generos': 'Gêneros'
        }
        widgets = {
            'generos': forms.CheckboxSelectMultiple(),  
        }
