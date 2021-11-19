from django import forms
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):

    class meta:
        model = Contacto 
        #fields = ["nombre", "correo", "tipo_comsulta", "mensaje", "avisos"]
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    class meta:
        model = Producto
        fields = '__all__'

#class Contacto_Insertar(models.Model):
#   nombre = models.CharField('nombre', max_length=50 )
#   correo = models.EmailField('correo' )
#   tipo_consulta = models.IntegerField('tipo_consulta')
#   mensaje = models.TextField('mensaje')

#   class Meta:
#       db_table = 'app_contacto'



