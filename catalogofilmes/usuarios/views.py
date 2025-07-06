from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


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
