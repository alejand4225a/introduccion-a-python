from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/contacto")
def contacto():
    return render_template("contactos/index.html")

@app.get("/contacto/<int:contactoId>/edit")
def editarContacto(contactoId):
    suma = 2+2
    return render_template('contactos/editar.html',contactoId = contactoId,
        suma= suma
    )

@app.get("/edad/<edadId>")
def edad(edadId):
    print("ingrese edad : ",edadId)

    return render_template('contactos/edad.html',edadId = edadId)


app.run(debug=True)

