# instalação 
1. instalar o postgresql na máquina
2. criar banco pesado
3. criar usuário "postgres" e senha "postgres"
4. abrir terminal na raiz do projeto
5. rodar o comando: python3 -m venv venv
6. rodar o comando: source venv/bin/activate
7. rodar o comando: pip install -r requirements.txt
8. rodar o comando: python manage.py migrate


# Iniciar servidor
1. iniciar venv com o comando: source venv/bin/activate
2. rodar o comando: python manage.py runserver

> OBS: ele irá iniciar no localhost:8000

# Criação de usuário
1. iniciar venv com o comando: source venv/bin/activate
2. rodar o comando: python manage.py createsuperuser
3. abrir o navegador na página: localhost:8000/admin

