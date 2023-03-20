from Cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
 
       

    @property
    def bonificacion(self):
        return (self.__bonificacion)
    
    @bonificacion.setter
    def bonificacion(self,nueva_bonificacion):   
        self.__bonificacion=nueva_bonificacion

    def es_titular_valido(self,titular):
        return (titular.edad >= 18 and titular.edad < 25)
    
    def mostrar(self):
        return (f"Titular de la Cuenta Joven {self.titular.mostrar()} - Saldo de la cuenta {self.cantidad} - Bonificacion {self.bonificacion}%")  

    def retirar(self, nueva_cantidad):
        if self.es_titular_valido(self.titular):
           super().retirar(nueva_cantidad)
        else:
            print("El titular no tiene acceso a Cuenta Joven y no puede retirar")              