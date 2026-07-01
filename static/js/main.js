
const contenedor = document.getElementById("contenedor-productos");

let productos = [];

let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

// =====================
// CARGAR
// =====================

async function cargar() {

    const res = await fetch("/api/productos");

    productos = await res.json();

    render(productos);
}

// =====================
// RENDER
// =====================

function render(lista) {

    contenedor.innerHTML = "";

    lista.forEach(p => {

        const div = document.createElement("div");

        div.className = "card";

        div.innerHTML = `

            <img src="/uploads/${p.imagen}">

            <h3>${p.nombre}</h3>

            <p>${p.marca}</p>

            <strong>$${p.precio}</strong>

            <button onclick="agregar(${p.id})">
                🛒 Agregar
            </button>

            <button onclick="fav('${p.nombre}')">
                ❤️
            </button>

        `;

        contenedor.appendChild(div);
    });
}

// =====================
// CARRITO
// =====================

function agregar(id) {

    const p = productos.find(x => x.id === id);

    carrito.push(p);

    localStorage.setItem("carrito", JSON.stringify(carrito));

    actualizar();
}

// =====================
// FAVORITOS
// =====================

function fav(nombre) {

    alert("❤️ Guardado en favoritos: " + nombre);

}

// =====================
// FILTROS
// =====================

document.getElementById("buscar").addEventListener("input", filtrar);

document.getElementById("filtroMarca").addEventListener("change", filtrar);

document.getElementById("precioMax").addEventListener("input", filtrar);

function filtrar() {

    let lista = [...productos];

    const texto = document.getElementById("buscar").value.toLowerCase();

    const marca = document.getElementById("filtroMarca").value;

    const precio = document.getElementById("precioMax").value;

    if (texto) {

        lista = lista.filter(p =>
            p.nombre.toLowerCase().includes(texto)
        );
    }

    if (marca !== "todas") {

        lista = lista.filter(p => p.marca === marca);
    }

    if (precio) {

        lista = lista.filter(p => p.precio <= precio);
    }

    render(lista);
}

// =====================
// CARRITO UI
// =====================

function actualizar() {

    const items = document.getElementById("items");

    const totalHTML = document.getElementById("total");

    const count = document.getElementById("count");

    items.innerHTML = "";

    let total = 0;

    carrito.forEach((p, i) => {

        total += p.precio;

        const div = document.createElement("div");

        div.innerHTML = `
            ${p.nombre} - $${p.precio}
            <button onclick="eliminar(${i})">❌</button>
        `;

        items.appendChild(div);
    });

    totalHTML.innerText = total;

    count.innerText = carrito.length;
}

function eliminar(i) {

    carrito.splice(i, 1);

    localStorage.setItem("carrito", JSON.stringify(carrito));

    actualizar();
}

// =====================

function abrirCarrito() {

    document.getElementById("carrito").style.right = "0";

}

function cerrarCarrito() {

    document.getElementById("carrito").style.right = "-400px";

}

// =====================

cargar();
actualizar();