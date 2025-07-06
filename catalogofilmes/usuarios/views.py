from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .disney_service import DisneyAPIService
from .models import Profile


def logout_view (request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            novo_user = form.save()
            
            email = request.POST.get('email', '')
            if email:
                novo_user.email = email
                novo_user.save()
            
            
            disney_character = DisneyAPIService.get_random_character()
            if disney_character:
                novo_user.profile.avatar_url = disney_character.get('imageUrl')
                novo_user.profile.avatar_name = disney_character.get('name')
                novo_user.profile.save()
            
            try:
                grupo_usuarios_gerais = Group.objects.get(name='Usuarios Gerais')
                novo_user.groups.add(grupo_usuarios_gerais)
            except Group.DoesNotExist:
                pass
                
            authenticate_user = authenticate(username = novo_user.username, password = request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('index'))
    
    context = {'form': form}
    return render(request, 'usuarios/register.html', context)


def ensure_user_profile(user):
    if not hasattr(user, 'profile') or user.profile is None:
        try:
            user.profile
        except Profile.DoesNotExist:
            Profile.objects.create(user=user)


@login_required
def perfil(request):
    ensure_user_profile(request.user)
    
    if request.method == 'POST':
        email = request.POST.get('email', '')
        request.user.email = email
        request.user.save()
        messages.success(request, 'Email atualizado com sucesso!')
        return HttpResponseRedirect(reverse('perfil'))
    
    return render(request, 'usuarios/perfil.html')


@login_required
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return HttpResponseRedirect(reverse('perfil'))
    else:
        form = PasswordChangeForm(request.user)
    
    context = {'form': form}
    return render(request, 'usuarios/alterar_senha.html', context)


@login_required 
def escolher_avatar(request):
    ensure_user_profile(request.user)
    
    page = int(request.GET.get('page', 1))
    search_query = request.GET.get('search', '').strip()
    
    if search_query:
        characters = DisneyAPIService.search_characters(search_query)
        disney_data = {
            'data': characters,
            'info': {
                'count': len(characters),
                'totalPages': 1,
                'previousPage': None,
                'nextPage': None
            }
        }
        current_page = 1
    else:
        disney_data = DisneyAPIService.get_characters_page(page, 24)
        current_page = page
    
    if request.method == 'POST':
        avatar_url = request.POST.get('avatar_url')
        avatar_name = request.POST.get('avatar_name')
        
        if avatar_url and avatar_name:
            request.user.profile.avatar_url = avatar_url
            request.user.profile.avatar_name = avatar_name
            request.user.profile.save()
            messages.success(request, f'Avatar alterado para {avatar_name}!')
            return HttpResponseRedirect(reverse('perfil'))
    
    context = {
        'disney_data': disney_data,
        'current_page': current_page,
        'search_query': search_query
    }
    return render(request, 'usuarios/escolher_avatar.html', context)


@login_required
def avatar_aleatorio(request):
    ensure_user_profile(request.user)
    
    disney_character = DisneyAPIService.get_random_character()
    if disney_character:
        request.user.profile.avatar_url = disney_character.get('imageUrl')
        request.user.profile.avatar_name = disney_character.get('name')
        request.user.profile.save()
        messages.success(request, f'Novo avatar aleatório: {disney_character.get("name")}!')
    else:
        messages.error(request, 'Erro ao buscar avatar aleatório. Tente novamente.')
    
    return HttpResponseRedirect(reverse('perfil'))
