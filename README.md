# 🎬 Catálogo de Filmes Django

Um sistema completo de catálogo de filmes desenvolvido em Django com sistema de usuários, permissões e avatares Disney.

## 📋 Funcionalidades

### 🎭 Sistema de Filmes
- **Catálogo completo**: Lista paginada de filmes com filtros e ordenação
- **Visualização detalhada**: Página individual com sinopse, ano, diretores e gêneros
- **Gerenciamento CRUD**: Adicionar, editar e excluir filmes (apenas administradores)
- **Upload de pôsters**: Sistema robusto de upload com validação de formatos
- **Relacionamentos**: Integração com diretores e gêneros múltiplos
- **Validação de dados**: Campos obrigatórios e validação de formatos
- **Imagens responsivas**: Pôsters otimizados para diferentes tamanhos de tela

### 👥 Sistema de Usuários e Permissões
- **Autenticação completa**: Login, logout, registro e recuperação de senha
- **Dois tipos de usuário**:
  - **Usuários Gerais**: Visualizam conteúdo, criam listas de favoritos e avaliam filmes
  - **Administradores**: Controle total sobre filmes, diretores, gêneros e usuários
- **Sistema de grupos Django**: Permissões granulares baseadas em grupos
- **Registro automático**: Novos usuários automaticamente no grupo "Usuários Gerais"
- **Decoradores personalizados**: `@admin_required` e `@user_required` para controle de acesso
- **Middleware de autenticação**: Proteção automática de rotas sensíveis

### 📧 Sistema de Perfil e Email
- **Perfil personalizado**: Página individual com avatar Disney e informações
- **Email obrigatório**: Campo validado durante o cadastro
- **Alteração de senha**: Para usuários autenticados com validação
- **Recuperação por email**: Sistema completo de reset com tokens seguros
- **Templates de email**: Emails HTML estilizados e responsivos
- **Configuração SMTP flexível**: Suporte a Gmail e outros provedores
- **Validação de domínio**: Verificação de emails válidos

### 🏰 Sistema de Avatares Disney
- **Avatar automático**: Personagem Disney aleatório no primeiro acesso
- **Galeria interativa**: Interface moderna com 24 personagens por página
- **Sistema de busca inteligente**: Busca por nome com sugestões
- **Paginação avançada**: Navegação fluida entre páginas
- **Avatar aleatório**: Geração instantânea de novo personagem
- **API Disney integrada**: Conexão com `api.disneyapi.dev` com fallback
- **Cache de avatares**: Armazenamento local para performance
- **Tratamento de erros**: Sistema robusto para falhas de API

### 🎬 Sistema de Gêneros
- **Catálogo de gêneros**: Lista completa e organizada
- **Gerenciamento CRUD**: Adicionar, editar e excluir gêneros (administradores)
- **Relacionamento com filmes**: Sistema many-to-many para múltiplos gêneros
- **Validação única**: Prevenção de gêneros duplicados
- **Confirmação de exclusão**: Modal de confirmação para deletar
- **Contagem de filmes**: Quantidade de filmes por gênero
- **Ordenação alfabética**: Lista organizada automaticamente

### 🎭 Sistema de Diretores
- **Perfil completo**: Página individual com biografia e filmografia
- **Upload de fotos**: Sistema de imagens para fotos dos diretores
- **Biografia detalhada**: Campo de texto rico para descrições
- **Filmografia automática**: Lista de filmes dirigidos automaticamente gerada
- **Gerenciamento CRUD**: Controle completo para administradores
- **Busca por diretor**: Filtros e pesquisa na lista de diretores
- **Relacionamento com filmes**: Sistema many-to-many para co-direções
- **Validação de dados**: Campos obrigatórios e formatos validados

### ⭐ Sistema de Favoritos
- **Listas personalizadas**: Criação de listas temáticas de filmes
- **Gerenciamento pessoal**: Cada usuário controla suas próprias listas
- **Múltiplas listas**: Capacidade de criar várias listas (Ex: "Para assistir", "Favoritos")
- **Adição/Remoção**: Interface simples para gerenciar filmes nas listas
- **Visualização organizada**: Listas com capas e informações dos filmes
- **Compartilhamento**: URLs únicas para compartilhar listas
- **Descrição de listas**: Campo personalizado para descrever cada lista
- **Contagem automática**: Número de filmes em cada lista

### 📝 Sistema de Avaliações
- **Avaliação por estrelas**: Sistema de 1 a 5 estrelas para cada filme
- **Comentários detalhados**: Campo de texto para resenhas completas
- **Avaliações por usuário**: Histórico de todas as avaliações do usuário
- **Média de avaliações**: Cálculo automático da nota média por filme
- **Edição de avaliações**: Usuários podem modificar suas próprias avaliações
- **Moderação**: Administradores podem excluir avaliações inapropriadas
- **Validação**: Prevenção de múltiplas avaliações do mesmo usuário por filme
- **Timeline de avaliações**: Exibição cronológica das últimas avaliações

### 🔐 Sistema de Segurança
- **Autenticação Django**: Sistema nativo com hash de senhas
- **Proteção CSRF**: Tokens em todos os formulários
- **Sanitização de dados**: Validação rigorosa de entrada
- **Upload seguro**: Validação de tipos de arquivo para imagens
- **Permissões granulares**: Controle detalhado por funcionalidade
- **Sessões seguras**: Gerenciamento automático de sessões
- **Logs de atividade**: Registro de ações importantes do sistema

### 📱 Interface e Experiência
- **Design responsivo**: Adaptação perfeita para mobile, tablet e desktop
- **Bootstrap 5**: Interface moderna e consistente
- **Navegação intuitiva**: Menu claro e breadcrumbs
- **Feedback visual**: Mensagens de sucesso, erro e aviso
- **Loading states**: Indicadores de carregamento para operações longas
- **Acessibilidade**: Semântica HTML adequada e contraste de cores
- **Performance otimizada**: Carregamento rápido com assets minificados

### 🛠️ Funcionalidades Administrativas
- **Django Admin**: Interface administrativa completa
- **Relatórios**: Estatísticas de filmes, usuários e avaliações
- **Backup de dados**: Comandos para exportar/importar dados
- **Logs de sistema**: Monitoramento de atividades e erros
- **Comandos personalizados**: `criar_grupos` e `criar_perfis`
- **Migração de dados**: Scripts para atualização de banco
- **Configuração flexível**: Settings para desenvolvimento e produção

### 🔌 Integrações e APIs
- **API Disney**: Integração completa para avatares de personagens
- **SMTP Gmail**: Configuração de envio de emails automáticos
- **Sistema de Upload**: Integração com sistema de arquivos local
- **Processamento de imagens**: Redimensionamento automático de pôsters
- **Cache inteligente**: Sistema de cache para performance
- **CDN Ready**: Preparado para integração com CDNs
- **RESTful Structure**: Arquitetura preparada para APIs futuras

### 📊 Analytics e Monitoramento
- **Contadores automáticos**: Número de filmes, usuários, avaliações
- **Estatísticas de uso**: Filmes mais avaliados e bem classificados
- **Logs detalhados**: Registro de ações de usuários e administradores
- **Métricas de performance**: Tempo de carregamento e uso de recursos
- **Relatórios de erro**: Sistema de captura e análise de erros
- **Dashboard administrativo**: Visão geral do sistema no Django Admin

### 🚀 Performance e Otimização
- **Consultas otimizadas**: Use de select_related e prefetch_related
- **Imagens comprimidas**: Otimização automática de uploads
- **Cache de templates**: Sistema de cache para páginas frequentes
- **Lazy loading**: Carregamento progressivo de imagens
- **Assets minificados**: CSS e JS otimizados para produção
- **Database indexing**: Índices otimizados para consultas rápidas

### 🔄 Automação e Scripts
- **Comandos Django**: Scripts personalizados para manutenção
- **Backup automático**: Rotinas de backup de banco de dados
- **Limpeza de arquivos**: Remoção de arquivos órfãos de mídia
- **Sincronização de dados**: Scripts para atualizar informações
- **Validação de integridade**: Verificação de consistência de dados
- **Deploy automatizado**: Scripts para produção

### 🌐 Internacionalização e Localização
- **Interface em português**: Totalmente traduzida
- **Formatação de datas**: Padrão brasileiro (DD/MM/AAAA)
- **Mensagens localizadas**: Feedbacks em português
- **Timezone configurado**: Horário de Brasília por padrão
- **Validações locais**: Formatos brasileiros para dados
- **Preparado para i18n**: Estrutura para múltiplos idiomas

### ♿ Acessibilidade e Usabilidade
- **Navegação por teclado**: Suporte completo a navegação via Tab
- **Screen readers**: Compatibilidade com leitores de tela
- **Contraste adequado**: Cores que atendem padrões de acessibilidade
- **Textos alternativos**: Alt text em todas as imagens
- **Foco visível**: Indicadores claros de foco nos elementos
- **ARIA labels**: Semântica adequada para assistive technologies
- **Responsive design**: Interface adaptável para todos os dispositivos

### 🔮 Funcionalidades Futuras (Roadmap)
- **Sistema de Comentários**: Discussões em tempo real sobre filmes
- **Recomendações IA**: Sistema inteligente de sugestões personalizadas
- **API RESTful**: Endpoints para integração com apps móveis
- **Sistema de Notificações**: Alertas para novos filmes e avaliações
- **Chat em Tempo Real**: Comunicação entre usuários
- **Sistema de Conquistas**: Badges e gamificação para usuários ativos
- **Integração com Streamings**: Links para plataformas como Netflix, Prime
- **Modo Escuro**: Interface com tema escuro
- **PWA (Progressive Web App)**: Instalação como app nativo
- **Exportação de Dados**: Download de listas em PDF/Excel
- **Sistema de Seguir Usuários**: Rede social de cinéfilos
- **Trailers Integrados**: Player de vídeos do YouTube/Vimeo

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.12** - Linguagem de programação principal
- **Django 4.x** - Framework web robusto e escalável
- **SQLite** - Banco de dados para desenvolvimento
- **Django Admin** - Interface administrativa
- **Django Forms** - Validação e processamento de formulários
- **Django Auth** - Sistema de autenticação e autorização

### Frontend
- **HTML5** - Estrutura semântica das páginas
- **CSS3** - Estilização avançada e animações
- **JavaScript ES6+** - Interatividade e funcionalidades dinâmicas
- **Bootstrap 5** - Framework CSS responsivo
- **jQuery** - Manipulação DOM e AJAX

### Integrações
- **API Disney** - Avatares de personagens Disney
- **Gmail SMTP** - Envio de emails transacionais
- **Requests** - Cliente HTTP para APIs externas

### Ferramentas de Desenvolvimento
- **Git** - Controle de versão
- **GitHub** - Repositório e colaboração
- **VS Code** - Editor de código recomendado
- **Python Virtual Environment** - Isolamento de dependências

## 📁 Estrutura do Projeto

```
Catalogo-Filmes/
├── catalogofilmes/
│   ├── catalogofilmes/          # Configurações principais
│   │   ├── __init__.py
│   │   ├── settings.py          # Configurações do Django
│   │   ├── urls.py              # URLs principais
│   │   ├── wsgi.py              # WSGI config
│   │   └── asgi.py              # ASGI config
│   ├── filmes/                  # App de filmes
│   │   ├── __init__.py
│   │   ├── models.py            # Modelo Filme
│   │   ├── views.py             # Views dos filmes
│   │   ├── urls.py              # URLs dos filmes
│   │   ├── forms.py             # Formulários
│   │   ├── admin.py             # Configuração admin
│   │   ├── apps.py              # Configuração da app
│   │   ├── tests.py             # Testes
│   │   └── migrations/          # Migrações do banco
│   │       ├── __init__.py
│   │       ├── 0001_initial.py
│   │       ├── 0002_filme_generos.py
│   │       ├── 0003_filme_diretor.py
│   │       └── 0004_remove_filme_diretor_filme_diretores.py
│   ├── usuarios/                # App de usuários
│   │   ├── __init__.py
│   │   ├── models.py            # Modelo Profile
│   │   ├── views.py             # Views de usuários
│   │   ├── urls.py              # URLs de usuários
│   │   ├── forms.py             # Formulários
│   │   ├── admin.py             # Configuração admin
│   │   ├── apps.py              # Configuração da app
│   │   ├── tests.py             # Testes
│   │   ├── decorators.py        # Decoradores personalizados
│   │   ├── disney_service.py    # Serviço da API Disney
│   │   ├── migrations/          # Migrações do banco
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py
│   │   └── management/
│   │       └── commands/
│   │           ├── __init__.py
│   │           ├── criar_grupos.py    # Comando para criar grupos
│   │           └── criar_perfis.py    # Comando para criar perfis
│   ├── genero/                  # App de gêneros
│   │   ├── __init__.py
│   │   ├── models.py            # Modelo Genero
│   │   ├── views.py             # Views de gêneros
│   │   ├── urls.py              # URLs de gêneros
│   │   ├── forms.py             # Formulários
│   │   ├── admin.py             # Configuração admin
│   │   ├── apps.py              # Configuração da app
│   │   ├── tests.py             # Testes
│   │   └── migrations/          # Migrações do banco
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   ├── diretores/               # App de diretores
│   │   ├── __init__.py
│   │   ├── models.py            # Modelo Diretor
│   │   ├── views.py             # Views de diretores
│   │   ├── urls.py              # URLs de diretores
│   │   ├── forms.py             # Formulários
│   │   ├── admin.py             # Configuração admin
│   │   ├── apps.py              # Configuração da app
│   │   ├── tests.py             # Testes
│   │   └── migrations/          # Migrações do banco
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   ├── avaliacoes/              # App de avaliações
│   │   ├── __init__.py
│   │   ├── models.py            # Modelo Avaliacao
│   │   ├── views.py             # Views de avaliações
│   │   ├── urls.py              # URLs de avaliações
│   │   ├── forms.py             # Formulários
│   │   ├── admin.py             # Configuração admin
│   │   ├── apps.py              # Configuração da app
│   │   ├── tests.py             # Testes
│   │   └── migrations/          # Migrações do banco
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   ├── favoritos/               # App de favoritos
│   │   ├── __init__.py
│   │   ├── models.py            # Modelo Favorito
│   │   ├── views.py             # Views de favoritos
│   │   ├── urls.py              # URLs de favoritos
│   │   ├── forms.py             # Formulários
│   │   ├── admin.py             # Configuração admin
│   │   ├── apps.py              # Configuração da app
│   │   ├── tests.py             # Testes
│   │   └── migrations/          # Migrações do banco
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   ├── templates/               # Templates HTML
│   │   ├── base.html            # Template base
│   │   ├── filmes/              # Templates de filmes
│   │   │   ├── index.html
│   │   │   ├── detalhes_filme.html
│   │   │   ├── adicionar_filmes.html
│   │   │   └── edit_filmes.html
│   │   ├── usuarios/            # Templates de usuários
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── perfil.html
│   │   │   ├── alterar_senha.html
│   │   │   ├── escolher_avatar.html
│   │   │   ├── password_reset_form.html
│   │   │   ├── password_reset_done.html
│   │   │   ├── password_resetconfirm.html
│   │   │   └── password_reset_complete.html
│   │   ├── genero/              # Templates de gêneros
│   │   │   ├── listar.html
│   │   │   ├── form.html
│   │   │   └── confirmar_delete.html
│   │   ├── diretores/           # Templates de diretores
│   │   │   ├── lista_diretores.html
│   │   │   ├── detalhes_diretor.html
│   │   │   ├── adicionar_diretor.html
│   │   │   └── editar_diretor.html
│   │   ├── avaliacoes/          # Templates de avaliações
│   │   │   ├── adicionar_avaliacao.html
│   │   │   ├── editar_avaliacao.html
│   │   │   └── deletar_avaliacao.html
│   │   ├── favoritos/           # Templates de favoritos
│   │   │   ├── minhas_listas.html
│   │   │   ├── criar_lista.html
│   │   │   ├── detalhes_lista.html
│   │   │   ├── editar_lista.html
│   │   │   └── confirmar_delete_lista.html
│   │   └── registration/        # Templates de autenticação
│   │       └── password_reset_email.html
│   ├── static/                  # Arquivos estáticos
│   │   ├── css/
│   │   │   └── footer.css
│   │   └── img/
│   │       ├── aba.png
│   │       └── logo.png
│   ├── staticfiles/             # Arquivos estáticos coletados
│   │   ├── admin/               # Arquivos do Django Admin
│   │   └── css/
│   │       └── footer.css
│   ├── media/                   # Arquivos de mídia
│   │   ├── posters/             # Pôsters dos filmes
│   │   └── diretores_fotos/     # Fotos dos diretores
│   ├── db.sqlite3               # Banco de dados SQLite
│   ├── requirements.txt         # Dependências do projeto
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

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

### Resumo da Licença MIT
- ✅ Uso comercial permitido
- ✅ Modificação permitida
- ✅ Distribuição permitida
- ✅ Uso privado permitido
- ❌ Sem garantia ou responsabilidade

---

**Desenvolvido com ❤️ usando Django**

*Um projeto de catálogo de filmes completo e moderno, pronto para uso pessoal ou comercial.*
