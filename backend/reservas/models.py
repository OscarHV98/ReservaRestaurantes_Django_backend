from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .validators import validar_telefono, validar_capacidad_mesa, validar_username, validar_precio_plato

# Gestor de clientes
class ClienteManager(BaseUserManager):
    def create_user(self, username, nombre, correo, password=None, **extra_fields):
        if not username:
            raise ValueError('El username es obligatorio.')
        if not correo:
            raise ValueError('El correo es obligatorio.')
        
        correo = self.normalize_email(correo)
        user = self.model(username=username, nombre=nombre, correo=correo, **extra_fields)
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, nombre, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, nombre, correo, password, **extra_fields)

# Modelo Cliente
class Cliente(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, validators=[validar_username] # Validación personalizada
        )  # Este es el campo que se utilizará para autenticación
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)  # El correo es único
    telefono = models.CharField(max_length=15, blank=True, null=True, unique=True, validators=[validar_telefono]) # Validación personalizada
    preferencias = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Relaciones con grupos y permisos
    groups = models.ManyToManyField('auth.Group', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', blank=True)

    objects = ClienteManager()

    USERNAME_FIELD = 'username'  # El campo usado para autenticar al usuario es 'username'
    REQUIRED_FIELDS = ['nombre', 'correo']  # Campos obligatorios para crear un usuario (aparte del 'username' y 'password')

    def __str__(self):
        return self.username
    
# Modelo Restaurante
class Restaurante(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    
# Modelo Mesa
class Mesa(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField(validators=[validar_capacidad_mesa]) # Validación personalizada
    ubicacion = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    restaurante = models.ForeignKey('Restaurante', on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        unique_together = ('restaurante', 'numero')  # Evitar duplicación de números de mesa en un restaurante

    def __str__(self):
        return f"Mesa {self.numero} - {self.capacidad} personas ({self.restaurante.nombre})"


# Modelo Reservación
class Reservacion(models.Model):
    ESTADO_CHOICES = [
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    numero_de_personas = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='confirmada')
    notas = models.TextField(blank=True, null=True)

    def clean(self):
        if self.numero_de_personas > self.mesa.capacidad:
            raise ValueError("El número de personas excede la capacidad de la mesa.")
        super().clean()

    def __str__(self):
        return f"Reservación de {self.cliente} en {self.mesa} el {self.fecha_hora}"

# Modelo Menú y Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='platos')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_precio_plato]) # Validación personalizada
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='platos')

    def __str__(self):
        return f"{self.nombre} ({self.restaurante.nombre})"