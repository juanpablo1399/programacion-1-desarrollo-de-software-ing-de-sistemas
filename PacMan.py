#creamos la  clase

from typing_extensions import Self


class PacMan:
    
    #creamos atributos
    
    Color:str
    Tamaño:int
    IncremetoX:int
    IncremetoY:int


# creamos  inicializador 



    def __init__(self, Color:str ,Tamaño:int ,IncremetoX:int ,IncremetoY:int):

            self.Color= Color
            self.Tamaño=Tamaño
            self.IncremetoX=IncremetoX
            self.IncremetoY=IncremetoY

# definimos metodos 

def MovimientoX():int
        
def MovimientoY():int
