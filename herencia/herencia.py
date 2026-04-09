#herencia

class Animal:
    def __init__(self,nombre):
        self.nombre  = nombre

    def respirar(self):
        print("respirando ando")



class Perro(Animal):
    def ladrar(self):
        print("guau guau")

#firulais = Perro("firulais")
#firulais.respirar() # metodo de animal heredado
#firulais.ladrar() # metodo del propio perro

#polimorfismo

class Ave:
    def volar(self): #metodo sin implementacion 
        pass

class Aguila(Ave):
    def volar(self):  # metodo sobreescrito
        print("ando volando son una agila")


#pichon = Aguila()
#pichon.volar()

#isinstance()

class Pago:
    def __init__(self, monto):
        self.monto = monto 
    
class Efectivo(Pago):
    pass

class Tarjeta(Pago):
    pass

class Cheque(Pago):
    pass 




#validar los tipos de pago 
def verificar_pago(obj):
    if not isinstance(obj, Pago):
        print("este objeto no es un pago valido")
    if isinstance(obj, Efectivo):
        print("abriendo caja manual")
    if isinstance(obj,Tarjeta ):
        print("pasando redbank")
    if isinstance(obj,Cheque):
        print("mandando a banco")

pagare = Pago(100)
cheque1 = Cheque(100)
tarjeta1 = Tarjeta(100)
efectivo1 = Efectivo(100) 

verificar_pago(efectivo1)
    

#super()


class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario


class Desarrollador(Empleado):
    def __init__(self, nombre, salario,lenguaje):
        super().nombre # nos traemos todos los atributos de empleado y agregamos los que son de  desarrollador solamente
        self.lenguaje = lenguaje






