from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
from .models import Cliente, Mesa, Reservacion, Categoria, Plato, Restaurante
from .serializers import ClienteRegistroSerializer, ClienteLoginSerializer, ClienteSerializer, MesaSerializer, ReservacionSerializer, CategoriaSerializer, PlatoSerializer, RestauranteSerializer
from drf_yasg.utils import swagger_auto_schema

#Registro Cliente

class RegistroClienteView(APIView):
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación
    @swagger_auto_schema(request_body=ClienteRegistroSerializer)
    def post(self, request):
        serializer = ClienteRegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para login
class LoginClienteView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(request_body=ClienteLoginSerializer)
    def post(self, request):
        print(request.data)  # Verifica qué datos llegan en la solicitud

        # Usamos el serializador modificado
        serializer = ClienteLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            # Generar el token JWT
            refresh = RefreshToken.for_user(user)
            token_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            # Serializar los datos del usuario
            user_data = {
                'id': user.id,
                'username': user.username,
                'nombre': user.nombre,
                'correo': user.correo,
                'telefono': user.telefono, 
                'preferencias': user.preferencias,
            }

            return Response({'data': user_data, 'token': token_data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vistas para Restaurante
class RestauranteListView(generics.ListCreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class RestauranteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer   

     
# Vistas para Cliente
class ClienteListView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Vistas para Mesa
class MesaListView(generics.ListCreateAPIView):
    serializer_class = MesaSerializer

    def get_queryset(self):
        restaurante_id = self.request.query_params.get('restaurante')
        if restaurante_id:
            return Mesa.objects.filter(restaurante_id=restaurante_id)
        return Mesa.objects.all()

class MesaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

# Vistas para Reservación
class ReservacionListView(generics.ListCreateAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer

class ReservacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer

# Vistas para Categoría
class CategoriaListView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# Vistas para Plato
class PlatoListView(generics.ListCreateAPIView):
    serializer_class = PlatoSerializer

    def get_queryset(self):
        restaurante_id = self.request.query_params.get('restaurante')
        if restaurante_id:
            return Plato.objects.filter(restaurante_id=restaurante_id)
        return Plato.objects.all()
    
class PlatoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer