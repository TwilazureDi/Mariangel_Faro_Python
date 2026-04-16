class Tamagochi:
    def __init__ (self, nombre:str, color:str, salud = 100, energia = 100, felicidad = 50):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.energia = energia
        self.felicidad = felicidad

    def jugar(self):
        if Tamagochi.puede_gastar_salud(self.salud, 5):
            if Tamagochi.puede_gastar_energia(self.energia, 10):
                self.felicidad = Tamagochi.agregar_felicidad(self.nombre, self.felicidad, 10)
                self.energia -= 10
                self.salud -= 5 
                print(f"Jugaste con {self.nombre}! felicidad sube a 10, energia baja 10, salud baja 5")
                return self
            else:
                print(f"{self.nombre} se encuentra cansado, solo tiene {self.energia}, no puedes realizar esta accion")
                return self
        else:
            print(f"{self.nombre} solo le queda {self.salud}! No puedes realizar esta accion")
            return self
            
    def comer(self):
        self.felicidad = Tamagochi.agregar_felicidad(self.nombre, self.felicidad, 5)
        self.energia = Tamagochi.agregar_energia(self.nombre, self.energia, 10)
        print(f"{self.nombre} comio y recupero 10 de energia y 5 de felicidad!")
        return self

    def curar(self):
        self.agregar_salud = Tamagochi.agregar_salud(self.nombre, self.salud, 20)
        self.felicidad = Tamagochi.quitar_felicidad(self.felicidad, 5)
        print(f"{self.nombre} descanso y tomo su medicina... aunque no le gusto mucho. Recupero 20 de energia y la felicidad bajo a 5")
        return self

    def estado_actual(self):
        print("-----------------")
        print(f"Estado actual de {self.nombre}:")
        print(f"Salud: {self.salud}")
        print(f"Energia: {self.energia}")
        print(f"Felicidad: {self.felicidad}")
        print("-----------------")
        return self

    
    @staticmethod
    def puede_gastar_salud(salud_acumulada, salud_quitada):
        if(salud_acumulada - salud_quitada) < 0:
            return False
        else:
            return True

    @staticmethod
    def agregar_salud(nombre, salud_acumulada, salud_agregada):
        if(salud_acumulada + salud_agregada) > 100:
            print(f"{nombre} esta en perfecta forma!")
            return 100
        else:
            return salud_acumulada + salud_agregada

    @staticmethod
    def quitar_felicidad(felicidad_acumulada, felicidad_quitada):
        if(felicidad_acumulada - felicidad_quitada) < 0:
            print("La felicidad no puede disminuir mas!")
            return 0
        else:
            return felicidad_acumulada - felicidad_quitada

    @staticmethod
    def agregar_felicidad(nombre, felicidad_acumulada, felicidad_Agregada):
        if(felicidad_acumulada + felicidad_Agregada) > 100:
            print(f"{nombre} no puede ser mas feliz!")
            return 100
        else:
            return felicidad_acumulada + felicidad_Agregada

    @staticmethod
    def agregar_energia(nombre, energia_acumulada, energia_Agregada):
        if(energia_acumulada + energia_Agregada) > 100:
            print(f"{nombre} esta al tope de energia!")
            return 100
        else:
            return energia_acumulada + energia_Agregada

    @staticmethod
    def puede_gastar_energia(energia_acumulada, energia_agregada):
        if(energia_acumulada - energia_agregada) < 0:
            return False
        else:
            return True

    


#amy = Tamagochi("Amelia","yellow")
#amy.jugar().jugar().jugar().comer().curar().estado_actual()