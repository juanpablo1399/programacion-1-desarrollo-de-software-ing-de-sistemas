from inspect import _void


class Usuario(object):
    "Clase que representa una persona."
    
    def __init__(self, Id, Nombre, Apellido):
        "Constructor de Persona"
    
        self.Id = Id
    
        self.Nombre = Nombre
    
        self.Apellido = Apellido
    
    
    def __str__(self):
        return " %s: %s, %s"


    print  ("MENU\n\n1)-Nuevo\n2-most")

opcion= input("elige una opcion")

if opcion == "1" :
        print ('registro\n')

        archivo = open("UsuarioArchivo.csv","a")

        Id= input("ingrese el Id:   ")

        Nombre = input("digite su Nombre:    ")

        Apellido = input("digite su Apellido:    ")


        print ("se guardo correctamente:"   "+ Nombre +","+ Apellido +","+ Contraseña + ") 

        UsuarioArchivo.write("Id","Nombre","Apellido","\n")
        
else:
    print("elija  una opcion ")
 

