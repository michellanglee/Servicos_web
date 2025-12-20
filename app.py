#desde la libreria flask importa la clase flask
from flask import Flask

from flask_restful import Api,Resource
#vamos a crear un objeto llamado app
app = Flask(__name__)
#del objeto app ejecutamos el metodo run

#creamos un objeto que ser llame api y de argumento le pasamos el objeto app
#El parametro/agrumento que espera recibir es el objeto de Flask

api=Api(app)
from rutas import crear_rutas
crear_rutas(api)

app.run(port=8080, debug=True)