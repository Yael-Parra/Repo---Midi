# app/cursos/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

# Configuración de las rutas de la API RESTful
router = routers.DefaultRouter()
router.register(r'cursos', views.CursoViewSet)  # Registra el ViewSet de la API

# Rutas para las vistas basadas en clases (HTML)
urlpatterns = [
    # Rutas para la interfaz web (HTML)
    path('', views.CursoListView.as_view(), name='curso_list'),
    path('crear/', views.CursoCreateView.as_view(), name='curso_create'),
    path('<int:pk>/editar/', views.CursoUpdateView.as_view(), name='curso_update'),
    path('<int:pk>/eliminar/', views.CursoDeleteView.as_view(), name='curso_delete'),

    # Rutas para la API RESTful
    path('api/', include(router.urls)),  # Prefijo 'api/' para las rutas de la API
]




# from django.urls import path, include
# from rest_framework import routers
# from . import views

# # Configuración de las rutas de la API RESTful
# router = routers.DefaultRouter()
# router.register(r'cursos', views.CursoViewSet)  # Registra el ViewSet de la API

# # Rutas para las vistas basadas en clases (HTML)
# urlpatterns = [
#     # Rutas para la interfaz web (HTML)
#     path('', views.CursoListView.as_view(), name='curso_list'),
#     path('crear/', views.CursoCreateView.as_view(), name='curso_create'),
#     path('<int:curso_id>/editar/', views.CursoUpdateView.as_view(), name='curso_update'),
#     path('<int:curso_id>/eliminar/', views.CursoDeleteView.as_view(), name='curso_delete'),

#     # Rutas para la API RESTful
#     path('api/', include(router.urls)),  # Prefijo 'api/' para las rutas de la API
# ]