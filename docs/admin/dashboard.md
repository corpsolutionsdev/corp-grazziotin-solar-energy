# Painel Administrativo

O painel administrativo do Django é a interface principal para gerenciar o conteúdo do sistema Grazziotin Energia Solar.

## Acesso

Para acessar o painel administrativo:

1. Inicie o servidor: `python manage.py runserver`
2. Acesse: [http://localhost:8000/admin](http://localhost:8000/admin)
3. Faça login com suas credenciais de superusuário

## Criação de Superusuário

Se ainda não tem um superusuário, crie um:

```bash
python manage.py createsuperuser
```

Siga as instruções para criar:
- Username
- Email
- Senha

## Módulos Disponíveis

### App Principal

#### Quem Somos
- **Localização**: Admin → App → Quem Somos
- **Funcionalidades**:
  - Criar/editar informações sobre a empresa
  - Definir título e descrição
  - Controle de datas de criação/atualização

#### Contato
- **Localização**: Admin → App → Contatos
- **Funcionalidades**:
  - Visualizar mensagens recebidas
  - Marcar como lido/não lido
  - Filtrar por assunto
  - Buscar por nome, email ou mensagem

### Blog

#### Artigos
- **Localização**: Admin → Blog → Artigos
- **Funcionalidades**:
  - Criar/editar artigos do blog
  - Definir título, conteúdo e data
  - Controle de publicação
  - Editor rico para conteúdo

### Projetos

#### Projetos
- **Localização**: Admin → Projects → Projetos
- **Funcionalidades**:
  - Cadastrar projetos realizados
  - Upload de imagens
  - Detalhes técnicos
  - Categorização

### Representantes

#### Representantes
- **Localização**: Admin → Representatives → Representantes
- **Funcionalidades**:
  - Cadastrar representantes
  - Informações de contato
  - Área de atuação
  - Gestão territorial

## Funcionalidades do Admin

### Listagem
- Visualização em tabela de todos os registros
- Paginação automática
- Ordenação por colunas
- Filtros por campos específicos

### Criação
- Formulários automáticos baseados nos modelos
- Validação de dados
- Upload de arquivos
- Campos obrigatórios e opcionais

### Edição
- Interface intuitiva para edição
- Histórico de alterações
- Preview de mudanças
- Salvamento automático

### Exclusão
- Confirmação antes de excluir
- Exclusão em lote
- Proteção contra exclusão acidental

### Busca
- Busca global no painel
- Busca específica por módulo
- Filtros avançados
- Resultados em tempo real

## Personalizações

### Configuração do Admin

O admin está configurado no arquivo `app/admin.py`:

```python
from django.contrib import admin
from .models import QuemSomos, Contato

# Configurar o admin site
admin.site.site_header = "Painel Grazziotin Energia Solar"
admin.site.site_title = "Administração Grazziotin"
admin.site.index_title = "Bem-vindo ao Painel"

@admin.register(QuemSomos)
class QuemSomosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_criacao', 'data_atualizacao']
    search_fields = ['titulo', 'descricao']
    readonly_fields = ['data_criacao', 'data_atualizacao']

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'email', 'assunto', 'data_envio', 'lido']
    list_filter = ['assunto', 'lido', 'data_envio']
    search_fields = ['nome_completo', 'email', 'mensagem']
    readonly_fields = ['data_envio']
    list_editable = ['lido']
```

### Personalizações Disponíveis

#### list_display
Define quais campos aparecem na listagem:

```python
list_display = ['titulo', 'data_criacao', 'status']
```

#### list_filter
Adiciona filtros laterais:

```python
list_filter = ['status', 'categoria', 'data_criacao']
```

#### search_fields
Define campos para busca:

```python
search_fields = ['titulo', 'descricao', 'conteudo']
```

#### readonly_fields
Campos que não podem ser editados:

```python
readonly_fields = ['data_criacao', 'data_atualizacao']
```

#### list_editable
Campos editáveis diretamente na listagem:

```python
list_editable = ['status', 'destaque']
```

## Segurança

### Controle de Acesso
- Apenas superusuários têm acesso total
- Permissões granulares por modelo
- Log de atividades
- Sessões seguras

### Validação
- Validação automática de formulários
- Proteção contra XSS
- Sanitização de dados
- Validação de uploads

## Dicas de Uso

### Navegação
- Use o menu lateral para navegar entre módulos
- Utilize os filtros para encontrar registros específicos
- Use a busca para localizar conteúdo rapidamente

### Edição
- Salve frequentemente durante edições longas
- Use o preview para verificar mudanças
- Revise antes de publicar conteúdo

### Upload de Arquivos
- Formatos suportados: JPG, PNG, GIF, PDF
- Tamanho máximo: 5MB por arquivo
- Nomes de arquivo são sanitizados automaticamente

## Solução de Problemas

### Erro de Login
```bash
# Recriar superusuário
python manage.py createsuperuser
```

### Erro de Permissão
```bash
# Verificar permissões do usuário
python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(username='seu_usuario')
>>> user.is_staff = True
>>> user.is_superuser = True
>>> user.save()
```

### Problemas de Upload
- Verifique se a pasta `media/` existe
- Confirme permissões de escrita
- Verifique tamanho do arquivo

## Próximos Passos

- **[Gerenciamento de Conteúdo](content-management.md)**: Guia detalhado para gerenciar conteúdo
- **[Configurações](development/settings.md)**: Configurações avançadas do admin
- **[Modelos](development/models.md)**: Entenda os modelos de dados 