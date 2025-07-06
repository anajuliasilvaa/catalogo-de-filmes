from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def is_admin_user(user):
    """Verifica se o usuário é um administrador"""
    return user.groups.filter(name='Administradores').exists()


def is_general_user(user):
    """Verifica se o usuário é um usuário geral"""
    return user.groups.filter(name='Usuarios Gerais').exists()


def admin_required(view_func):
    """Decorador que exige que o usuário seja um administrador"""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Se não estiver autenticado, redireciona para o login
            return redirect('login')
            
        if not is_admin_user(request.user):
            messages.error(request, 'Acesso negado. Você precisa ser um administrador para acessar esta página.')
            return redirect('index')
            
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def user_required(view_func):
    """Decorador que exige que o usuário seja um usuário geral ou administrador"""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Se não estiver autenticado, redireciona para o login
            return redirect('login')
            
        if not (is_general_user(request.user) or is_admin_user(request.user)):
            messages.error(request, 'Acesso negado. Você precisa estar logado como usuário do sistema.')
            return redirect('index')
            
        return view_func(request, *args, **kwargs)
    return _wrapped_view 