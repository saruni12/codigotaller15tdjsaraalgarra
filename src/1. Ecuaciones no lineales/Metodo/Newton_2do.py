import numpy as np
import sympy as sp
import math
from math import *
#import scipy.optimize as optimize
from scipy.misc import derivative
from prettytable import PrettyTable


def derivar(expr,orden):
    x = sp.Symbol('x')
    primera_derivada = sp.Derivative(expr, x, evaluate=True)
    if orden==1:
        return primera_derivada
    elif orden==2:
        segunda_derivada = sp.Derivative(primera_derivada, evaluate=True)
        return segunda_derivada

def funcion(expr, val):
    x = val
    y = eval(expr)
    return y

def Newton_R2do_orden(expr, x0, emax, N=100):
    tabla = PrettyTable(["Iteracion", "Xi", "Xi+1","f(x)", "%Error"])
    tabla.title = "METODO DE NEWTON RAPHSON DE 2DO ORDEN "
    primera_derivada=derivar(expr,1)
    segunda_derivada=derivar(expr,2)

    for k in range(1, N):
        fx = funcion(expr, x0)
        dfx_dx1 = funcion(str(primera_derivada), x0)
        dfx_dx2 = funcion(str(segunda_derivada), x0)
        x0_new = x0-2*fx*dfx_dx1/(2*(dfx_dx1)**2-fx*dfx_dx2)
        # analisis de errores
        error = funcion(expr, x0_new)
        # el pretitable
        tabla.add_row([k,"{0:.7f}".format(x0), "{0:.7f}".format(x0_new), "{0:.7f}".format(
            error), "{0:.2f}".format(abs(error*100))])
        # print(k,x0,error,function(expr,x0),e_porc*100)
        x0 = x0_new
        if abs(error) < emax or error == 0:
            break
    print(tabla)
    x = "{0:.8f}".format(x0)
    print(f'''
        la raiz es: {x}
        ''')
    #print(der,der2,uuu)