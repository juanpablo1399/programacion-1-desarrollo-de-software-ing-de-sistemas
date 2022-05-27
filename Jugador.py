from inspect import _void

from Usuario import Usuario


class Jugador(Usuario):

    #atributos
    # NickName:str
    #Contraseña

    # inicializador 

    def __init__(self,NickName:str,Contraseña:str):
        self.NickName= NickName
        self.Contraseña=Contraseña



#metodos
    def PuntosJugador(cantidadPuntos:str):str