document.addEventListener("DOMContentLoaded", function () {


    const contadorSolicitudes = document.getElementById("contador-solicitudes");
    const contadorConexiones = document.getElementById("contador-conexiones");

    const botonesAceptar = document.querySelectorAll(".aceptar");
    const botonesRechazar = document.querySelectorAll(".rechazar");

    function disminuirSolicitudes() {

        let actual = parseInt(contadorSolicitudes.textContent);
        contadorSolicitudes.textContent = actual - 1;
    }

    function aumentarConexiones() {

        let actual = parseInt(contadorConexiones.textContent);
        contadorConexiones.textContent = actual + 1;
    }

    botonesAceptar.forEach(function (boton) {
        boton.addEventListener("click", function () {

            const solicitud = this.parentElement;

            solicitud.remove();

            disminuirSolicitudes();   
            aumentarConexiones();     

            alert("¡Solicitud aceptada!");

        });
    });

    botonesRechazar.forEach(function (boton) {
        boton.addEventListener("click", function () {

            const solicitud = this.parentElement;

            solicitud.remove();

            disminuirSolicitudes();

            console.log("Solicitud rechazada");
        });
    });

});

