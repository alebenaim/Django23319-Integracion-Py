class Persona:
    def __init__(self, nombre = "", edad = 0, dni = ""):
        #nombre - no vacio
        flag = True
        while flag:
            if len(nombre)>0:
                self.__nombre = nombre
                flag=False
            else:
                nombre = input("Ingrese el nombre de la Persona: ") 
        #edad - numero entre 1 y120
        flag = True
        while flag:
            try:
                if edad>0 and edad <=120:
                    self.__edad = edad 
                    flag = False
                else:
                    edad = int(input("Edad incorrecta, reingrese: "))    
            except ValueError:  
                edad = int(input("Edad incorrecta, debe ser un numero, reingrese: "))
        #dni - 8 caracteres numericos 
        flag = True
        while flag:
            if dni.isnumeric() and  len(dni)==8:
                self.__dni = dni
                flag = False
            else:
                dni = input('DNI inválido. Reingrese ')   
 
       
    @property
    def nombre(self):
        return (self.__nombre)
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        flag = True
        while flag:
            if len(nuevo_nombre)>0:
                self.__nombre = nuevo_nombre
                flag=False
            else:
                nuevo_nombre = input("Ingrese el nombre de la Persona: ")    

    @property
    def edad(self):
        return(self.__edad)

    @edad.setter
    def edad(self,nueva_edad):
        flag = True
        while flag:
            try:
                if nueva_edad>0 and nueva_edad <=120:
                    self.__edad = nueva_edad 
                    flag = False
                else:
                    nueva_edad = int(input("Edad incorrecta, reingrese: "))    
            except ValueError:  
                nueva_edad = int(input("Edad incorrecta, debe ser un numero, reingrese: "))  
                     

    @property
    def dni(self):
        return(self.__dni)   
    
    @dni.setter
    def dni(self, nuevo_dni):
        flag = True
        while flag:
            if nuevo_dni.isnumeric() and  len(nuevo_dni)==8:
                self.__dni = nuevo_dni
                flag = False
            else:
                nuevo_dni = input('DNI inválido. Reingrese ')   
                    

    def mostrar(self):
        return(f'Nombre:{self.__nombre} - Edad: {self.__edad} - DNI: {self.__dni}')    
    

    def es_mayor_de_edad(self):
        if type(self.__edad) == int:
            return (self.__edad >= 18)
        else:
            print("Edad invalida")
            return (False)