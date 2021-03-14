import numpy as np
from prettytable import PrettyTable
from math import *


def funcion(expr, val):
    x = val
    y = eval(expr)
    return y


def falsa_Posicion(expr, xi, xd, emax, N=100):
    tabla = PrettyTable(
        ["Iteracion", "Xi", "Xd", "X", "f(x)", "Error", "%Error"])
    tabla.title = "METODO DE LA FALSA POSICION "
    for k in range(1, N):
        xi_old = xi
        xd_old = xd
        fxi = funcion(expr, xi)
        fxd = funcion(expr, xd)
        xm = xd-(xd-xi)*fxd/(fxd-fxi)
        fxm = funcion(expr, xm)
        if k == 1:
            error = abs(xd-xm)
        else:
            error = abs(xm_old-xm)
        xm_old = xm
        if fxm < 0:
            xi = xm
        else:
            xd = xm
        tabla.add_row([k, "{0:.7f}".format(xi_old), "{0:.7f}".format(
            xd_old), "{0:.7f}".format(xm), "{0:.7f}".format(abs(fxm)), "{0:.7f}".format(error), "{0:.2f}".format(error*100)])
        if error < emax:
            break
    print(tabla)
    xm = "{0:.8f}".format(xm)
    print(f'''
        la raiz es: {xm}
        ''')
