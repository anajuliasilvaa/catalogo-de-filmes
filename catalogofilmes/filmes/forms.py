from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields= ['titulo', 'sinopse', 'ano_publicacao', 'duracao', 'poster']
        labels = {'text': '', 'sinopse': '', 'ano_publicacao': '', 'duracao': '', 'poster': ''}
