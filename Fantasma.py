
from ast import If
from inspect import _void
from re import S

class Fantasma:

#atributos
    Situacion:int    
    Seguir=1
    Huir=2
    Reaparecer=3
    # Color:str
    # Movimiento:int
    # creamos inicializador
    
    def __init__(self,Color:str,Movimiento:int):
        self.Color= Color
        self.Movimiento= Movimiento
    
    #metodos 

    def Estado(self)->int:
        pass   




