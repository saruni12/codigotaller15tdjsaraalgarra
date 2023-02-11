import numpy as np
from prettytable import PrettyTable
from math import *


def funcion(expr, val):
    x = val
    y = eval(expr)
    return y


def biseccion(expr, xi, xd, emax, N=100):
    tabla = PrettyTable(
        ["Iteracion", "Xi", "Xd", "X", "f(x)", "Error", "%Error"])
    tabla.title = "METODO DE LA BISECCION "
    for k in range(1, N):
        xd_old = xd
        xi_old= xi
        x_medio = (xi+xd)/2
        fx = funcion(expr, x_medio)
        if k == 1:
            error = abs(xd_old-x_medio)
        else:
            error = abs(xm_old-x_medio)
        xm_old = x_medio
        if fx > 0:
            xd = x_medio
        else:
            xi = x_medio
        tabla.add_row([k, "{0:.7f}".format(xi_old), "{0:.7f}".format(
            xd_old), "{0:.7f}".format(x_medio), "{0:.7f}".format(abs(fx)), "{0:.7f}".format(error), "{0:.2f}".format(error*100)])
        if error < emax:
            break
    print(tabla)
    x = "{0:.8f}".format(x_medio)
    print(f'''
        la raiz es: {x}
        ''')
