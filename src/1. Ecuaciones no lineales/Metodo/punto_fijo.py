import numpy as np
from prettytable import PrettyTable
from math import *


def funcion(expr, val):
    x = val
    y = eval(expr)
    return y


def punto_fijo(expr, x0, emax, N=50):
    tabla = PrettyTable(["Iteracion", "Xi", "Error", "f(x)", "%Error"])
    tabla.title = "METODO DE PUNTO FIJO "
    for k in range(1, N):
        xi = funcion(expr,x0)
        error=abs(xi-x0)
        e_porc = abs(error/xi)
        x0=xi
        fx=funcion(expr,xi)
        tabla.add_row([k, "{0:.7f}".format(xi), "{0:.7f}".format(
            error), "{0:.7f}".format(fx), "{0:.2f}".format(e_porc*100)])
        if error < emax or error>10:
            break
    print(tabla)
    x = "{0:.8f}".format(xi)
    print(f'''
        la raiz es: {x}
        ''')