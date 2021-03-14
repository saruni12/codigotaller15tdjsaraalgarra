from math import *
import sympy as sp
from scipy.misc import derivative
from prettytable import PrettyTable


def funcion(expr, x_eval, y_eval):
    x = x_eval
    y = y_eval
    funcion = eval(expr)
    return funcion


def derivar(ecuacion):

    x = sp.Symbol('x')
    y = sp.Symbol('y')
    derv_x = str(sp.Derivative(ecuacion, x, evaluate=True))
    derv_y = str(sp.Derivative(ecuacion, y, evaluate=True))

    return derv_x, derv_y

def mTaylor(ecuacion, x0, x1, y0, n):
    n = int(n)
    h = (x1-x0)/n
    x = x0
    y = y0
    dfdx, dfdy = derivar(ecuacion)
    dfxy_literal = dfdx+'+'+dfdy+'*('+ecuacion+')'
    # constructor tabla
    enc_y = f'y{x1}'
    tabla = PrettyTable(["Iteracion", "xi", "yi", enc_y])
    tabla.title = "METODO DE TAYLOR DE SEGUNDO ORDEN "
    for i in range(0, n):
        fxy = funcion(ecuacion, x, y)
        dfxy = funcion(dfxy_literal, x, y)
        y_cal = y+h*fxy+((h**2)/2)*dfxy
        if i < 10:
            tabla.add_row(
                [i+1, "{0:.4f}".format(x), "{0:.6f}".format(y), "{0:.6f}".format(y_cal)])
        x = x+h
        y = y_cal
        # print(y_cal)
    # print(fxy,dfxy)
    print("\n")
    print(tabla)
    print(f'             y({x1}) = {"{0:.8f}".format(y_cal)}')


# datos de ejemplo
""" x0 = 0
x1 = 1
y = 2
ecuacion = 'x-y'
n = 100
mTaylor(ecuacion, x0, x1, y, n) """

""" x0 = 0
x1 = 1
y = 1
ecuacion = 'cos(x*y)'
n = 5
mTaylor(ecuacion, x0, x1, y, n) """


""" x0 = 0
x1 = 1
y = 1
ecuacion = 'x+y'
n = 10
mTaylor(ecuacion, x0, x1, y, n) """
