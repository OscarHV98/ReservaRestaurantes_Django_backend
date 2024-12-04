# Backend de Reservas de Restaurante

Este proyecto es un backend para la gestión de reservas en un restaurante, desarrollado con **Django** y **Django REST Framework**. Utilizamos **autenticación JWT** para proteger las APIs, y **Swagger** para documentar y facilitar el uso de las APIs.

## Características principales

- **Gestión de reservas:** CRUD completo para reservas de restaurante.
- **Autenticación JWT:** Implementado con `djangorestframework-simplejwt`.
- **Base de datos PostgreSQL:** Configurada para almacenar y gestionar datos de manera eficiente.
- **Filtros avanzados:** Soportados por `django-filters` para mejorar la experiencia del usuario.
- **Swagger:** Documentación automática de la API usando `drf-yasg`.
- **Gestión de clientes y autenticación:** Creación de usuarios con registro y login utilizando JWT.
- **Gestión de restaurantes y mesas:** CRUD de restaurantes y mesas con validación de capacidad.
- **Menú y platos:** Gestión de menús, categorías y platos disponibles.
- **Validación personalizada:** Validaciones personalizadas para campos como número de teléfono, capacidad de mesa y precio de los platos.

## Requisitos previos

Asegúrate de tener instalado:

- **Python 3.9 o superior**
- **PostgreSQL** (si usas PostgreSQL como base de datos)
- **Virtualenv** (opcional, pero recomendado para crear un entorno virtual)

## Instalación

1. **Clona este repositorio**:
   
   Abre una terminal y clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/OscarHV98/ReservaRestaurantes_Django_backend.git
   cd ReservaRestaurantes_Django_backend

### Detalles:
- En el paso 2 se especifica cómo crear y activar un entorno virtual, lo cual es una práctica recomendada.
- Se indica cómo instalar las dependencias con `pip install -r requirements.txt`.
- Se detalla el comando `makemigrations` para asegurar que las migraciones se generen correctamente antes de aplicarlas.
- También se añade la creación del superusuario con el comando `createsuperuser` para poder acceder al panel de administración de Django.
- Se explica cómo iniciar el servidor de desarrollo con `python manage.py runserver`.
  
Con estos pasos, los usuarios podrán configurar el entorno y ejecutar el proyecto de manera correcta.