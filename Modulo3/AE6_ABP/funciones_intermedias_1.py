matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]
#1. Actualizar valores en diccionarios y listas

# Cambia el valor de 3 en matriz por 6.
matriz[1][0] = 6

# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0]["nombre"] = "Enrique Martin Morales"

# En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"

# En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = 9.9355431

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"},
   {"nombre": "Luis Miguel", "pais": "México"},
   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# 2. Iterar a través de una lista de diccionarios

def iterarDiccionario(lista):
   for diccionario in lista:
      output_parts = []
      for llave, valor in diccionario.items():
         output_parts.append(f"{llave} - {valor}")
      
      print(", ".join(output_parts))

# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
   for diccionario in lista:
      if llave in diccionario:
         print(diccionario[llave])

# 4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
   for llave, lista in diccionario.items():
      print(f"{len(lista)} {llave.upper()}")
      for elemento in lista:
         print(elemento)
      print() 