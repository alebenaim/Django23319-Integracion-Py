from Persona import Persona
from CuentaJoven import CuentaJoven

if __name__ == "__main__":

#persona1 valido para cuenta joven
    persona1 = Persona("Juanito",20,"55555455")
    print(Persona.mostrar(persona1))
#crea cuenta    
    cuenta1 = CuentaJoven(persona1,4500, 50)
    print(CuentaJoven.mostrar(cuenta1))
#ingreso $1000
    CuentaJoven.ingresar(cuenta1,1000)
    print(CuentaJoven.mostrar(cuenta1))
#ingreso número negativo, no se hace
    CuentaJoven.ingresar(cuenta1,-500)
    print(CuentaJoven.mostrar(cuenta1))
#retiro
    CuentaJoven.retirar(cuenta1,500)
    print(CuentaJoven.mostrar(cuenta1))
#retiro y saldo en rojo    
    CuentaJoven.retirar(cuenta1,5500)
    print(CuentaJoven.mostrar(cuenta1))

#perosona con edad no valida para Cuenta Joven
    persona2 = Persona("Sol",30,"23456789")
    print(Persona.mostrar(persona2))

# crea la cuenta y valida que la edad
    cuenta2 = CuentaJoven(persona2,3600, 20)
    print(CuentaJoven.mostrar(cuenta2))
    if  cuenta2.es_titular_valido(persona2):
        print(CuentaJoven.mostrar(cuenta2))
    else:
        print("El titular no reune los requisitos para acceder a Cuenta Joven")    
   
    
#intento de retiro de cuenta joven por persona fuera del rango de edad
    CuentaJoven.retirar(cuenta2,500)


 