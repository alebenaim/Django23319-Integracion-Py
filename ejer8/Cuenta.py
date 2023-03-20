from Persona import Persona

class Cuenta:
    def __init__(self, titular, cantidad):
        if titular != None:
            self.__titular = titular
            flag = True
            while flag:
                try: 
                    self.__cantidad = cantidad
                    flag = False
                except ValueError:    
                    x=float(input("Cantidad invalida. Reingrese: "))
        else:
            print ("Titular invalido, no se puede crear la cuenta")      
                   
    @property
    def titular(self):
        return (self.__titular)
    
    @titular.setter
    def titular(self,nuevo_titular):
        self.__titular = nuevo_titular

    @property
    def cantidad(self):
        return (self.__cantidad)
    
    @cantidad.setter
    def cantidad(self,nueva_cantidad):   
        self.__cantidad=nueva_cantidad 


    def mostrar(self):
        return (f"Titular de la cuenta {self.titular.mostrar()} - Saldo de la cuenta {self.cantidad}")  

    def ingresar(self, nueva_cantidad):
        if nueva_cantidad > 0:
           self.cantidad = self.cantidad + nueva_cantidad
        else:
            print("Importe Negativo - No se realiza movimiento")  

    def retirar(self, nueva_cantidad):
        if nueva_cantidad > 0:
            self.cantidad = self.cantidad - nueva_cantidad
            if self.cantidad < 0:
                print("ATENCION - Saldo Negativo!!!")
        else:
            print("Importe Negativo - No se realiza movimiento")          


