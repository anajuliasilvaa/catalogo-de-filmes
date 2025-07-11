from django import forms
from .models import Filme
from diretores.models import Diretor

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'sinopse', 'ano_publicacao', 'duracao', 'poster', 'generos', 'diretores']
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
