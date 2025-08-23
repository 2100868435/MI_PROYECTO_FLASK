from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/usuarios/<nombre>')
def usuarios(nombre):
    return f"Hola, {nombre}!"

# ruta de servicios
@app.route('/servicios')
def servicios():
    return "servicios disponibles:"

if __name__ == "__main__":
    app.run(debug=True)
