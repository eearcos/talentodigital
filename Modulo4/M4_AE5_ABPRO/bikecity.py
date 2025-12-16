class ReservaInvalidaError(Exception):
    """Excepción para manejar errores específicos en reservas."""
    pass

class Bicicleta:
    def __init__(self, id_bici, estado="disponible"):
        self.id_bici = id_bici
        self.estado = estado

    def marcar_reservada(self):
        if self.estado != "disponible":
            raise ReservaInvalidaError(f"La bicicleta {self.id_bici} no está disponible.")
        self.estado = "reservada"

    def marcar_disponible(self):
        self.estado = "disponible"

class Reserva:
    def __init__(self, cliente, bicicleta, horas):
        if horas <= 0:
            raise ValueError("La cantidad de horas debe ser mayor a cero.")
        
        self.cliente = cliente
        self.bicicleta = bicicleta
        self.horas = horas

    def calcular_costo(self):
        tarifa_por_hora = 2500
        return self.horas * tarifa_por_hora

class SistemaReservas:
    def __init__(self):
        self.bicicletas = {}
        self.reservas = []

    def registrar_bicicleta(self, id_bici):
        self.bicicletas[id_bici] = Bicicleta(id_bici)

    def reservar(self, cliente, id_bici, horas):
        try:
            if id_bici not in self.bicicletas:
                raise KeyError("La bicicleta no existe en el sistema.")

            bicicleta = self.bicicletas[id_bici]

            bicicleta.marcar_reservada()

            reserva = Reserva(cliente, bicicleta, horas)
            self.reservas.append(reserva)

            print(f"Reserva creada para {cliente}. Costo: ${reserva.calcular_costo()}")

        except (ValueError, TypeError) as e:
            print("Error de datos en la reserva:", e)

        except ReservaInvalidaError as e:
            print("Error en la reserva:", e)

        except Exception as e:
            print("Error inesperado:", e)

        finally:
            print(f"Intento de reserva para bicicleta {id_bici} procesado.\n")

    def liberar_bicicleta(self, id_bici):
        if id_bici in self.bicicletas:
            self.bicicletas[id_bici].marcar_disponible()

sistema = SistemaReservas()

sistema.registrar_bicicleta("B1")
sistema.registrar_bicicleta("B2")

sistema.reservar("Juan", "B1", 3)

sistema.reservar("Pedro", "B1", 2)

sistema.reservar("Luis", "B2", 0)

sistema.reservar("Ana", "B3", 2)
