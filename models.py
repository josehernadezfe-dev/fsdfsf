from database import conectar


# ==========================
# OBTENER TODOS LOS PRODUCTOS
# ==========================

def obtener_productos():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM productos
        ORDER BY id DESC
    """)

    productos = cursor.fetchall()

    conexion.close()

    return productos


# ==========================
# OBTENER UN PRODUCTO
# ==========================

def obtener_producto(id_producto):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM productos
        WHERE id = ?
    """, (id_producto,))

    producto = cursor.fetchone()

    conexion.close()

    return producto


# ==========================
# AGREGAR PRODUCTO
# ==========================

def agregar_producto(nombre,
                     marca,
                     precio,
                     descripcion,
                     imagen,
                     stock):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

        INSERT INTO productos(

            nombre,
            marca,
            precio,
            descripcion,
            imagen,
            stock

        )

        VALUES(?,?,?,?,?,?)

    """, (

        nombre,
        marca,
        precio,
        descripcion,
        imagen,
        stock

    ))

    conexion.commit()

    conexion.close()


# ==========================
# EDITAR PRODUCTO
# ==========================

def editar_producto(id_producto,
                     nombre,
                     marca,
                     precio,
                     descripcion,
                     imagen,
                     stock):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

        UPDATE productos

        SET

            nombre=?,
            marca=?,
            precio=?,
            descripcion=?,
            imagen=?,
            stock=?

        WHERE id=?

    """, (

        nombre,
        marca,
        precio,
        descripcion,
        imagen,
        stock,
        id_producto

    ))

    conexion.commit()

    conexion.close()


# ==========================
# ELIMINAR PRODUCTO
# ==========================

def eliminar_producto(id_producto):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

        DELETE FROM productos

        WHERE id=?

    """, (id_producto,))

    conexion.commit()

    conexion.close()