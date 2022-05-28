from inspect import _void

from Usuario import Usuario


class Administrador(Usuario):


    Cc:int
    Clave:int
    
    def __init__(self,Cc:int,Clave:int):

        self.Cc=Cc
        self.Clave:Clave

    def __init__(self,Id:int,Usuario:str):
        self.Id=Id
        self.Usuario=Usuario


    
    def CantidadPartidas(self):
        
        return("Partidas jugadas en el mes")

    def CantidadHoras(self):
        
        return("Horas de juego al mes ")


    def CantidadJugadores(self):

        return("Cantidad de jugadores en el mes ")



    print  ("MENU\n\n1)-Nuevo\n2-most")

opcion= input("elige una opcion")

if opcion == "1" :
        print ('registro\n')

        archivo = open("AdministradorArchivo.csv","a")

        
        Cc= input("ingrese su cedula:   ")

        clave= input("digite la clave de su maquina:    ")
        


        print ("se guardo correctamente:"   "+ Cedula+","Clave") 
        AdministradorArchivo.write("Cedula","Clave","\n")
else:
    print("elija  una opcion ")




    