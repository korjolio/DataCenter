from django.contrib import admin
from django.urls import path, include
from WebApp import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import PedidoViewset

router = routers.DefaultRouter()
router.register('pedido', PedidoViewset)

urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),
    path('contacto', views.contacto, name="Contacto"),
    path('registro/', views.registro_usuario, name="Registro"),
    path('listar-pedidos/', views.listar_pedidos, name="ListarPedidos"),
    path('eliminar-pedido/<id>/', views.eliminar_pedido, name="EliminarPedido"),
    path('modificar-pedidos/<id>/', views.modificar_pedidos, name="ModificarPedidos"),
    path('api/', include(router.urls)),
    path('login-facebook-error/', views.login_facebook_error, name="LoginFacebookError"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Administración de Web Datacenter"
admin.site.index_tittle = "Módulos de Administración"
admin.site.site_tittle = "Web Datacenter"