from prettytable import PrettyTable
from math import *


def funcion(expr, x_eval, y_eval):
    x = x_eval
    y = y_eval
    funcion = eval(expr)
    return funcion


def mEulerm(ecuacion, x0, x1, y0, n):
    n = int(n)
    h = (x1-x0)/n
    x = x0
    y = y0
    # Armado de la tabla
    enc_y = f'y({x1})'
    tabla = PrettyTable(["Iteracion", "xi", "yi", "y(i+1)", "fxy prom", enc_y])
    tabla.title = "METODO DE EULER MODIFICADO"
    for i in range(0, n):
        fxy = funcion(ecuacion, x, y)

        y_cal = y + h*fxy
        fxiyi = funcion(ecuacion, x+h, y_cal)
        yi_1 = (1/2)*(fxy+fxiyi)
        y_new = y+h*yi_1
        if i < 10:
            tabla.add_row(
                [i+1, "{0:.6f}".format(x), "{0:.6f}".format(y), "{0:.6f}".format(y_cal), "{0:.6f}".format(yi_1), "{0:.6f}".format(y_new)])
        x = x+h
        y = y_new
        # print(y_cal)
    if n > 10:
        tabla.add_row(['.', '.', '.', '.','.','.'])
        tabla.add_row([n, "{0:.6f}".format(
            x), "{0:.6f}".format(y), "{0:.6f}".format(y_cal), "{0:.6f}".format(yi_1), "{0:.6f}".format(y_new)])
    print("\n")
    print(tabla)
    print(f'                      y({x1}) = {"{0:.8f}".format(y_new)}')


# datos de ejemplo
""" x0 = 0
x1 = 1
y = 2
ecuacion = 'x-y'
n = 100
mEulerm(ecuacion, x0, x1, y, n) """
