# Gerador de GitIgnore

Aplicação de linha de comando desenvolvida em Python para facilitar a criação de arquivos `.gitignore`.

O projeto surgiu de uma necessidade pessoal de agilizar a configuração de repositórios Git, permitindo selecionar grupos de regras de exclusão por meio de um menu interativo no terminal.

Além de atender a essa necessidade, o desenvolvimento também foi utilizado para praticar a criação e a organização de aplicações em Python.

## Funcionalidades

- Exibe um menu interativo no terminal com os grupos de regras disponíveis.
- Permite selecionar os grupos que serão adicionados ao arquivo `.gitignore`.
- Remove do menu os grupos que já foram selecionados, evitando seleções duplicadas.
- Gera automaticamente o arquivo `.gitignore` com as regras dos grupos escolhidos.
- Impede a geração do arquivo quando nenhum grupo foi selecionado.

## Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento da aplicação, incluindo a lógica de seleção, validação de entradas e manipulação de arquivos.
- **Conda:** utilizado para criar e gerenciar o ambiente de desenvolvimento e suas dependências.

## Requisitos

- Python na versão definida no ambiente do projeto.
- Conda, caso seja utilizado o método de instalação com `environment.yml`.
- Terminal compatível com a execução de scripts Python.

## Instalação

Clone o repositório:

```bash
git https://github.com/CarlosAlexandreOM/Gerador_GitIgnore.git
```

Acesse a pasta do projeto:

```bash
cd Gerador_GitIgnore
```

### Configuração do ambiente

Crie o ambiente a partir do arquivo `environment.yml`:

```bash
conda env create -f environment.yml
```

Ative o ambiente:

```bash
conda activate gerador_gitignore
```

## Como executar

Com o ambiente ativado, execute o arquivo principal:

```bash
python main.py
```

Após a execução, será exibido um menu no terminal com os grupos disponíveis.

Selecione os grupos desejados e escolha a opção de criação do arquivo para gerar o `.gitignore` no diretório de execução do programa.

## Personalização

É possível adicionar novos grupos de regras ou modificar os existentes por meio do arquivo `group.py`.

Para adicionar um novo grupo, atualize:

- `GROUPS`: inclua o nome do grupo e sua respectiva lista de regras de exclusão.
- `DICT_NAMES`: adicione uma opção numérica associada ao nome do novo grupo.

O nome utilizado em ambos os dicionários deve corresponder para que as regras sejam identificadas corretamente.

## Limitações

- O projeto foi desenvolvido e testado inicialmente em ambiente Windows.
- O arquivo `.gitignore` é gerado no diretório de execução do programa, sem opção de escolher outro local.
- Caso já exista um arquivo `.gitignore` no diretório, seu conteúdo será substituído pelo novo arquivo gerado.
- O programa não possui funcionalidades para editar arquivos existentes ou preservar regras personalizadas durante a geração.

## Objetivo do projeto e aprendizados

O projeto teve como objetivo resolver uma necessidade pessoal e praticar o desenvolvimento de uma aplicação de linha de comando em Python.

Durante o desenvolvimento, foram trabalhados conceitos como organização de código em módulos, criação e utilização de funções, estruturas de dados, validação de entradas, manipulação de arquivos e gerenciamento de ambientes com Conda.

O projeto também serviu como oportunidade para praticar a estruturação de aplicações e compreender melhor a separação de responsabilidades no código.