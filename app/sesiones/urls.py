from django.urls import path, include
from rest_framework import routers
from . import views

# Configuración de las rutas de la API RESTful
router = routers.DefaultRouter()
router.register(r'sesiones', views.SesionViewSet)  # Registra el ViewSet de la API

# Rutas para las vistas basadas en clases (HTML)
urlpatterns = [
    # Rutas para la interfaz web (HTML)
    path('', views.SesionListView.as_view(), name='sesion_list'),
    path('nueva/', views.SesionCreateView.as_view(), name='sesion_create'),
    path('<int:pk>/', views.SesionDetailView.as_view(), name='sesion_detail'),
    path('<int:pk>/editar/', views.SesionUpdateView.as_view(), name='sesion_update'),
    path('<int:pk>/eliminar/', views.SesionDeleteView.as_view(), name='sesion_delete'),

    # Rutas para la API RESTful
    path('api/', include(router.urls)),  # Prefijo 'api/' para las rutas de la API
]