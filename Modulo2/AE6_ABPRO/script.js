    $(document).ready(function() {
      $('.reservar-btn').click(function() {
        const pelicula = $(this).data('pelicula');
        $('#pelicula').val(pelicula);
        $('#formModal').modal('show');
        $('#confirmacion').hide();
      });

      // Manejar el botón Reservar del modal
      $('#btnReservar').click(function() {
        const pelicula = $('#pelicula').val();
        const horario = $('#horario').val();
        const asiento = $('#asiento').val();
        const pago = $('#pago').val();

        if (!asiento) {
          alert('Por favor, ingresa un número de asiento');
          return;
        }

        const mensaje = `🎟️ Reserva Confirmada:<br>
        <strong>Película:</strong> ${pelicula}<br>
        <strong>Horario:</strong> ${horario}<br>
        <strong>Asiento:</strong> ${asiento}<br>
        <strong>Pago:</strong> ${pago}`;

        $('#confirmacion').html(mensaje).fadeIn();
        $('#reservaForm')[0].reset();
        $('#formModal').modal('hide');
      });
    });