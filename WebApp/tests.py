from django.test import TestCase
from WebApp.models import Pedido

# Create your tests here.
class ProductoTestCase(TestCase):
    def setUp(self):
        Pedido.objects.create(id=1, rut="123123" , cert_ssl=1, dominio="www.ejemplo.com", email="ejemplo@host")

def test_pedidoingresadorut(self):
    producto1 = Pedido.objects.get(id=1)
    self.assertEqual(producto1.rut,"123123")

def test_pedidoingresadocert(self):
    producto1 = Pedido.objects.get(id=1)
    self.assertEqual(producto1.cert_ssl,1)

def test_pedidoingresadodominio(self):
    producto1 = Pedido.objects.get(id=1)
    self.assertEqual(producto1.dominio,"www.ejemplo.com") 

def test_pedidoingresamail(self):
    producto1 = Pedido.objects.get(id=1)
    self.assertEqual(producto1.email,"ejemplo@host.com")   