import Metodo.elim_de_gauss
from numpy import *


A = matrix([[4, -9, 2], [2, -4, 6], [1, -1, 3]])
B = matrix([[5], [3], [4]])
Metodo.elim_de_gauss.metodo_gauss(A, B)
Metodo.elim_de_gauss.solucion(A,B)