from django.shortcuts import render

# Create your views here.
def home(request):# definimos una vista que se llama home con metodo de djago por medio de def. Esta debe recibir una peticion ( un reques). MODELO DE CLIENTE SERVIDOR, EN EL CUAL UN CLIENTE HACE PETICIONES A UN SERVIDOR,Y EL SERVIDOR SE ENCARGA DE PROCESAR ESAS PETICIONES Y DEVOLVER UNA RESPUESTA.
    return render(request, "gestionCursos.html") # RETORNA LA RESPUESTA MEDIANTE UN RENDE, DEL REQUEST, DE LA PETICION Y ACA LE PASO ENTRE "" EL NOMBRE DE LA PLANTILLA TEMPLATE HTML)