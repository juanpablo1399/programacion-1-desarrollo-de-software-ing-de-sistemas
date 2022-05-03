#creamos la clase

from typing_extensions import Self


class Puntos:

#definimos atributos 
    PuntoNormal:int
    PuntoEspecial:int
    
    #creamos inicializador 

    def __init__(self,PuntoNormal,PuntoEspecial):
        self.PuntoNormal=PuntoNormal
        self.PuntoEspecial=PuntoEspecial   
    
    def Score(self):
        TotalPunto=0
        TotalPunto=self.PuntoEspecial+self.PuntoNormal
        
        return TotalPunto
        