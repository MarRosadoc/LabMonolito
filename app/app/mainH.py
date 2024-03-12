from flask import Flask
from modules import module1
from modules import module2

app = Flask(__name__)

@app.route('/')
def index():
    # Llamamos a una función del módulo 1
    module1.funcion1()

    # Llamamos a una función del módulo 2
    module2.funcion2()

    return "Laboratorio Monolito <br> <br> Paola Mérida - 1084120 <br> María del Mar Rosado - 1070720"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)