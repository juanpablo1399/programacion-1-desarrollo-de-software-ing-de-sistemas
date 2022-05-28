from Usuario import Usuario

class Jugador(Usuario):

    #atributos
    # NickName:str
    #Contraseña

    # inicializador 

    def __init__(self,NickName:str,Contraseña:str):
        self.NickName= NickName
        self.Contraseña=Contraseña
    
    def __init__(self,Id:int,NombreUsuario:str):
        self.Id=Id
        self.NombreUsuario=NombreUsuario

        self.NickName
        self.Contraseña



#metodos
    def PuntosJugador(cantidadPuntos:str):str



print  ("MENU\n\n1)-Nuevo\n2-most")

opcion= input("elige una opcion")

if opcion == "1" :
        print ('registro\n')

        archivo = open("JugadorArchivo.csv","a")

        NickName = input("ingrese el NickName:   ")
        Contraseña = input("digite su contraseña:    ")


        print ("se guardo correctamente:"   "+ NickName+","Contraseña")

        JugadorArchivo.write("NicName","Contraseña","\n")
else:
    print("elija  una opcion ")
