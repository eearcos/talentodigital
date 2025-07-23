matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0]= 6
print(matriz)

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

for cantante in cantantes:
    print(f"Nombre: {cantante['nombre']}, País: {cantante['pais']}")

for cantante in cantantes:
    print(f"Nombre: {cantante['nombre']}")

for cantante in cantantes:
    print(f"Pais: {cantante['pais']}")

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2]="Monterrey"
print(ciudades)

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
x=coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431

print(coordenadas)

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

for x, y in costa_rica.items():
    print(f"{len(y)} {x.upper()}")
    for z in y:
        print(z)
