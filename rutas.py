#Rutas de acceso a cada recurso
from click import clear

from recursos import *
def crear_rutas(api):
    # Quiero que puedas acceder a este recurso por medio de tal ruta
    api.add_resource(HolaMundo, '/hola')
    api.add_resource(PantallaInicio, '/')
    api.add_resource(Despedida, '/adios')
