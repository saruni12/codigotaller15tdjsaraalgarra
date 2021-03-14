import numpy as np
from prettytable import PrettyTable
from math import *

def funcion(expr, val):
    x = val
    y = eval(expr)
    return y


def secante_x(expr, x0, x1, emax, N=100):

    tabla = PrettyTable(["Iteracion", "Xi", "Error", "f(x)", "%Error"])
    tabla.title = "METODO DE LA SECANTE "
    for k in range(1, N):
        fx0 = funcion(expr, x0)
        fx1 = funcion(expr, x1)
        x = x1-(x1-x0)*fx1/(fx1-fx0)
        #emax=emax*0.1
        error = abs(x1-x)
        e_porc = abs(error/x)
        x0 = x1
        x1 = x
        fx = funcion(expr, x)
        tabla.add_row([k, "{0:.7f}".format(x), "{0:.7f}".format(
            error), "{0:.7f}".format(fx), "{0:.2f}".format(e_porc*100)])
        if error < emax:
            break
    print(tabla)
    x = "{0:.8f}".format(x)
    print(f'''
        la raiz es: {x}
        ''')