from models import agregar_producto, obtener_productos

agregar_producto(
    "Nike Air Max 90",
    "Nike",
    599900,
    "Zapatilla deportiva",
    "nike.jpg",
    12
)

for producto in obtener_productos():
    print(dict(producto))