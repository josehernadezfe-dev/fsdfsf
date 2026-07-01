const formulario = document.getElementById("formulario");

const preview = document.getElementById("preview");

const imagen = document.getElementById("imagen");

imagen.addEventListener("change", () => {

    const archivo = imagen.files[0];

    if (!archivo) return;

    preview.src = URL.createObjectURL(archivo);

    preview.style.display = "block";

});

formulario.addEventListener("submit", async (e)=>{

    e.preventDefault();

    const datos = new FormData();

    datos.append(
        "nombre",
        document.getElementById("nombre").value
    );

    datos.append(
        "marca",
        document.getElementById("marca").value
    );

    datos.append(
        "precio",
        document.getElementById("precio").value
    );

    datos.append(
        "stock",
        document.getElementById("stock").value
    );

    datos.append(
        "descripcion",
        document.getElementById("descripcion").value
    );

    if(imagen.files.length>0){

        datos.append(
            "imagen",
            imagen.files[0]
        );

    }

    const respuesta = await fetch("/api/productos",{

        method:"POST",

        body:datos

    });

    const json = await respuesta.json();

    document.getElementById("mensaje").innerHTML = json.mensaje;

    formulario.reset();

    preview.style.display="none";

});