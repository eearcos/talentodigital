$(document).ready(function() {
    
    // 1. Simulación Login (Evento Submit)
    $('#loginForm').on('submit', function(e) {
        e.preventDefault(); // Evita recarga
        
        var email = $('#emailInput').val();
        var pass = $('#passInput').val();

        if (email && pass) {
            // Simulamos redirección
            alert("¡Bienvenido/a a Growth Academy! Redirigiendo al aula...");
            window.location.href = "plataforma.html";
        } else {
            alert("Por favor completa los campos.");
        }
    });

    // 2. Simulación Pago (Evento Click)
    $('.btn-pagar').click(function() {
        var metodo = $(this).text();
        // Confirmación nativa JS
        var confirmar = confirm("¿Estás seguro que deseas ir a pagar con " + metodo + "?");
        if (confirmar) {
            alert("Redirigiendo a pasarela segura... (Simulación)");
        }
    });

    // 3. Simulación Subida Tarea (Manipulación DOM + jQuery)
    $('#btnSubir').click(function() {
        var archivo = $('#fileInput').val();
        var btn = $(this);

        if (archivo) {
            btn.prop('disabled', true).text('Subiendo...');
            
            // Simulamos delay de red
            setTimeout(function() {
                $('#uploadMsg').removeClass('d-none').hide().fadeIn();
                btn.prop('disabled', false).text('Enviar Tarea');
                $('#fileInput').val(''); // Limpiar input
            }, 1500);
        } else {
            alert("Debes seleccionar un archivo primero.");
        }
    });

});