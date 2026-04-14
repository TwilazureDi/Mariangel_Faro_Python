class TarjetaCredito:
    
    coleccion_tarjetas = []

    def __init__(self,nombre, saldo_pagar=0, limite_credito=30000, intereses=0.02):
        self.nombre = nombre
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

        TarjetaCredito.coleccion_tarjetas.append(self)

       

    def compra(self, monto):
        if TarjetaCredito.puede_comprar(self.limite_credito, self.saldo_pagar, monto):
            self.saldo_pagar += monto
            return self
        else:
            print("la tarjeta alcanzo su limite!")
            return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar de la tarjeta {self.nombre}: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.intereses
        return self

    @classmethod
    def mostrar_coleccion_tarjetas(cls):
        print("Tarjetas registradas: y su saldo")
        for tarjeta in cls.coleccion_tarjetas:
            print(f"{tarjeta.nombre}: {tarjeta.saldo_pagar}")
        

    @staticmethod
    def puede_comprar(limite, saldo, monto):
        if(saldo + monto) > limite:
            return False
        else:
            return True
    
#Ejercicios debajo

'''tarjetaA = TarjetaCredito("a")
tarjetaB = TarjetaCredito("b", 300, 400000, 0.10)
tarjetaC = TarjetaCredito("c", 0, 1000000, 0.30)
print("TarjetaA: ")
tarjetaA.compra(500).compra(2000).pago(2000).cobrar_interes().mostrar_info_tarjeta()
print(" ")
print("TarjetaB: ")
tarjetaB.compra(6000).compra(400).compra(30).pago(6400).pago(10).cobrar_interes().mostrar_info_tarjeta()

print(" ")
print("TarjetaC: ")
tarjetaC.compra(5).compra(5).compra(60000).compra(30000).compra(40000000)
print(" ")
TarjetaCredito.mostrar_coleccion_tarjetas()'''
