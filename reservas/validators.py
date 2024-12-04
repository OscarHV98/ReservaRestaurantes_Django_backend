# validators.py
from django.core.exceptions import ValidationError
import re

# Validación para el número de teléfono
def validar_telefono(valor):
    if not re.match(r'^\+?\d{7,15}$', valor):
        raise ValidationError(f'El número de teléfono "{valor}" no es válido. Debe tener entre 10 y 15 dígitos.')

# Validación para capacidad de mesa
def validar_capacidad_mesa(valor):
    if valor <= 0:
        raise ValidationError('La capacidad de la mesa debe ser un número positivo.')

# Validación para el nombre de usuario (sin espacios ni caracteres especiales)
def validar_username(valor):
    if not re.match(r'^\w+$', valor):
        raise ValidationError('El nombre de usuario solo puede contener letras, números y guiones bajos.')

# Validación para precio de plato
def validar_precio_plato(valor):
    if valor <= 0:
        raise ValidationError('El precio del plato debe ser mayor a cero.')
