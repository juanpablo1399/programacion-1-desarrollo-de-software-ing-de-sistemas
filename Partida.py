#importamos las otras clases
from array import array
from ast import Str
from ctypes.wintypes import FLOAT
from webbrowser import get
from Comida import Comida
from PacMan import  PacMan
from Mapa   import  Mapa
from Jugador import Jugador
from Puntos  import Puntos
from Fantasma import Fantasma



#creamos la  clase


from array import ArrayType


class partida:

    #atributos
    Comida: ArrayType("Comida")  
    # JugadorPartida:Jugador
    # Tiempo:float
    # Puntaje:Puntos
    # PacMan:PacMan
    Fantasma:ArrayType("Fantasma")
    # Mundo:Mapa
    #Vida:bool


    #creamos inicializador 

    def __init__(self, JugadorPartida:Jugador , 
    Tiempo:float,Puntaje:Puntos, Mundo:Mapa, Vida:bool ):
    
        def GetJugadorPartida(self):
            return self.JugadorPartida
    
    def SetJugadorPartida(self,JugadorPartida):
        self.JugadorPartida = JugadorPartida


        #compocision
        self.PacMan=PacMan("Color:str ,Tamaño:int ,IncremetoX:int ,IncremetoY:int")

        self.Comida=Comida("Cereza:int, Basica:int, Dots: int")
        
        self.Jugador=Jugador("NombreUsuario:str")
        
        self.Mapa=Mapa('Paredes:ArrayType("Fantasma"),PosicionMapax:int,PosicionMapay:int')
        
        self.Fantasma=Fantasma("Color:str,Movimiento:int")
        
        
        
        
        #Metodos

    def JugarPartida(self):
    
        return("Iniciar partida")
    
    def TerminarPartida(self):

        return("Finalizar partida")
    
    def Reaparecer(self):
        
        return("desea reaparecer ")





print  ("MENU\n\n1)-Nuevo\n2-most")




print ('registro\n')
archivo = open("PartidaArchivo.csv","a")

        
JugadorPartida = input("masterchief:")

Tiempojuego = input("ha jugado 7 minutos :")
        
        
Puntosjuego = input("su puntaje es 500 ")
        
PartidaArchivo.write(NicName,Contraseña)

PartidaArchivo.close()

print ("se guardo correctamente:" ,Tiempojuego,Puntosjuego   ) 






    
