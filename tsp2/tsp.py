"""
TSP
"""


class Mundo:
   def __init__(self,lugares):
      self. lugares=[]
      with open(lugares,'r') as lugares:
         posicion = lugares.read()
         self.lugares.append(Lugar(**lugar))

      
   pass

class Lugar:
   def_ init__(self,x,y):
      self.x = x
      self.y = y
   def __repr(Self):
      return f"Posición: ({self.x},{self.y})"

class Optimizador:
   def optimizar_ruta(self):
      mundo = Mundo()
      algoritmo = Algoritmo()
      ruta = algoritmo.ejecutar()
      return ruta 



class Ruta: 
   def __init__ (self):
      self.lugares=[]
   
   @property
   def costo(self):
      return 0.0

   def __repr__(self):
   return f"Ruta : {self.lugares} (Costo: {self.costo})"

	
