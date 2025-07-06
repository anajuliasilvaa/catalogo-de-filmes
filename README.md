# 🎬 Catálogo de Filmes Django

Um sistema completo de catálogo de filmes desenvolvido em Django com sistema de usuários, permissões e avatares Disney.

## 📋 Funcionalidades

### 🎭 Sistema de Filmes
- **Visualização de filmes**: Lista completa com pôsters e informações
- **Detalhes do filme**: Página individual com todas as informações
- **Gerenciamento CRUD**: Adicionar, editar e excluir filmes (apenas administradores)
- **Upload de pôsters**: Sistema de upload de imagens para capas dos filmes

### 👥 Sistema de Usuários e Permissões
- **Dois tipos de usuário**:
  - **Usuários Gerais**: Podem visualizar filmes e detalhes
  - **Administradores**: Podem gerenciar filmes (adicionar, editar, excluir)
- **Sistema de grupos Django**: Permissões baseadas em grupos
- **Registro automático**: Novos usuários são automaticamente adicionados ao grupo "Usuários Gerais"

### 📧 Sistema de Perfil e Email
- **Perfil do usuário**: Página individual com informações pessoais
- **Email no registro**: Campo obrigatório durante o cadastro
- **Alteração de senha**: Para usuários logados
- **Redefinição de senha por email**: Para usuários que esqueceram a senha
- **Configuração SMTP**: Integração com Gmail para envio de emails

### 🏰 Sistema de Avatares Disney
- **Avatar automático**: Personagem Disney aleatório atribuído no registro
- **Galeria de seleção**: Interface com 24 personagens por página
- **Sistema de busca**: Busca personagens por nome
- **Paginação**: Navegação entre páginas de personagens
- **Avatar aleatório**: Botão para gerar novo avatar instantaneamente
- **Integração com API Disney**: Utiliza a API oficial da Disney para buscar personagens

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Django 4.x**
- **SQLite** (banco de dados)
- **HTML/CSS** (templates)
- **Bootstrap** (estilização)
- **API Disney** (avatares)
- **Gmail SMTP** (envio de emails)

## 📁 Estrutura do Projeto

```
Catalogo-Filmes/
├── catalogofilmes/
│   ├── catalogofilmes/          # Configurações principais
│   │   ├── settings.py          # Configurações do Django
│   │   ├── urls.py              # URLs principais
│   │   └── wsgi.py              # WSGI config
│   ├── filmes/                  # App de filmes
│   │   ├── models.py            # Modelo Filme
│   │   ├── views.py             # Views dos filmes
│   │   ├── urls.py              # URLs dos filmes
│   │   └── forms.py             # Formulários
│   ├── usuarios/                # App de usuários
│   │   ├── models.py            # Modelo Profile
│   │   ├── views.py             # Views de usuários
│   │   ├── urls.py              # URLs de usuários
│   │   ├── disney_service.py    # Serviço da API Disney
│   │   └── management/
│   │       └── commands/
│   │           ├── criar_grupos.py    # Comando para criar grupos
│   │           └── criar_perfis.py    # Comando para criar perfis
│   ├── templates/               # Templates HTML
│   │   ├── base.html            # Template base
│   │   ├── filmes/              # Templates de filmes
│   │   └── usuarios/            # Templates de usuários
│   ├── media/                   # Arquivos de mídia
│   │   └── posters/             # Pôsters dos filmes
│   └── manage.py                # Script de gerenciamento Django
├── LICENSE
└── README.md
```

## ⚙️ Configuração e Instalação

### 1. Pré-requisitos
```bash
python 3.12+
pip
```

### 2. Clonar o repositório
```bash
git clone [URL_DO_REPOSITORIO]
cd Catalogo-Filmes/catalogofilmes
```

### 3. Instalar dependências
```bash
pip install django
pip install requests
```

### 4. Configurar banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar grupos de usuários
```bash
python manage.py criar_grupos
```

### 6. Criar perfis para usuários existentes (se houver)
```bash
python manage.py criar_perfis
```

### 7. Criar superusuário
```bash
python manage.py createsuperuser
```

### 8. Executar o servidor
```bash
python manage.py runserver
```

## 🚀 Como Usar

### Acesso ao Sistema
1. Acesse `http://localhost:8000`
2. Faça login ou registre-se
3. Explore o catálogo de filmes

### Para Usuários Gerais
- Visualizar lista de filmes
- Ver detalhes de cada filme
- Acessar perfil pessoal
- Alterar senha
- Escolher avatar Disney

### Para Administradores
- Todas as funcionalidades de usuários gerais
- Adicionar novos filmes
- Editar filmes existentes
- Excluir filmes
- Gerenciar usuários via Django Admin
- usuario : adm
- senha: Admin123#

### Configuração de Email
Para ativar o envio de emails, configure as seguintes variáveis no `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-senha-de-app'
```

## 🎨 Funcionalidades Detalhadas

### Sistema de Permissões
- **Grupos automatizados**: Usuários são automaticamente atribuídos a grupos
- **Decoradores personalizados**: `@admin_required` e `@user_required`
- **Templates dinâmicos**: Botões aparecem apenas para usuários com permissão

### Sistema de Avatares Disney
- **API Integration**: Conecta com `https://api.disneyapi.dev/character`
- **Busca inteligente**: Múltiplas estratégias de busca por nome
- **Cache local**: Informações do avatar armazenadas no perfil
- **Fallback**: Sistema robusto para lidar com falhas da API

### Sistema de Email
- **Templates personalizados**: Emails HTML estilizados
- **Redefinição segura**: Tokens temporários para redefinição de senha
- **Configuração flexível**: Suporte a diferentes provedores SMTP

## 🔧 Comandos Úteis

### Gerenciamento de Grupos
```bash
# Criar grupos e permissões
python manage.py criar_grupos

# Verificar grupos existentes
python manage.py shell
>>> from django.contrib.auth.models import Group
>>> Group.objects.all()
```

### Gerenciamento de Perfis
```bash
# Criar perfis para usuários existentes
python manage.py criar_perfis

# Verificar perfis
python manage.py shell
>>> from usuarios.models import Profile
>>> Profile.objects.all()
```

### Limpeza de Dados
```bash
# Limpar cache
python manage.py collectstatic

# Limpar sessões expiradas
python manage.py clearsessions
```

## 📊 Modelos de Dados

### Filme
```python
class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano = models.IntegerField()
    diretor = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    data_criacao = models.DateTimeField(auto_now_add=True)
```

### Profile
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.URLField(blank=True, null=True)
    avatar_name = models.CharField(max_length=200, blank=True, null=True)
```

## 🔐 Segurança

- **Autenticação Django**: Sistema nativo do Django
- **Permissões granulares**: Baseadas em grupos
- **Validação de formulários**: Proteção contra ataques
- **CSRF Protection**: Tokens CSRF em todos os formulários
- **Sanitização de dados**: Validação de entrada de dados

## 📱 Responsividade

- **Design responsivo**: Interface adaptável para diferentes dispositivos
- **Bootstrap integration**: Componentes estilizados
- **Mobile-first**: Otimizado para dispositivos móveis

## 🤝 Contribuição

1. Faça fork do projeto
2. Crie sua branch de feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🎯 Próximas Funcionalidades

- [ ] Sistema de avaliações e comentários
- [ ] Filtros avançados de busca
- [ ] Wishlist de filmes
- [ ] Notificações por email
- [ ] API REST para mobile
- [ ] Integração com outras APIs de filmes

## 🆘 Suporte

Se você encontrar algum problema ou tiver dúvidas:

1. Verifique a documentação
2. Procure por issues semelhantes
3. Abra uma nova issue com detalhes do problema
4. Inclua logs de erro e passos para reproduzir

---

**Desenvolvido com ❤️ usando Django**
