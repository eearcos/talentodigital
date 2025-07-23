num_productos= input("Ingrese el número de productos que desea llevar: ")
"""Si el cliente compra más de 10 productos, obtiene un 10% de descuento"""
cliente_frecuente= input("¿Cuántas compras previas ha realizado en esta tienda? Ingrese el número:")
"""Si el cliente es frecuente (más de 5 compras previas), se aplica 5% adicional"""
monto_total= input("Cuál es el monto de su compra? Ingrese el monto: ")
"""Si la compra supera los 500 dólares, se otorga un descuento adicional de 7%"""
dia_promo = input("¿Qué día de la semana es hoy? Ingrese el día: ")
"""Los viernes se aplica un 15% de descuento adicional"""
num_productos_desct= 10
cliente_frecuente_desct = 5
monto_total_desct = 7
dia_promo_desct = 15
if int(num_productos) > 10:
    descuento_prod = int(num_productos_desct)
else:
    descuento_prod = 0
if int(cliente_frecuente) > 5:
    descuento_freq = int(cliente_frecuente_desct)
else:
    descuento_freq = 0
if int(monto_total) > 500:
    descuento_monto = int(monto_total_desct)
else:
    descuento_monto = 0
if str(dia_promo) == "viernes":
    descuento_dia = int(dia_promo_desct)
else:
    descuento_dia = 0
total_descuento = descuento_prod + descuento_freq + descuento_monto + descuento_dia
if total_descuento >= 30:
    total_descuento = 30
else:
    total_descuento = descuento_prod + descuento_freq + descuento_dia + descuento_monto

print("El total de descuento es: "+ str(total_descuento) +"%")