# Gerenciador de Tarefas com Flask

Este é um projeto simples de gerenciamento de tarefas criado com Flask. Ele permite adicionar tarefas com título, descrição e prioridade, além de listar as tarefas existentes.

## Estrutura do Projeto

- app.py: Arquivo principal da aplicação Flask.
- models.py: Arquivo contendo a lógica de manipulação das tarefas.
- templates/: Diretório contendo os arquivos HTML para renderização das páginas.
  - index.html: Página principal que lista as tarefas e possui o formulário para adicionar novas tarefas.
- static/: Diretório para arquivos estáticos (CSS, JS, imagens, etc).
- venv/: Ambiente virtual Python para o projeto.

## Pré-requisitos

- Python 3.7 ou superior
- Pipenv (opcional, mas recomendado para gerenciar dependências)

## Instalação

1. Clone o repositório:

    sh
    git clone https://github.com/elliemendes/ProjetoGTI-Flask.git
    cd ProjetoGTI-Flask
    

2. Crie um ambiente virtual e ative-o:

    No Windows:
    sh
    python -m venv venv
    .\venv\Scripts\activate
    

    No MacOS/Linux:
    sh
    python3 -m venv venv
    source venv/bin/activate
    

3. Instale as dependências:

    sh
    pip install flask
    

## Executando o Projeto

1. Certifique-se de que o ambiente virtual está ativado.
2. Execute o aplicativo:

    sh
    python app.py
    

3. Acesse o aplicativo em seu navegador:

    
    http://127.0.0.1:5000/
    

## Estrutura do Código

- *app.py*: Contém as rotas e a lógica principal do Flask.
- *models.py*: Contém as funções add_task e get_tasks que manipulam as tarefas.
- *templates/index.html*: Contém o layout da página principal.

## Contribuição

Sinta-se à vontade para contribuir com este projeto através de pull requests. Para grandes mudanças, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Licença

[MIT](LICENSE)
