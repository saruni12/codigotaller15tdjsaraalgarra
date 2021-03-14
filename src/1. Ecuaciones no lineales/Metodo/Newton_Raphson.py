import numpy as np
import sympy as sp
#from numpy import log as ln
import math
from math import *
#import scipy.optimize as optimize
from scipy.misc import derivative
from prettytable import PrettyTable




def funcion(expr, val):
    x = val
    y = eval(expr)
    return y


def derivada(expr, x0):
    # funcion derivada
    x = sp.Symbol('x')
    f_prime = sp.Derivative(expr, x)
    derivada_de_la_funcion = f_prime.doit().subs(x, x0)
    return derivada_de_la_funcion


def Newton_R(expr, x0, emax, N=100):
    tabla = PrettyTable(["Iteracion", "Xi", "error", "f(x)", "%Error"])
    tabla.title = "METODO DE NEWTON RAPHSON "
    #emax = emax*0.1
    for k in range(1, N):
        xold = x0
        # funcion sustituida
        fx = funcion(expr, x0)
        df_dx = derivada(expr, x0)
        x0 = x0-fx/df_dx
        #analisis de errores
        e_porc = abs((x0-xold)/x0)
        error = abs(xold-x0)
        fx = funcion(expr, x0)
        # el pretitable
        tabla.add_row([k, "{0:.7f}".format(x0), "{0:.7f}".format(
            error), "{0:.7f}".format(fx), "{0:.2f}".format(e_porc*100)])
        # print(k,x0,error,function(expr,x0),e_porc*100)
        if error < emax:
            break
    print(tabla)
    x = "{0:.8f}".format(x0)
    print(f'''
        la raiz es: {x}
        ''')

#Newton_Rhapson(expr, valor_inicial, 1e-3)


# para obtener la raiz por medio optimize de scipy se da la funcion definida
#print(f"La raiz es: {optimize.newton(f,1)}")
