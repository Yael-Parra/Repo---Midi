from django.urls import path, include
from rest_framework import routers
from . import views

# Configuración de las rutas de la API RESTful
router = routers.DefaultRouter()
router.register(r'info_padres_tutores_legales', views.InfoPadresTutoresLegalesViewSet)  # Registra el ViewSet de la API

# Rutas para las vistas basadas en funciones (HTML)
urlpatterns = [
    # Rutas para la interfaz web (HTML)
    path('', views.lista_info, name='lista_info'),
    path('detalle/<int:id>/', views.detalle_info, name='detalle_info'),

    # Rutas para la API RESTful
    path('api/', include(router.urls)),  # Prefijo 'api/' para las rutas de la API
]



# # app/info_padres_tutores_legales/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.lista_info, name='lista_info'),  # Vista para listar información de padres/tutores
#     path('detalle/<int:id>/', views.detalle_info, name='detalle_info'),  # Vista de detalle de información
# ]