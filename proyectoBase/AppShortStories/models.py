from django.db import models
from django.contrib.auth.models import User

class Genero(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField(default = False)
    creador = models.ForeignKey(to=User,on_delete = models.CASCADE, related_name="creador")

    def __str__(self):
        return self.descripcion

class ShortStories(models.Model):
    titulo = models.CharField(max_length=50)
    genero = models.ForeignKey(to=Genero, on_delete=models.CASCADE)
    estado = models.BooleanField()
    texto = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="cuentos", null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add= True)
    publisher = models.ForeignKey(to=User,on_delete = models.CASCADE, related_name="publisher")

class Profile(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    user = models.OneToOneField(to = User,on_delete = models.CASCADE,related_name='profile')
    imagen = models.ImageField(upload_to="profiles", null=True, blank=True)

class Mensaje(models.Model):
    motivos_combo =[(1,'Consulta sobre la App'),(2,'Problemas en la Registracion'),
                    (3,'Problemas al Loguearse'), (4,'Problemas en la App'), (5,'Publicacion Ofensiva'),
                    (6,'Otros') ]
    estado_combo =[(1,'Pendiente'), (2,'En proceso'), (3,'Cerrado'),(4,'Derivado')]

    email = models.EmailField()
    motivo = models.IntegerField(null=True, blank=True, choices = motivos_combo,default = 1)
    estado = models.IntegerField(null=False, blank=False, choices = estado_combo,default = 1)
    mensaje = models.TextField(max_length=500)
    enviado_el = models.DateTimeField(auto_now_add= True)
    destinatario = models.ForeignKey(to=User, on_delete = models.CASCADE, related_name ="destinatario")

    
