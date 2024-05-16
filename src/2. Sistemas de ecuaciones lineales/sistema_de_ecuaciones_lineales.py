import Metodo.elim_de_gauss
from numpy import *

#datos de prueba
A = matrix([[1,2,-1,3],[2,0,2,-1],[-1,1,1,-1],[3,3,-1,2]])
B = matrix([[-8],[13],[8],[-1]])
Metodo.elim_de_gauss.metodo_gauss(A, B)
Metodo.elim_de_gauss.solucion(A,B)


#otro ejemplo (seleccionar codigo y presionar "Shift+Alt+A")

""" A = matrix([[4,-2,-1,1,2],[1,2,2,-1,4],[2,-1,4,-2,2],[1,1,1,1,1],[6,4,1,-6,6]])
B = matrix([[14],[14],[-8],[23],[-4]])
Metodo.elim_de_gauss.metodo_gauss(A, B)
Metodo.elim_de_gauss.solucion(A,B) """

"holisss"