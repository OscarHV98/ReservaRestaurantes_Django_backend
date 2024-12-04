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

1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd backend
