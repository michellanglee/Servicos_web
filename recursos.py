#Los recursos (informacion) que mi servidor tendra disponible

from flask_restful import Resource
from flask import make_response,render_template

#Vamos a crear recursos, lo haremos a través de clases y objetos
class HolaMundo(Resource):
    def get(self):
        return{'hola':'mundo' }

class PantallaInicio(Resource):
    def get (self):
        contenido = render_template('index.html')
        return make_reponse (contenido)

class Despedida(Resource):
    def get(self):
        print('Este es un texto de prueba')
        return 'adios'
