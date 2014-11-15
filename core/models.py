from django.db import models
from django.contrib.auth.models import User
from django_hstore import hstore


class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    rate = models.FloatField()

    def __unicode__(self):
        return u'{0}'.format(self.nombre)

class Usuario_empresa(models.Model):
    user = models.ForeignKey(User,related_name='perfil_empresa')
    empresa = models.ForeignKey(Empresa,related_name='empresa')
    is_admin = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{0}'.format(self.user.username)

class Servicio(models.Model):
    tipo = models.CharField(max_length=100)
    def __unicode__(self):
        return u'{0}'.format(self.tipo)

class Services_tag(models.Model):
    tag = models.CharField(max_length=100)
    servicio = models.ForeignKey(Servicio,related_name='servicio')
    def __unicode__(self):
        return u'{0}'.format(self.tag)

class Usuario(models.Model):
    user = models.ForeignKey(User,related_name='perfil_cliente')
    biografia = models.CharField(max_length='200')
    rating = models.FloatField()
    foto_perfil = models.ImageField(upload_to='perfil/cliente', default='perfil/cliente/avatar.jpg')
    def __unicode__(self):
        return u'{0}'.format(self.user.username)

class Service_req(models.Model):
    descripcion = models.CharField(max_length=200)
    servicio = models.ForeignKey(Servicio,related_name='servicio_pedido')
    tags = models.ForeignKey(Services_tag,related_name='etiquetas')
    usuario = models.ForeignKey(Usuario,related_name='cliente')
    fecha = models.DateTimeField()


class Service_prop(models.Model):
    service_req = models.ForeignKey(Service_req,related_name='service_req')
    empresa = models.ForeignKey(Empresa,related_name='propuesta_empresa')
    precio = models.FloatField()
    fecha = models.DateTimeField()
    rango = hstore.DictionaryField()

class Service_order(models.Model):
    service_prop = models.ForeignKey(Service_prop, related_name='propuesta')
    service_req = models.ForeignKey(Service_req,related_name= 'pedido')
    valor_aceptado = models.FloatField()
    usuario_empresa = models.ForeignKey(Usuario_empresa,related_name='usuario_empresa')
    terminado = models.BooleanField(default=False)
