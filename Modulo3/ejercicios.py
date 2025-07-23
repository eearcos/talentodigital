import random

dado = random.randint(1, 6)

intento = input("Introduce un número:")
if int(intento) == dado:
    print("¡Has acertado!")
else:
    print("Has fallado. El número era:", dado)
