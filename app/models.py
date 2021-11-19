from django.db import models
from django.db.models.base import Model

# Create your models here.
# DB C_motors

class Categoria(models.Model):
    nombre = models.CharField(max_length=50 )

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50 )
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=50 )

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField( max_length=50 )
    nombre = models.CharField( max_length=50 )
    descripcion = models.CharField( max_length=50)
    proveedor_idproveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    marca_idmarca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria_idcategoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen =models.ImageField(upload_to="productos", null=True)
    valor_ingreso = models.FloatField()
    valor_egreso = models.FloatField()
    valor_mayoreo = models.FloatField()
    stock = models.IntegerField()
    stockmin = models.IntegerField()
    stockmax = models.IntegerField()
    estado = models.BooleanField(null=True)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=50 )

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    documento = models.IntegerField()
    nombre = models.CharField(max_length=50 )
    apellido = models.CharField(max_length=50 )
    contrasena = models.CharField(max_length=50 )
    rol_idrol = models.ForeignKey(Rol, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    documento = models.IntegerField()
    nombre = models.CharField(max_length=50 )
    apellido = models.CharField(max_length=50 )
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50 )

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    usuario_idusuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    cliente_idcliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha = models.DateField()
    total = models.FloatField()

    def __str__(self):
        return self.cliente_idcliente

class producto_has_factura(models.Model):
    producto_idproducto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    factura_idfactura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    valor_unitario = models.FloatField()
    importe = models.FloatField()

    def __str__(self):
        return self.factura_idfactura

class Tipocontrol(models.Model):
    nombre = models.CharField(max_length=50 )

    def __str__(self):
        return self.nombre

class Control(models.Model):
    tipocontrol_idtipocontrol = models.ForeignKey(Tipocontrol, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50 )
    fecha = models.DateField()


    def __str__(self):
        return self.tipocontrol_idtipocontrol

class producto_has_control(models.Model):
    producto_idproducto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    control_idcontrol = models.ForeignKey(Control, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.producto_idproducto














# Estes es contacto solo por practica 

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField( max_length=50 )
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField(null=True)

    def __str__(self):
        return self.nombre