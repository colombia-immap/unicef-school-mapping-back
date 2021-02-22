## Analítica de datos e innovación para el análisis de trayectorias educativas y evaluación de las condiciones de WASH en escuelas

Herramienta de visualización de la localización de los colegios en Colombia <br />
y otras de sus características priorizadas por las entidades de Gobierno y UNICEF.

## Funcionamiento

### Requerimientos

1. Base de datos Postgresql
2. Python - Django

### Al clonar el repositorio por primera vez:

1. Copia el archivo mapa/settings.py.example a mapa/settings.py y configura la base de datos DATABASES['default'] y los
   origenes de consulta permitidos en CORS_ALLOWED_ORIGINS
2. Importa el archivo de base de datos base
3. Instala la dependencia de CORS `python -m pip install django-cors-headers`

### Correr la aplicación:

`python3 manage.py runserver`
Abrir [http://127.0.0.1:8000](http://127.0.0.1:8000) para verlo en el navegador.
