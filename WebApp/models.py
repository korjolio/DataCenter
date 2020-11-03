from django.db import models
# Create your models here.

class Pedido(models.Model):
    alt_tipo_plan = (
        (24990, 'Wordpress SSD'),
        (34990, 'Basico SSD'),
        (44990, 'Emprendedor SSD'),
        (54990, 'Corporativo SSD'),
    )
    tipo_plan = models.IntegerField(choices=alt_tipo_plan)
    alt_vig = (
        (1, '1 año'),
        (2, '2 años'),
        (3, '3 años'),
        (4, '4 años'),
    )
    vigencia = models.IntegerField(choices=alt_vig)
    dominio = models.URLField(max_length=100)
    cert_ssl = models.BooleanField(blank=True, verbose_name='¿Requiere Certificado SSL?')
    nombre = models.CharField(max_length=100)
    a_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    a_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    rut = models.CharField(max_length=10)
    email = models.EmailField(blank=False)

    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'

    def __str__(self):
        return str(self.tipo_plan)

    def calculo(self):
        if self.cert_ssl == False:
            return self.tipo_plan * self.vigencia
        else:
            return self.tipo_plan * self.vigencia + 10000


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    telefono = models.CharField(max_length=9, null=True)
    alt_tipo_consulta = (
        (0, 'Consulta'),
        (1, 'Reclamo'),
        (2, 'Sugerencia'),
        (3, 'Felicitaciones'),
    )
    tipo_consulta = models.IntegerField(choices=alt_tipo_consulta, verbose_name='Tipo de consulta')
    mensaje = models.TextField(max_length=200)
    avisos = models.BooleanField(blank=False, null=False, verbose_name='¿Desea recibir información adicional a su email?')

    class Meta:
        verbose_name='Contacto'
        verbose_name_plural='Contactos'

    def __str__(self):
        return self.nombre