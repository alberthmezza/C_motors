
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from app import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    #Gestion de Login 
    path('', views.loginUsers,name="login"),
    path('index', login_required(views.index), name='index'),
    path('validar/', views.validar,name="validar"),
    path('logout/',login_required(views.salir),name="logout"),
    path('accounts/login/',LoginView.as_view(template_name ='app/login.html'), name = 'Login2'),
    #Gestion de producto
    path('registrarProducto', login_required(views.registrarProducto), name='registrarProducto'),
    path('listarProductos', login_required(views.listarProductos), name='listarProductos'),
    path('Producto_registrar', login_required(views.Producto_registrar), name='Producto_registrar'),

    #Prueba de registro contacto 
    path('contacto', views.contacto, name='contacto'),
    path('Contacto_registar',views.Contacto_registrar, name="Contacto_registar"),
]

