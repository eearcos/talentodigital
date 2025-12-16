class Tamagotchi:
    def __init__(self, nombre, color, salud=50, felicidad=50, energia=50):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        print(f"{self.nombre} está jugando 🎮")
        self.felicidad += 10
        self.salud -= 5

    def comer(self):
        print(f"{self.nombre} está comiendo 🍖")
        self.felicidad += 5
        self.salud += 10

    def curar(self):
        print(f"{self.nombre} está siendo curado 🏥")
        self.salud += 20
        self.felicidad -= 5


class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        print(f"{self.nombre} juega con {self.tamagotchi.nombre}")
        self.tamagotchi.jugar()

    def darle_comida(self):
        print(f"{self.nombre} alimenta a {self.tamagotchi.nombre}")
        self.tamagotchi.comer()

    def curarlo(self):
        print(f"{self.nombre} cura a {self.tamagotchi.nombre}")
        self.tamagotchi.curar()


tama = Tamagotchi("Pixel", "Azul")
persona = Persona("Esteban", "Arcos", tama)

persona.darle_comida()
persona.curarlo()
persona.jugar_con_tamagotchi()

print("\n--- Estado final del Tamagotchi ---")
print("Salud:", tama.salud)
print("Felicidad:", tama.felicidad)
print("Energía:", tama.energia)

