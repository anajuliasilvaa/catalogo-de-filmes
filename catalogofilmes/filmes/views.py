from django.shortcuts import get_object_or_404, render
from .models import Filme
from .forms import FilmeForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):

   filme = Filme.objects.all() 

   return render(request, 'filmes/index.html', {'filmes': filme})


def adicionar_filme(request):
    if request.method != 'POST':
        form = FilmeForm()
    
    else:
        form = FilmeForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    
    context =  {'form': form}
    return render (request, 'filmes/adicionar_filmes.html', context)

def editar_filme(request, id):

   filme = get_object_or_404(Filme, pk=id)

   if request.method != 'POST':
        form = FilmeForm(instance = filme)
   else:
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
         
   return render(request, 'filmes/edit_filmes.html', {'form': form, 'edit': filme})


def deletar_filme(request, id):

    filme= Filme.objects.get(pk=id)
    filme.delete()

    return HttpResponseRedirect(reverse('index'))
   

def detalhar_filme(request, id):
    filme = get_object_or_404(Filme, pk=id)
    return render(request, 'filmes/detalhes_filme.html', {'filme': filme})
