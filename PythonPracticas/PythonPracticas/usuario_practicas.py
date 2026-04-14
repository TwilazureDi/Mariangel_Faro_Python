class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
  
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto
        return self

    def pagar_tarjeta(self,monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_saldo(self):
        print( f"Usuario: {self.nombre} {self.apellido}, Saldo a pagar: ${self.saldo_pagar}")
        return self

    def transferir_deuda(self, otro_usuario:Usuario, monto):

        self.saldo_pagar -= monto
        otro_usuario.saldo_pagar += monto

        return self


#--- Usuarios ----
ana = Usuario("Ana", "Rosales", "anarosales.com")
daniel = Usuario("Daniel", "Larosse", "danielLarosse.com") 
pedro = Usuario("Pedro", "Rodrigres", "pedrorodrigez.com")


#--- Movimientos de Ana
ana.hacer_compra(45).hacer_compra(80).pagar_tarjeta(100).mostrar_saldo()

#--- Movimientos de Daniel

daniel.hacer_compra(400).pagar_tarjeta(250).pagar_tarjeta(150).mostrar_saldo()

#--- Movimientos de Pedro
pedro.hacer_compra(500).hacer_compra(25).hacer_compra(120).pagar_tarjeta(300).pagar_tarjeta(10).pagar_tarjeta(200).pagar_tarjeta(1).mostrar_saldo()
print("- Pedro le pide prestado a Daniel")
pedro.transferir_deuda(daniel,134).mostrar_saldo()

daniel.mostrar_saldo()
