from Persona import Persona
from Cuenta import Cuenta

if __name__ == "__main__":
    persona1 = Persona("Juanito",20,"55555455")
    print(Persona.mostrar(persona1))
    persona2 = Persona("Sol",20,"23456789")
    print(Persona.mostrar(persona2))

    cuenta1 = Cuenta(persona1,4500)
    print(Cuenta.mostrar(cuenta1))
    cuenta2 = Cuenta(persona2,230.45)
    print(Cuenta.mostrar(cuenta2))

    Cuenta.ingresar(cuenta1,1000)
    print(Cuenta.mostrar(cuenta1))

    Cuenta.ingresar(cuenta1,-500)
    print(Cuenta.mostrar(cuenta1))

    Cuenta.retirar(cuenta1,500)
    print(Cuenta.mostrar(cuenta1))
    Cuenta.retirar(cuenta1,5500)
    print(Cuenta.mostrar(cuenta1))