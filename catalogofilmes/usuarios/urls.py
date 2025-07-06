from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.perfil, name='perfil'),
    path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
    path('escolher-avatar/', views.escolher_avatar, name='escolher_avatar'),
    path('avatar-aleatorio/', views.avatar_aleatorio, name='avatar_aleatorio'),
    
    # URLs para redefinir senha por email
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='usuarios/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        success_url='/usuarios/password-reset-done/'
    ), name='password_reset'),
    
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='usuarios/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='usuarios/password_resetconfirm.html',
        success_url='/usuarios/password-reset-complete/'
    ), name='password_reset_confirm'),
    
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='usuarios/password_reset_complete.html'
    ), name='password_reset_complete'),
]