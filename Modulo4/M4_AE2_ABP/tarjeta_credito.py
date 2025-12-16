class TarjetaCredito:

    def __init__(self, saldo_pagar, limite_credito, intereses):

        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):
        if monto + self.saldo_pagar < self.limite_credito:
            self.saldo_pagar += monto
            print("Compra realizada con éxito.")
        else:
            print("Compra denegada: excede el límite de crédito.")
        return self.saldo_pagar
    
    def pago(self, monto):
        if monto <= self.saldo_pagar:
            self.saldo_pagar -= monto
            print("Pago realizado con éxito.")
        else:
            print("El monto del pago excede el saldo a pagar.")
        return self.saldo_pagar

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: {self.saldo_pagar}")

    def cobrar_interes(self):
        interes_cobrado = self.saldo_pagar * self.intereses
        self.saldo_pagar += interes_cobrado
        print(f"Interés cobrado: {interes_cobrado}")
        return self.saldo_pagar
todas_las_tarjetas = []

@classmethod
def imprimir_todas_las_tarjetas(cls):
    print("Información de todas las tarjetas de crédito:")
    if not cls.todas_las_tarjetas:
        print("No hay tarjetas registradas.")
        return
    for i, tarjeta in enumerate(cls.todas_las_tarjetas):
        print(f"\nTarjeta {i + 1}:")
        tarjeta.mostrar_info_tarjeta()
        print(f"------------------------")

tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.03)
tarjeta2 = TarjetaCredito(limite_credito=2500, intereses=0.015, saldo_pagar=50) # Saldo inicial de $50
tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.02)


tarjeta1.compra(500).compra(150).pago(200).cobrar_interes().mostrar_info_tarjeta()

tarjeta2.compra(1000).compra(300).compra(500).pago(800).pago(200).cobrar_interes().mostrar_info_tarjeta()

tarjeta3.compra(100).compra(150).compra(100).compra(100).compra(100).mostrar_info_tarjeta()

TarjetaCredito.imprimir_todas_las_tarjetas()