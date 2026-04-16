import Tamagochi

class Persona:
    def __init__(self, nombre:str, apellido:str, tamagochi:Tamagochi.Tamagochi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagochi = tamagochi

    def jugar_con_tamagochi(self):
        self.tamagochi.jugar()
        return self

    def darle_comer(self):
        self.tamagochi.comer()
        return self

    def curar_tamagochi(self):
        self.tamagochi.curar()
        return self

    def chequear_estado_tamagochi(self):
        self.tamagochi.estado_actual()
        return self

migu = Tamagochi.Tamagochi("Migu","Azul")
lisa = Persona("Lisa", "Del valle", migu)

lisa.jugar_con_tamagochi().jugar_con_tamagochi().darle_comer().curar_tamagochi().chequear_estado_tamagochi()