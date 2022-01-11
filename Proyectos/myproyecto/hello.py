from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    salida='<html><head></head><body><h1>Bienvenido al servidor de erick castro <br> con nodejs'
    salida+='</h1><img src="https://erickcastro.000webhostapp.com/Metodo.jpg"> <br> <a href="https://github.com/erickcasnav" target="_blank">Entra a mi github</a></body></html>';
    return salida