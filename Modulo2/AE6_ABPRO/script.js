
$(document).ready(function() {
  $('.reservar-btn').click(function() {
    const pelicula = $(this).data('pelicula');
    $('#pelicula').val(pelicula);
    $('#formularioReserva').slideDown();
    $('#confirmacion').hide();
  });

  $('#reservaForm').submit(function(event) {
    event.preventDefault();
    const pelicula = $('#pelicula').val();
    const horario = $('#horario').val();
    const asiento = $('#asiento').val();
    const pago = $('#pago').val();

    const mensaje = `🎟️ Reserva Confirmada:<br>
    <strong>Película:</strong> ${pelicula}<br>
    <strong>Horario:</strong> ${horario}<br>
    <strong>Asiento:</strong> ${asiento}<br>
    <strong>Pago:</strong> ${pago}`;

    $('#confirmacion').html(mensaje).fadeIn();
    $('#reservaForm')[0].reset();
    $('#formularioReserva').hide();
  });
});
