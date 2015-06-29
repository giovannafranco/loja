### Instalar pacotes de desenvolvedor Python
```sh
sudo apt-get install python-dev
```

### Criar ambiente virtual
```sh
mkvirtualenv loja-dw
```

### Ativar ambiente virtual
```sh
workon loja-dw
```

### Instalar dependências
```sh
pip install -r requirements.txt
```

### Rodar scripts de criação do banco de dados
```sh
python manage.py makemigrations
python manage.py migrate
```

### Rodar servidor de desenvolvimento
```sh
python manage.py runserver
```

### Url de acesso
http://localhost:8000
