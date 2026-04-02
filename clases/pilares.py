
#Pilares de la poo 


#encapsulacion 

class CuentaBancaria:

    def __init__(self, titular , saldo):
        self.titular = titular
        self.__saldo = saldo  #se puede encapsular con __ 2 barras para ocultar metodos o atributos
    

    # esto cambia el nombre del objeto de esto  <__main__.CuentaBancaria object at 0x767d49e87950> 
    # a esto  esto es el objeto:{self.titular} y tiene un saldo de:{self.saldo}
    def __str__(self):
        return f"esto es el objeto:{self.titular} y tiene un saldo de:{self.__saldo}"
        
    def __depositar(self, monto):
        if monto >= 0:
            self.__saldo += monto

                      #100000
    def retirar(self, monto):
        if monto < self.__saldo:
            self.__saldo -= monto
        else:
            print("retiro no es posible trabaje mas")

cuenta1 = CuentaBancaria("juanito", 10000)
cuenta2 = CuentaBancaria("marcela", 100)

# esto es el objeto <__main__.CuentaBancaria object at 0x767d49e87950>
#cuenta1.retirar(10000)
#cuenta1.__depositar(1000)
#print(cuenta1)




#herencia

class Vehiculo:
    def __init__(self,marca,cant_ruedas):
        self.marca = marca
        self.cant_ruedas = cant_ruedas

    def moverse(self):
        print("auto se movio!!")



class Auto(Vehiculo):
    def moverse(self):
        print("auto moviendose")

class Moto(Vehiculo):
    def __init__(self, marca, cant_ruedas,ruedas):
        super().__init__(marca, cant_ruedas)
        

    def moverse(self):
        print("moto moviendose")


class Rueda:
    pass




auto = Auto("byd")
moto = Moto("ktm")

auto.moverse()
moto.moverse()



