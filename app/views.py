from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import Producto, Contacto
from .forms import ContactoForm, ProductoForm

@csrf_protect

# Gestión de Login 

def index(request):
    return render(request, 'app/index.html')

def contacto(request):
	data = {
		'form': ContactoForm
	}
	return render(request, 'app/contacto.html', data)

def Contacto_registrar(request):
	
	if request.method == 'POST':
			nombre=request.POST['nombre']
			correo=request.POST['correo']
			tipo_consulta=request.POST['tipo_consulta']
			mensaje=request.POST['mensaje']
			avisos=request.POST['avisos']
			
			contacto = Contacto(nombre = nombre, correo=correo, tipo_consulta=tipo_consulta, mensaje=mensaje, avisos = avisos)
			
			if contacto is not None:
				contacto.save()
				messages.success(request,"Contacto guardado")
				return redirect(to='contacto')
			else:
				messages.success(request,"Contacto no pudo ser guardado")
				return HttpResponse("Error al guardar")

def validar(request):
	if request.method == 'POST':
		usuario=request.POST['username']
		clave=request.POST['password']
		#tablaUsuariosDB=LoginUsuarios.objects.get(email=usuario)
		#emailsDB=tablaUsuariosDB.email
		#claveDB=tablaUsuariosDB.clave
		#if emailsDB==usuario and claveDB==clave:
		#	return render(request,"principal.html")
		#else: return HttpResponse("Error, usuario o clave incorrectos")
		user = authenticate(username=usuario, password = clave)
		if user is not None:
			login(request,user)
			messages.success(request,"    Bienvenido: ")
			return redirect(to='index')
			#return render(request, 'principal.html')
		else:
			messages.success(request,"Usuario o contraseña incorrectos")
			return redirect(to='login')
	else: return HttpResponse("Error")

def loginUsers(request):
	return render(request,"app/login.html")

def salir(request):
	logout(request)
	return redirect(to='login')

# Gestionar productos 

def registrarProducto(request):
	return render(request, 'app/registrarProducto.html')

def Producto_registrar(request):
	
	if request.method == 'POST':
			codigo=request.POST['codigo']
			nombre=request.POST['nombre']
			descripcion=request.POST['descripcion']
			proveedor_idproveedor=request.POST['proveedor_idproveedor']
			marca_idmarca=request.POST['marca_idmarca']
			categoria_idcategoria=request.POST['categoria_idcategoria']
			imagen=request.POST['imagen']
			valor_ingreso=request.POST['valor_ingreso']
			valor_egreso=request.POST['valor_egreso']
			valor_mayoreo=request.POST['valor_mayoreo']
			stock=request.POST['stock']
			stockmin=request.POST['stockmin']
			stockmax=request.POST['stockmax']
			estado=request.POST['estado']
			
			producto = Producto(codigo=codigo, nombre=nombre, descripcion=descripcion, proveedor_idproveedor=proveedor_idproveedor, marca_idmarca=marca_idmarca, categoria_idcategoria=categoria_idcategoria, imagen=imagen, valor_ingreso=valor_ingreso, valor_egreso=valor_egreso, valor_mayoreo=valor_mayoreo, stock=stock, stockmin=stockmin, stockmax=stockmax, estado=estado)
			
			if producto is not None:
				producto.save()
				messages.success(request,"Producto guardado")
				return redirect(to='registrarProducto')
			else:
				messages.success(request,"Producto no pudo ser guardado")
				return redirect(to='registrarProducto')


def listarProductos(request):
	productos = Producto.objects.all()
	data = {
		'productos': productos
	}
	return render(request, 'app/listarProductos.html', data)

