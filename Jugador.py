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

opcion= rawinput("elige una opcion")

if opcion == "1" :
        print ('registro\n')

        archivo = open("JugadorArchivo.csv","a")

        NickName = raw_input("ingrese el NickName:   ")
        Contraseña = raw_input("digite su contraseña:    ")


        print ("se guardo correctamente:"   "+ NickName+","Contraseña") 
else:
    print("elija  una opcion ")
