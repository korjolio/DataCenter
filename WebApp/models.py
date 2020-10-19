from django.db import models

# Create your models here.

class Pedido(models.Model):
    alt_tipo_plan = (
        ('Wordpress SSD', 'Wordpress SSD'),
        ('Basico SSD', 'Basico SSD'),
        ('Emprendedor SSD', 'Emprendedor SSD'),
        ('Corporativo SSD', 'Corporativo SSD'),
    )
    tipo_plan = models.CharField(max_length=50, choices=alt_tipo_plan)
    alt_vig = (
        ('1 año', '1 años'),
        ('2 años', '2 años'),
        ('3 años', '3 años'),
        ('4 años', '4 años'),
    )
    vigencia = models.CharField(max_length=50, choices=alt_vig)
    dominio = models.CharField(max_length=100)
    cert_ssl = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    a_paterno = models.CharField(max_length=100)
    a_materno = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    email = models.EmailField(blank=False)

    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'

    def __str__(self):
        return self.tipo_plan
