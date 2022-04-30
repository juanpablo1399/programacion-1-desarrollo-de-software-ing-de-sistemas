#importamos las otras clases
from array import array
from Comida import Comida
from PacMan import  PacMan
from Mapa   import  Mapa
from Jugador import Jugador
from Puntos  import Puntos
from Fantasma import Fantasma


  
#creamos clase


class partida:

    #atributos
    Comida:array # comidas
    JugadorPartida:Jugador
    Tiempo:float
    Puntaje:Puntos
    PacMan1:PacMan
    Fantasmas:Fantasma
    Mundo:Mapa
    Vida:bool


    #creamos metodos

    def JugarPartida():bool
    def TerminarPartida():bool
    def ComerFantasma(aumentarPuntos:int):int
    def Reaparecer():bool