from TarjetaCredito_practicas import TarjetaCredito

class Usuario:
    def __init__(self, nombre, apellido, email,tarjeta_nombre = "Tarjeta 1"):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = [TarjetaCredito(tarjeta_nombre)]
  
    def hacer_compra(self, monto, numTarjeta = 0):  #recibe como argumento el monto de la compra
        self.tarjetas[numTarjeta].compra(monto)
        print( f"realizo una compra de: ${monto} con la tarjeta {self.tarjetas[numTarjeta].nombre}")
        return self

    def pagar_tarjeta(self,monto, numTarjeta = 0):
        self.tarjetas[numTarjeta].pago(monto)
        print( f"Pago: ${monto} del credito de la tarjeta {self.tarjetas[numTarjeta].nombre}")
        return self

    def mostrar_saldo(self, numTarjeta = 0):
        self.tarjetas[numTarjeta].mostrar_info_tarjeta()
        return self

    def pedir_tarjeta(self, tarjetaNombre):
        self.tarjetas.append(TarjetaCredito(tarjetaNombre))

ana = Usuario("Ana", "Rosales", "mail.com", "tarjeta1")

ana.hacer_compra(500)