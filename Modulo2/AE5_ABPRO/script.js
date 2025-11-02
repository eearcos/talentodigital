// LibroLibre - Funcionalidad JavaScript
// Autor: Asistente Claude
// Descripción: Script para manejo de búsqueda, validación y eventos

// Función principal que se ejecuta cuando el DOM está cargado
document.addEventListener('DOMContentLoaded', function() {
    console.log('LibroLibre - Script cargado correctamente');
    
    // Inicializar contadores y elementos
    inicializarElementos();
    
    // Configurar eventos
    configurarEventos();
    
    // Mostrar estadísticas iniciales
    actualizarContadorLibros();
});

// Variables globales
let totalLibros = 0;
let librosVisibles = 0;

// Función para inicializar elementos del DOM
function inicializarElementos() {
    const libros = document.querySelectorAll('.libro');
    totalLibros = libros.length;
    librosVisibles = totalLibros;
    
    console.log(`Total de libros en el catálogo: ${totalLibros}`);
    
    // Crear contador visual
    crearContadorLibros();
}

// Función para crear y mostrar contador de libros
function crearContadorLibros() {
    const catalogoSection = document.getElementById('catalogo');
    
    // Verificar si ya existe el contador
    if (!document.getElementById('contador-libros')) {
        const contadorDiv = document.createElement('div');
        contadorDiv.id = 'contador-libros';
        contadorDiv.style.cssText = `
            background-color: #f0f0f0;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            font-weight: bold;
            text-align: center;
        `;
        
        // Insertar después del botón de búsqueda
        const botonBuscar = catalogoSection.querySelector('button');
        botonBuscar.insertAdjacentElement('afterend', contadorDiv);
    }
    
    actualizarContadorLibros();
}

// Función para actualizar el contador de libros
function actualizarContadorLibros() {
    const contador = document.getElementById('contador-libros');
    if (contador) {
        // Expresión aritmética para calcular porcentaje
        const porcentaje = totalLibros > 0 ? Math.round((librosVisibles / totalLibros) * 100) : 0;
        
        contador.innerHTML = `
            Mostrando: ${librosVisibles} de ${totalLibros} libros 
            (${porcentaje}% del catálogo)
        `;
        
        console.log(`Libros visibles: ${librosVisibles}/${totalLibros} (${porcentaje}%)`);
    }
}

// Función para configurar todos los eventos
function configurarEventos() {
    // Evento para el campo de búsqueda (input en tiempo real)
    const textboxBusqueda = document.getElementById('textbox');
    if (textboxBusqueda) {
        textboxBusqueda.addEventListener('input', function() {
            console.log('Búsqueda en tiempo real:', this.value);
            mostrarOcultarDiv();
        });
        
        // Evento para limpiar búsqueda con Escape
        textboxBusqueda.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                this.value = '';
                mostrarOcultarDiv();
                console.log('Búsqueda limpiada con Escape');
            }
        });
    }
    
    // Evento onclick para el botón de búsqueda
    const botonBuscar = document.querySelector('#catalogo button');
    if (botonBuscar) {
        botonBuscar.addEventListener('click', function() {
            console.log('Búsqueda activada por botón');
            mostrarOcultarDiv();
            
            // Feedback visual del botón
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 100);
        });
    }
    
    // Eventos para el formulario de registro
    configurarFormularioRegistro();
    
    // Eventos para los libros (hover y click)
    configurarEventosLibros();
}

// Función principal para mostrar/ocultar libros según búsqueda
function mostrarOcultarDiv() {
    const textoBusqueda = document.getElementById('textbox').value.toLowerCase().trim();
    const libros = document.querySelectorAll('.libro');
    
    librosVisibles = 0; // Reiniciar contador
    
    console.log('Iniciando búsqueda:', textoBusqueda);
    
    libros.forEach(function(libro, index) {
        const titulo = libro.querySelector('h3').textContent.toLowerCase();
        const autor = libro.querySelector('p:nth-child(2)').textContent.toLowerCase();
        const genero = libro.querySelector('p:nth-child(3)').textContent.toLowerCase();
        
        // Lógica de búsqueda: buscar en título, autor o género
        const coincide = textoBusqueda === '' || 
                        titulo.includes(textoBusqueda) || 
                        autor.includes(textoBusqueda) || 
                        genero.includes(textoBusqueda);
        
        if (coincide) {
            libro.style.display = 'block';
            libro.style.opacity = '1';
            libro.style.transform = 'translateY(0)';
            librosVisibles++;
            
            console.log(`Libro ${index + 1} mostrado:`, titulo);
        } else {
            libro.style.display = 'none';
            libro.style.opacity = '0';
            libro.style.transform = 'translateY(-10px)';
            
            console.log(`Libro ${index + 1} oculto:`, titulo);
        }
    });
    
    // Actualizar contador con expresión aritmética
    actualizarContadorLibros();
    
    // Mostrar mensaje si no hay resultados
    mostrarMensajeNoResultados();
}

// Función para mostrar mensaje cuando no hay resultados
function mostrarMensajeNoResultados() {
    const catalogoSection = document.getElementById('catalogo');
    let mensajeExistente = document.getElementById('mensaje-no-resultados');
    
    if (librosVisibles === 0 && document.getElementById('textbox').value.trim() !== '') {
        if (!mensajeExistente) {
            const mensaje = document.createElement('div');
            mensaje.id = 'mensaje-no-resultados';
            mensaje.style.cssText = `
                text-align: center;
                padding: 20px;
                background-color: #ffe6e6;
                border: 1px solid #ffcccc;
                border-radius: 5px;
                margin: 20px 0;
                color: #cc0000;
            `;
            mensaje.innerHTML = '📚 No se encontraron libros que coincidan con tu búsqueda.';
            catalogoSection.appendChild(mensaje);
        }
    } else if (mensajeExistente) {
        mensajeExistente.remove();
    }
}

// Función para configurar eventos del formulario de registro
function configurarFormularioRegistro() {
    const seccionRegistro = document.getElementById('registro');
    const campos = seccionRegistro.querySelectorAll('input');
    const botonRegistro = seccionRegistro.querySelector('button');
    
    // Validación en tiempo real para cada campo
    campos.forEach(function(campo, index) {
        campo.addEventListener('input', function() {
            validarCampo(campo);
        });
        
        campo.addEventListener('blur', function() {
            validarCampo(campo);
        });
        
        // Cambio de evento onchange para campos específicos
        campo.addEventListener('change', function() {
            console.log(`Campo ${index + 1} modificado:`, this.value);
            validarFormulario();
        });
    });
    
    // Evento onclick para el botón de registro
    if (botonRegistro) {
        botonRegistro.addEventListener('click', function(event) {
            event.preventDefault();
            console.log('Intento de registro iniciado');
            
            if (validarFormularioCompleto()) {
                procesarRegistro();
            }
        });
    }
}

// Función de validación individual de campo
function validarCampo(campo) {
    const valor = campo.value.trim();
    const tipo = campo.type;
    let esValido = true;
    let mensajeError = '';
    
    // Limpiar estilos previos
    campo.style.borderColor = '';
    
    // Validaciones según tipo de campo
    switch (tipo) {
        case 'text': // Nombre completo
            if (valor.length < 2) {
                esValido = false;
                mensajeError = 'El nombre debe tener al menos 2 caracteres';
            } else if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(valor)) {
                esValido = false;
                mensajeError = 'El nombre solo puede contener letras y espacios';
            }
            break;
            
        case 'email':
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(valor)) {
                esValido = false;
                mensajeError = 'Por favor ingresa un email válido';
            }
            break;
            
        case 'password':
            if (valor.length < 6) {
                esValido = false;
                mensajeError = 'La contraseña debe tener al menos 6 caracteres';
            }
            break;
    }
    
    // Aplicar estilos según validación
    if (!esValido && valor !== '') {
        campo.style.borderColor = '#ff0000';
        campo.style.borderWidth = '2px';
        mostrarMensajeError(campo, mensajeError);
    } else if (esValido && valor !== '') {
        campo.style.borderColor = '#00cc00';
        campo.style.borderWidth = '2px';
        ocultarMensajeError(campo);
    }
    
    return esValido;
}

// Función para validar formulario completo
function validarFormulario() {
    const campos = document.querySelectorAll('#registro input');
    let todosValidos = true;
    let camposCompletos = 0;
    
    campos.forEach(function(campo) {
        if (campo.value.trim() === '') {
            todosValidos = false;
        } else {
            camposCompletos++;
            if (!validarCampo(campo)) {
                todosValidos = false;
            }
        }
    });
    
    // Expresión aritmética para progreso
    const progreso = Math.round((camposCompletos / campos.length) * 100);
    console.log(`Progreso del formulario: ${camposCompletos}/${campos.length} campos (${progreso}%)`);
    
    return todosValidos;
}

// Función para validación completa del formulario
function validarFormularioCompleto() {
    const campos = document.querySelectorAll('#registro input');
    let formularioValido = true;
    
    campos.forEach(function(campo) {
        if (campo.value.trim() === '') {
            formularioValido = false;
            campo.style.borderColor = '#ff0000';
            campo.style.borderWidth = '2px';
            mostrarMensajeError(campo, 'Este campo es obligatorio');
        } else if (!validarCampo(campo)) {
            formularioValido = false;
        }
    });
    
    if (!formularioValido) {
        alert('Por favor completa todos los campos correctamente antes de continuar.');
        console.log('Validación de formulario fallida');
    }
    
    return formularioValido;
}

// Función para procesar el registro exitoso
function procesarRegistro() {
    const campos = document.querySelectorAll('#registro input');
    const datosUsuario = {};
    
    // Recopilar datos
    campos.forEach(function(campo, index) {
        const nombres = ['nombre', 'email', 'password'];
        datosUsuario[nombres[index]] = campo.value.trim();
    });
    
    console.log('Registro exitoso:', datosUsuario);
    
    // Simular procesamiento
    const boton = document.querySelector('#registro button');
    const textoOriginal = boton.textContent;
    
    boton.textContent = 'Registrando...';
    boton.disabled = true;
    
    setTimeout(function() {
        alert(`¡Registro exitoso! Bienvenido/a, ${datosUsuario.nombre}`);
        
        // Limpiar formulario
        campos.forEach(function(campo) {
            campo.value = '';
            campo.style.borderColor = '';
            campo.style.borderWidth = '';
            ocultarMensajeError(campo);
        });
        
        boton.textContent = textoOriginal;
        boton.disabled = false;
        
        console.log('Proceso de registro completado y formulario reiniciado');
    }, 1500);
}

// Función para mostrar mensaje de error en campo
function mostrarMensajeError(campo, mensaje) {
    ocultarMensajeError(campo); // Limpiar mensaje previo
    
    const mensajeDiv = document.createElement('div');
    mensajeDiv.className = 'mensaje-error';
    mensajeDiv.style.cssText = `
        color: #ff0000;
        font-size: 12px;
        margin-top: 5px;
        padding: 2px 5px;
        background-color: #ffe6e6;
        border-radius: 3px;
    `;
    mensajeDiv.textContent = mensaje;
    
    campo.parentNode.insertBefore(mensajeDiv, campo.nextSibling);
}

// Función para ocultar mensaje de error
function ocultarMensajeError(campo) {
    const mensajeExistente = campo.parentNode.querySelector('.mensaje-error');
    if (mensajeExistente) {
        mensajeExistente.remove();
    }
}

// Función para configurar eventos de los libros
function configurarEventosLibros() {
    const libros = document.querySelectorAll('.libro');
    
    libros.forEach(function(libro, index) {
        // Evento hover (mouseenter y mouseleave)
        libro.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.02)';
            this.style.transition = 'transform 0.2s ease';
            this.style.boxShadow = '0 4px 8px rgba(0,0,0,0.1)';
            console.log(`Hover en libro ${index + 1}`);
        });
        
        libro.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
            this.style.boxShadow = 'none';
        });
        
        // Evento click para mostrar detalles
        libro.addEventListener('click', function() {
            const titulo = this.querySelector('h3').textContent;
            const autor = this.querySelector('p:nth-child(2)').textContent;
            const genero = this.querySelector('p:nth-child(3)').textContent;
            const descripcion = this.querySelector('p:last-child').textContent;
            
            alert(`📖 Detalles del libro:\n\n${titulo}\n${autor}\n${genero}\n\n${descripcion}`);
            
            console.log(`Click en libro: ${titulo}`);
        });
    });
}

// Función de depuración para mostrar información en consola
function mostrarEstadisticasDebug() {
    console.group('📊 Estadísticas LibroLibre');
    console.log(`Total de libros: ${totalLibros}`);
    console.log(`Libros visibles: ${librosVisibles}`);
    console.log(`Término de búsqueda actual: "${document.getElementById('textbox').value}"`);
    console.log(`Formulario válido: ${validarFormulario()}`);
    console.groupEnd();
}

// Exponer función de debug globalmente para testing en consola
window.debugLibroLibre = mostrarEstadisticasDebug;

// Mensaje de bienvenida en consola
console.log(`
🚀 LibroLibre JavaScript cargado exitosamente!
📋 Funcionalidades disponibles:
   • Búsqueda dinámica por título, autor o género
   • Validación completa de formulario de registro
   • Conteo automático de libros visibles
   • Eventos interactivos (hover, click)
   • Depuración con: window.debugLibroLibre()

🔧 Para depurar, escribe en la consola: debugLibroLibre()
`);