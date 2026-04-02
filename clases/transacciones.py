class Transaccion:
    
    def __init__(self, monto,descripcion):
        self.__monto = monto
        self.descripcion = descripcion
    
    def get_monto(self):
        return self.__monto      
    
    def set_monto(self,monto):
        if monto > 0:
           self.__monto = monto
        else:
           print("monto ingresado es 0 o menor de 0")

    def tipo(self):
        return "Transaccion"
        
    def mostrar(self):
        return f"{self.descripcion} - {self.get_monto()} - {self.tipo()} "
    
    def __str__(self):
        return f"{self.descripcion} - {self.get_monto()} - {self.tipo()} "
        
    
#pago1 = Transaccion(100, "pago banco")
#print(pago1)
#print(pago1.mostrar())

class Ingreso(Transaccion):
    #polimorfismo del metodo tipo de la clase transaccion 
    def __init__(self, monto, descripcion):
        super().__init__(monto, descripcion)
    def tipo(self):
        return "Ingreso"
        
        
class Egreso(Transaccion):
    #polimorfismo del metodo tipo de la clase transaccion 
    def tipo(self):
        return "Egreso"

class GestorFinanzas:
    def __init__(self):
        self.transacciones = [] #lista vacia
        

    def agregar(self,transaccion):
        if not isinstance(transaccion, Transaccion):
            raise TypeError("Debe ser una transaccion valida")
        self.transacciones.append(transaccion)
        print("transaccion agregada")

    def mostrar_todo(self):
        return [t.mostrar() for t in self.transacciones]
        

    def calcular_balance(self):
        balance = 0
        for transaccion in self.transacciones:
            if not isinstance(transaccion, Ingreso):
                balance += transaccion.get_monto()
            else:
                balance -= transaccion.get_monto()
            return 
            

            
















    def guardar_en_archivo(self):
        pass

    def importar_del_archivo(self):
        pass
    
    

        
ingreso = Ingreso(100,"ingreso")
egreso = Egreso(100, "dasdda")
gestor = GestorFinanzas()

variable= "texto"


gestor.agregar(egreso)
gestor.agregar(ingreso)

print(gestor.mostrar_todo())



