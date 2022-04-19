## API Catalog

API rest Product Catalog

### Requerimientos
* Python 3.6+
* Django <4
* Pipenv

#### Instalar requerimientos
```
pipenv install
pipenv install --dev
```

#### Configuracion
```
Nota: Cambiar <django_project> por `catalog` en cada paso de este documento
```

* Crear el archivo .env y configurarlo de acuerdo al ambiente
```
cd <django_project>/
cp -a .env.example .env
```

* Crear el archivo de configuracion de django segun ambiente de despliegue
```
cd <django_project>/settings/
cp -a local_settings.py.example local.py
```

* Generar **_SECRET_KEY_** desde la consola de django y remplazar en .env
```
python manage.py shell --settings=<django_project>.settings.local
```

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

#### Cargar fixture
```
python manage.py loaddata ../fixtures/initial.json --settings=<django_project>.settings.local
```
#### Crear las tablas en nuestra BD de nuestras apps
```
python manage.py makemigrations --settings=<django_project>.settings.local
python manage.py migrate --settings=<django_project>.settings.local
```

#### Iniciar proyecto

* Ejecutar servidor de prueba
```
python manage.py runserver --settings=<django_project>.settings.local
```

### Test
* Cumplimiento de la guía de estilo de python
```
flake8 .
```