cd loja/

# Instalar pacotes de desenvolvedor Python
sudo apt-get install python-dev

# Criar ambiente virtual
mkvirtualenv loja-dw

# Ativar ambiente virtual
workon loja-dw

# Instalar dependências
pip install -r requirements.txt

# Rodar scripts de criação do banco de dados
python manage.py makemigrations
python manage.py migrate

# Rodar servidor de desenvolvimento
python manage.py runserver

# Url de acesso
http://localhost:8000
