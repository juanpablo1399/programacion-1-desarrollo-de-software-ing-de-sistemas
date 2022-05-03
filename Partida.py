#importamos las otras clases
from array import array
from ast import Str
from ctypes.wintypes import FLOAT
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
    # PacMan1:PacMan
    Fantasma:ArrayType("Fantasma")
    # Mundo:Mapa
    # Vida:bool


    #creamos inicializador 

    def __init__(self,Comida: ArrayType("Comida"), JugadorPartida:Jugador , 
    Tiempo:float,Puntaje:Puntos, Fantasma:ArrayType("Fantasma"), Mundo:Mapa, Vida:bool ):
    



        #compocision
        self.PacMan=PacMan("Color:str ,Tamaño:int ,IncremetoX:int ,IncremetoY:int")

        self.Comida=Comida("Cereza:int, Basica:int, Dots: int")
        
        self.Jugador=Jugador("NombreUsuario:str")
        
        self.Mapa=Mapa('Paredes:ArrayType("Fantasma"),PosicionMapax:int,PosicionMapay:int')
        
        self.Fantasma=Fantasma("Color:str,Movimiento:int")
        
        
        
        
        
        
        
        #Metodos
        
        def JugarPartida():str

        def TerminarPartida():str
        
        def Reaparecer():str
