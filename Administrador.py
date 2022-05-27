from inspect import _void

from Usuario import Usuario


class Administrador(Usuario):


    Cc:int
    
    def __init__(self,Cc:int):

        self.Cc=Cc

    def __init__(self,Id:int,NombreUsuario:str):
        self.Id=Id
        self.NombreUsuario=NombreUsuario


    
    def CantidadPartidas(self):_void

    def CantidadHoras(self):_void
    
    def CantidadJugadores(self):_void
