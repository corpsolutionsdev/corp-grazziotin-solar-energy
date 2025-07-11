# Como Contribuir

Obrigado por seu interesse em contribuir com o projeto Grazziotin Energia Solar! 🚀

## Como Contribuir

### 1. Fork do Projeto

1. Acesse o repositório no GitHub
2. Clique no botão "Fork" no canto superior direito
3. Clone seu fork localmente:

```bash
git clone https://github.com/corpsolutionsdev/corp-grazziotin-solar-energy.git
cd corp-grazziotin-solar-energy
```

### 2. Configure o Ambiente

```bash
# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate
```

### 3. Crie uma Branch

```bash
# Crie uma branch para sua feature
git checkout -b feature/nova-funcionalidade

# Ou para correção de bug
git checkout -b fix/correcao-bug
```

### 4. Faça suas Alterações

- Escreva código limpo e bem documentado
- Siga os padrões de código do projeto
- Adicione testes para novas funcionalidades
- Atualize a documentação quando necessário

### 5. Commit e Push

```bash
# Adicione suas alterações
git add .

# Faça o commit com mensagem descritiva
git commit -m "feat: adiciona nova funcionalidade X"

# Envie para seu fork
git push origin feature/nova-funcionalidade
```

### 6. Abra um Pull Request

1. Vá para seu fork no GitHub
2. Clique em "New Pull Request"
3. Selecione sua branch
4. Preencha o template do PR
5. Aguarde a revisão

## Padrões de Código

### Python

- Use **PEP 8** como guia de estilo
- Máximo 79 caracteres por linha
- Use 4 espaços para indentação
- Nomes de variáveis e funções em snake_case
- Nomes de classes em PascalCase

### Django

- Siga as convenções do Django
- Use nomes descritivos para modelos e campos
- Documente views complexas
- Use migrations para mudanças no banco

### Templates

- Use indentação consistente
- Separe lógica de apresentação
- Use includes para reutilização
- Mantenha templates responsivos

## Estrutura de Commits

Use o padrão **Conventional Commits**:

```
tipo(escopo): descrição

feat: nova funcionalidade
fix: correção de bug
docs: documentação
style: formatação
refactor: refatoração
test: testes
chore: tarefas de manutenção
```

### Exemplos

```bash
feat(auth): adiciona autenticação OAuth
fix(admin): corrige erro no painel administrativo
docs(readme): atualiza instruções de instalação
style(css): formata código CSS
refactor(models): simplifica modelo de usuário
test(views): adiciona testes para views
chore(deps): atualiza dependências
```

## Testes

### Executar Testes

```bash
# Todos os testes
python manage.py test

# Testes específicos
python manage.py test app.tests
python manage.py test blog.tests.TestArtigoModel
```

### Escrever Testes

```python
from django.test import TestCase
from django.urls import reverse
from app.models import QuemSomos

class QuemSomosModelTest(TestCase):
    def setUp(self):
        self.quem_somos = QuemSomos.objects.create(
            titulo="Teste",
            descricao="Descrição de teste"
        )
    
    def test_titulo_max_length(self):
        self.assertEqual(self.quem_somos.titulo, "Teste")
    
    def test_str_representation(self):
        self.assertEqual(str(self.quem_somos), "Teste")
```

## Documentação

### Atualizar Documentação

- Mantenha a documentação atualizada
- Adicione exemplos de uso
- Documente APIs e interfaces
- Use linguagem clara e objetiva

### Estrutura de Documentação

```
docs/
├── index.md                    # Página inicial
├── installation/              # Guias de instalação
├── development/               # Desenvolvimento
├── modules/                   # Documentação dos módulos
├── admin/                     # Painel administrativo
├── deploy/                    # Deploy e produção
└── contributing/              # Guias de contribuição
```

## Processo de Revisão

### Checklist do PR

- [ ] Código segue os padrões do projeto
- [ ] Testes foram adicionados/atualizados
- [ ] Documentação foi atualizada
- [ ] Não há conflitos de merge
- [ ] Build passa sem erros
- [ ] Funcionalidade foi testada localmente

### Feedback

- Seja construtivo e respeitoso
- Foque no código, não na pessoa
- Sugira melhorias específicas
- Aprenda com o feedback recebido

## Tipos de Contribuição

### 🐛 Reportar Bugs

1. Verifique se o bug já foi reportado
2. Use o template de issue
3. Inclua passos para reproduzir
4. Adicione logs e screenshots se relevante

### 💡 Sugerir Melhorias

1. Descreva a funcionalidade desejada
2. Explique o benefício
3. Sugira uma implementação se possível
4. Considere o impacto na performance

### 📝 Melhorar Documentação

1. Identifique áreas confusas
2. Adicione exemplos práticos
3. Corrija erros gramaticais
4. Traduza para outros idiomas

### 🔧 Corrigir Bugs

1. Reproduza o bug localmente
2. Identifique a causa raiz
3. Escreva um teste que falha
4. Implemente a correção
5. Verifique se o teste passa

## Comunicação

### Canais

- **Issues**: Para bugs e sugestões
- **Discussions**: Para debates e ideias
- **Pull Requests**: Para código
- **Email**: Para assuntos privados

### Código de Conduta

- Seja respeitoso e inclusivo
- Mantenha discussões construtivas
- Foque no bem do projeto
- Reporte comportamentos inadequados

## Reconhecimento

### Contribuidores

- Seu nome será adicionado ao README
- Contribuições significativas ganham destaque
- Badges para diferentes tipos de contribuição
- Menção em releases

### Como Ser Reconhecido

- Mantenha commits consistentes
- Participe de discussões
- Ajude outros contribuidores
- Mantenha-se ativo no projeto

## Próximos Passos

- **[Padrões de Código](coding-standards.md)**: Detalhes sobre padrões
- **[Desenvolvimento](development/project-structure.md)**: Estrutura do projeto
- **[Testes](development/testing.md)**: Guia de testes
- **[Deploy](deploy/production.md)**: Configuração de produção

---

**Obrigado por contribuir com o Grazziotin Energia Solar!** 🌟 