$(document).ready(function() {
    
    $('#contactForm').on('submit', function(e) {
        e.preventDefault();

        
        var nombre = $('#nombre').val().trim();
        var email = $('#email').val().trim();
        var mensaje = $('#mensaje').val().trim();

        if (nombre === "" || email === "" || mensaje === "") {
            $('#form-error').removeClass('d-none');
            $('#form-feedback').addClass('d-none');
        } else {
            // Éxito
            $('#form-error').addClass('d-none');
            $('#form-feedback').removeClass('d-none').text(`¡Gracias ${nombre}! Hemos recibido tu consulta.`);
            
            // Limpiar formulario
            $('#contactForm')[0].reset();
        }
    });

    $('.test-btn').on('click', function() {
        var respuesta = $(this).data('res');
        
        if (respuesta === 'correcto') {
            $('#test-result').text('¡Correcto! Nunca uses contraseñas simples.').addClass('text-success').removeClass('text-danger');
        } else {
            $('#test-result').text('Incorrecto. Esa es una de las peores contraseñas del mundo.').addClass('text-danger').removeClass('text-success');
        }
    });

    $('.alert').on('click', function() {
        $(this).addClass('d-none');
    });

});