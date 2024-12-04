from django.urls import path, include
from . import views

urlpatterns = [
    #register y login
    path('register/', views.RegistroClienteView.as_view(), name='register'),
    path('login/', views.LoginClienteView.as_view(), name='login'),
    
    # path('registro/', views.registro_cliente, name='register'),
    # path('login/', views.login_cliente, name='login'),
    
    # Rutas para Cliente
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente-detail'),

    # Rutas para Restaurante
    path('restaurantes/', views.RestauranteListView.as_view(), name='restaurante-list'),
    path('restaurantes/<int:pk>/', views.RestauranteDetailView.as_view(), name='restaurante-detail'),

    # Rutas para Mesa
    path('mesas/', views.MesaListView.as_view(), name='mesa-list'),
    path('mesas/<int:pk>/', views.MesaDetailView.as_view(), name='mesa-detail'),

    # Rutas para Reservación
    path('reservaciones/', views.ReservacionListView.as_view(), name='reservacion-list'),
    path('reservaciones/<int:pk>/', views.ReservacionDetailView.as_view(), name='reservacion-detail'),

    # Rutas para Categoría
    path('categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),

    # Rutas para Plato
    path('platos/', views.PlatoListView.as_view(), name='plato-list'),
    path('platos/<int:pk>/', views.PlatoDetailView.as_view(), name='plato-detail'),
]
