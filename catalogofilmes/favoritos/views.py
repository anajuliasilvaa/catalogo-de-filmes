# catalogofilmes/favoritos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required 

from .models import ListaFavoritos
from .forms import ListaFavoritosForm
from filmes.models import Filme 
from django.http import JsonResponse


@login_required
def minhas_listas(request):
    """Lista as listas de favoritos do usuário logado."""
    listas = ListaFavoritos.objects.filter(usuario=request.user).order_by('nome')
    context = {'listas': listas}
    return render(request, 'favoritos/minhas_listas.html', context)


@login_required
def criar_lista(request):
    """Permite ao usuário logado criar uma nova lista de favoritos."""
    if request.method == 'POST':
        form = ListaFavoritosForm(request.POST)
        if form.is_valid():
            nova_lista = form.save(commit=False)
            nova_lista.usuario = request.user 
            nova_lista.save()
            form.save_m2m() 
            return redirect(reverse('favoritos:detalhes_lista', args=[nova_lista.id]))
    else:
        form = ListaFavoritosForm()
    context = {'form': form}
    return render(request, 'favoritos/criar_lista.html', context)


@login_required
def detalhes_lista(request, lista_id):
    """Mostra os detalhes de uma lista de favoritos."""
    lista = get_object_or_404(ListaFavoritos, id=lista_id)

    if lista.usuario != request.user:
        return redirect(reverse('favoritos:minhas_listas')) 

    context = {'lista': lista}
    return render(request, 'favoritos/detalhes_lista.html', context)


@login_required
def editar_lista(request, lista_id):
    """Permite ao usuário logado editar uma de suas listas de favoritos."""
    lista = get_object_or_404(ListaFavoritos, id=lista_id, usuario=request.user)

    if request.method == 'POST':
        form = ListaFavoritosForm(request.POST, instance=lista)
        if form.is_valid():
            form.save() 
            return redirect(reverse('favoritos:detalhes_lista', args=[lista.id]))
    else:
        form = ListaFavoritosForm(instance=lista)
    context = {'form': form, 'lista': lista}
    return render(request, 'favoritos/editar_lista.html', context)


@login_required
def deletar_lista(request, lista_id):
    """Permite ao usuário logado deletar uma de suas listas de favoritos."""
    lista = get_object_or_404(ListaFavoritos, id=lista_id, usuario=request.user) 
    if request.method == 'POST':
        lista.delete()
        return redirect(reverse('favoritos:minhas_listas'))

    return render(request, 'favoritos/confirmar_delete_lista.html', {'lista': lista}) 