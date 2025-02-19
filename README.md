# Gestão de Pacientes

Este é um projeto de gestão de pacientes, desenvolvido com Django. O sistema permite o cadastro de pacientes, registro de consultas, acompanhamento de faltas e visualização de gráficos de humor dos pacientes.

## Funcionalidades

- Cadastro de pacientes
- Registro de consultas
- Acompanhamento de faltas
- Visualização de gráficos de humor dos pacientes

## Tecnologias Utilizadas

- Python
- Django
- Tailwind CSS
- Chart.js

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/gestao-de-financas.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd gestao-de-financas
    ```

3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No Linux/Mac:
        ```bash
        source venv/bin/activate
        ```

5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

6. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

7. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

8. Acesse o sistema no navegador:
    ```
    http://127.0.0.1:8000
    ```

## Uso

1. Acesse a página de pacientes para cadastrar novos pacientes.
2. Registre consultas para os pacientes cadastrados.
3. Acompanhe as faltas dos pacientes.
4. Visualize os gráficos de humor dos pacientes.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.