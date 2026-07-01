import sqlite3

DATABASE = "tienda.db"


def conectar():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_tablas():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS productos(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nombre TEXT NOT NULL,

        marca TEXT NOT NULL,

        precio REAL NOT NULL,

        descripcion TEXT,

        imagen TEXT,

        stock INTEGER DEFAULT 0

    )

    """)

    conexion.commit()

    conexion.close()
