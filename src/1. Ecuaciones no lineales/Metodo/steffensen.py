import numpy as np
from prettytable import PrettyTable
from math import *


def funcion(expr, val):
    x = val
    y = eval(expr)
    return y


def Steffensen(expr, x0, emax, N=100):
    tabla = PrettyTable(["Iteracion", "X0", "X1", "X2",
                         "X", "Error", "%Error"])
    tabla.title = "METODO DE STEFFENSEN "
    for k in range(1, 6):
        x0_old = x0
        x1 = funcion(expr, x0)
        x2 = funcion(expr, x1)
        x_new = x0-((x1-x0)**2)/(x2-2*x1+x0)
        error = abs(x2-x_new)
        x0 = x_new
        tabla.add_row([k, "{0:.7f}".format(x0_old), "{0:.7f}".format(x1), "{0:.7f}".format(x2), "{0:.7f}".format(x_new), "{0:.7f}".format(
            error), "{0:.2f}".format(error*100)])
        if error < emax or error == 0:
            break
    print(tabla)
    x = "{0:.8f}".format(x_new)
    print(f'''
        la raiz es: {x}
        ''')
