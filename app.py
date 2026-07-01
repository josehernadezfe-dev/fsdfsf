import os

from werkzeug.utils import secure_filename

from flask import (
    Flask,
    render_template,
    request,
    jsonify
)



from flask import Flask, render_template, request, jsonify

from database import crear_tablas

from models import (
    obtener_productos,
    agregar_producto,
    editar_producto,
    eliminar_producto
)

app = Flask(__name__)

crear_tablas()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/admin")
def admin():

    return render_template("admin.html")

# ======================
# OBTENER PRODUCTOS
# ======================

@app.route("/api/productos")
def api_productos():

    productos = []

    for p in obtener_productos():

        productos.append({

            "id": p["id"],
            "nombre": p["nombre"],
            "marca": p["marca"],
            "precio": p["precio"],
            "descripcion": p["descripcion"],
            "imagen": p["imagen"],
            "stock": p["stock"]

        })

    return jsonify(productos)




# ======================
# AGREGAR PRODUCTO
# ======================

@app.route("/api/productos", methods=["POST"])
def api_agregar():

    nombre = request.form["nombre"]

    marca = request.form["marca"]

    precio = float(request.form["precio"])

    descripcion = request.form["descripcion"]

    stock = int(request.form["stock"])

    archivo = request.files["imagen"]

    nombre_archivo = ""

    if archivo.filename != "":

        nombre_archivo = secure_filename(archivo.filename)

        archivo.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                nombre_archivo
            )
        )

    agregar_producto(

        nombre,

        marca,

        precio,

        descripcion,

        nombre_archivo,

        stock

    )

    return jsonify({

        "mensaje": "Producto agregado"

    })


# ======================
# ELIMINAR PRODUCTO
# ======================

@app.route("/api/productos/<int:id>", methods=["DELETE"])
def api_eliminar(id):

    eliminar_producto(id)

    return jsonify({
        "mensaje": "Producto eliminado"
    })


# ======================
# EDITAR PRODUCTO
# ======================

@app.route("/api/productos/<int:id>", methods=["PUT"])
def api_editar(id):

    datos = request.json

    editar_producto(

        id,

        datos["nombre"],
        datos["marca"],
        datos["precio"],
        datos["descripcion"],
        datos["imagen"],
        datos["stock"]

    )

    return jsonify({
        "mensaje": "Producto actualizado"
    })


if __name__ == "__main__":
    app.run(debug=True)