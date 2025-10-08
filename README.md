# Projeto de Receitas com Django

Este é um projeto de um site de receitas desenvolvido com o framework web Django. O objetivo é criar uma plataforma onde os usuários possam visualizar e buscar por diversas receitas culinárias.

## Tecnologias Utilizadas

*   Python
*   Django
*   HTML5
*   CSS3
*   SQLite3 (banco de dados padrão de desenvolvimento)

## Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

Certifique-se de ter o Python 3 e o pip instalados em sua máquina.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd projeto1_django
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Cria o ambiente virtual
    python -m venv venv

    # Ativa o ambiente no Windows
    .\venv\Scripts\activate

    # Ativa o ambiente no Linux ou macOS
    source venv/bin/activate
    ```

3.  **Instale as dependências do Django:**
    ```bash
    pip install Django
    ```

4.  **Execute as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

Após iniciar o servidor, você pode acessar o site em `http://127.0.0.1:8000/` no seu navegador.
