
# Gestão de Pacientes

Este é um projeto Django para gerenciar pacientes, consultas e tarefas. O projeto inclui funcionalidades para cadastrar pacientes, registrar consultas, visualizar consultas públicas e muito mais.

## Estrutura do Projeto

```
core/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
db.sqlite3
manage.py
media/
    fotos/
    video/
pacientes/
    __init__.py
    admin.py
    apps.py
    migrations/
    models.py
    templates/
        consulta_publica.html
        paciente.html
        pacientes.html
    tests.py
    urls.py
    views.py
requirements.txt
templates/
    base.html
```

## Funcionalidades

- **Cadastro de Pacientes**: Formulário para cadastrar novos pacientes com campos como nome, email, telefone, queixa e foto.
- **Visualização de Pacientes**: Página detalhada para cada paciente, mostrando suas informações e consultas registradas.
- **Consultas**: Registro de consultas para pacientes, incluindo humor, registro geral, vídeo e tarefas associadas.
- **Administração**: Registro dos modelos Pacientes e Tarefas no admin do Django para gerenciamento.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/lelecodog/gestao-de-pacientes
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```sh
   python manage.py runserver
   ```

## Uso

- Acesse `http://127.0.0.1:8000/pacientes/` para visualizar e cadastrar pacientes.
- Acesse `http://127.0.0.1:8000/admin/` para acessar a interface de administração do Django.

## Estrutura dos Modelos

- **Pacientes**: Armazena informações sobre os pacientes.
- **Tarefas**: Armazena informações sobre as tarefas atribuídas aos pacientes.
- **Consultas**: Armazena informações sobre as consultas realizadas com os pacientes.
- **Visualizacoes**: Armazena informações sobre as visualizações das consultas públicas.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
