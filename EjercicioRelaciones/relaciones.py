

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo 


class Auto:
    def __init__(self, patente, motor):
        self.patente = patente
        self.motor = motor 


class Cliente:
    def __init__(self, nombre): #asociacion 
        self.nombre = nombre
        self.autos = []

    def __str__(self):
        return f"{self.nombre}"


    def agregar_autos(self, auto):
        self.autos.append(auto)

class Mecanico:
    def __init__(self,nombre):
        self.nombre = nombre

    def reparar_auto(self,auto):
        return f"reparando auto"
    

class Reparacion:
    def __init__(self, auto, mecanico):
        self.auto = auto
        self.mecanico = mecanico

    def __str__(self):
        return f"{self.mecanico.nombre} _ esta reparando el auto {self.auto.patente}_ con motor {self.auto.motor}"



        
cliente1 = Cliente("pepito")

motor = Motor("6 en linea")

auto1 = Auto("xx3434",motor)


mecanico1 = Mecanico("federico")


reparacion1 = Reparacion(auto1,mecanico1)
print(reparacion1)

