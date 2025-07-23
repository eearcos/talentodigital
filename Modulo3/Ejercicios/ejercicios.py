"""
Ejercicio: Calculadora de Ganancias de una Frutería
Objetivo: Escribir un script en Python para calcular la ganancia total de la venta de manzanas y naranjas en un día.
Instrucciones:
Define las variables para los precios y las cantidades vendidas según los siguientes datos:
Precio por kilo de manzanas: $950
Precio por kilo de naranjas: $1300
Kilos de manzanas vendidos: 10
Kilos de naranjas vendidos: 15
Calcula la ganancia obtenida por cada tipo de fruta.
Suma las ganancias para obtener el total del día.
Muestra el resultado en la consola utilizando un f-string. El mensaje debe tener el siguiente formato, mostrando el total con dos decimales:  Ganaste $monto_total hoy!
"""

pxkilomanzanas = 950
pxkilonaranjas = 1300

kilosmanzanasvendidos = 10
kilosnaranjasvendidos = 15

gananciamanzanas = pxkilomanzanas * kilosmanzanasvendidos
ganancianaranjas = pxkilonaranjas * kilosnaranjasvendidos

montototal = gananciamanzanas + ganancianaranjas

print(f"Ganaste ${montototal} hoy!")