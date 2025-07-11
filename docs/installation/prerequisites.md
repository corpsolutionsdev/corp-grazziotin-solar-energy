# Pré-requisitos

Antes de começar a instalar o sistema Grazziotin Energia Solar, certifique-se de ter os seguintes requisitos instalados em seu sistema.

## Requisitos do Sistema

### Python

- **Versão**: Python 3.8 ou superior
- **Download**: [python.org](https://www.python.org/downloads/)
- **Verificação**: `python --version`

### Git

- **Versão**: Git 2.0 ou superior
- **Download**: [git-scm.com](https://git-scm.com/downloads)
- **Verificação**: `git --version`

### pip

- **Descrição**: Gerenciador de pacotes Python
- **Incluso**: Vem com Python 3.4+
- **Verificação**: `pip --version`

## Requisitos Opcionais

### Editor de Código

Recomendamos um dos seguintes editores:

- **VS Code**: [code.visualstudio.com](https://code.visualstudio.com/)
- **PyCharm**: [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
- **Sublime Text**: [sublimetext.com](https://www.sublimetext.com/)

### Terminal/CLI

- **Windows**: PowerShell ou Git Bash
- **macOS**: Terminal padrão
- **Linux**: Terminal padrão

## Verificação de Instalação

Execute os seguintes comandos para verificar se tudo está instalado:

```bash
# Verificar Python
python --version
# Deve mostrar: Python 3.8.x ou superior

# Verificar pip
pip --version
# Deve mostrar a versão do pip

# Verificar Git
git --version
# Deve mostrar a versão do Git
```

## Configuração Inicial

### 1. Configurar Git (Primeira vez)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

### 2. Criar Diretório de Trabalho

```bash
# Criar pasta para projetos
mkdir ~/projetos
cd ~/projetos
```

## Próximos Passos

Após verificar que todos os pré-requisitos estão instalados:

1. **[Instalação](installation.md)**: Siga o guia de instalação
2. **[Configuração](configuration.md)**: Configure o ambiente
3. **[Desenvolvimento](development/project-structure.md)**: Entenda a estrutura

## Solução de Problemas

### Python não encontrado

**Windows:**
- Adicione Python ao PATH durante a instalação
- Ou reinstale Python marcando "Add to PATH"

**macOS/Linux:**
```bash
# Usar pyenv para gerenciar versões
curl https://pyenv.run | bash
pyenv install 3.11.0
pyenv global 3.11.0
```

### pip não encontrado

```bash
# Instalar pip manualmente
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Git não encontrado

**Windows:**
- Baixe e instale do [git-scm.com](https://git-scm.com/downloads)

**macOS:**
```bash
# Instalar via Homebrew
brew install git
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install git
```

## Suporte

Se encontrar problemas com os pré-requisitos:

- Verifique a documentação oficial de cada ferramenta
- Consulte fóruns da comunidade
- Abra uma issue no GitHub do projeto 