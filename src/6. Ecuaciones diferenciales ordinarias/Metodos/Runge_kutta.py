from prettytable import PrettyTable
from math import *


def funcion(expr, x_eval, y_eval):
    x = x_eval
    y = y_eval
    funcion = eval(expr)
    return funcion


def mRungeK4orden(ecuacion, x0, x1, y0, n):
    n = int(n)
    h = (x1-x0)/n
    x = x0
    y = y0
    # Armado de la tabla
    enc_y = f'y sol'
    tabla = PrettyTable(
        ["Iteracion", "xi", "yi", "k1", "k2", "k3", "k4", enc_y])
    tabla.title = "METODO DE RUNGE KUTTA DE 4to ORDEN "
    for i in range(0, n):
        k1 = funcion(ecuacion, x, y)
        k2 = funcion(ecuacion, x+h/2, y+h*k1/2)
        k3 = funcion(ecuacion, x+h/2, y+h*k2/2)
        k4 = funcion(ecuacion, x+h, y+h*k3)
        y_cal = y + (h/6)*(k1+2*k2+2*k3+k4)
        tabla.add_row(
                [i+1, "{0:.4f}".format(x), "{0:.6f}".format(y), "{0:.6f}".format(k1), "{0:.6f}".format(k2), "{0:.6f}".format(k3), "{0:.6f}".format(k4), "{0:.6f}".format(y_cal)])
        x = x+h
        y = y_cal
        # print(k1,k2,k3,k4,y_cal)
    print("\n")
    print(tabla)
    print(f'                        y({x1}) = {"{0:.9f}".format(y_cal)}')


# datos de ejemplo
""" x0 = 0
x1 = 1
y = 2
ecuacion = 'x-y'
n = 5
mRungeK4orden(ecuacion, x0, x1, y, n) """


""" x0 = 0
x1 = 0.5
y = 4
ecuacion = '(y+1)*(x+1)*cos(x**2+2*x)'
n = 5
mRungeK4orden(ecuacion, x0, x1, y, n) """