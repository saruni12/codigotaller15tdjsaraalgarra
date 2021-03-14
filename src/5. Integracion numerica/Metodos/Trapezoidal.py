from math import *


def evaluarFuncion(expr, val):
    x = val
    y = eval(expr)
    return y


def mTrapecio(ecuacion, lim_inf, lim_sup, n):
    h = (lim_sup-lim_inf)/n
    fxa=evaluarFuncion(ecuacion,lim_inf)
    fxb=evaluarFuncion(ecuacion,lim_sup)
    sfx = 0
    for k in range(1, n):
        eval_x=lim_inf+h*k
        fxeval=evaluarFuncion(ecuacion,eval_x)
        sfx = sfx+fxeval
    integral = (h/2)*(fxa+2*sfx+fxb)
    print(f'\n      METODO DEL TRAPECIO\n')
    print(f'  Nro. de franjas = {n}\n')
    print(f'        I = {"{0:.7f}".format(integral)}')
    """ cant_datos = len(eje_x)
    fx0 = eje_y[0]
    fxn = eje_y[cant_datos-1]
    sfx = 0
    for i in range(1, cant_datos-1):
        sfx = sfx+eje_y[i]
        # print(eje_y[i])
    integral = (h/2)*(fx0+2*sfx+fxn)
    print(integral)
    return print(h, fx0, fxn, sfx)
 """

""" x=[-1,0,1,2,3,4]
y=[8,10,10,20,76,238] """


""" x0 = 0
x1 = 2
ecuacion = '3*x'
n = 6
x, y = None, None
mTrapecio(ecuacion, x0, x1, n, x, y)
"""

""" x0 = 0
x1 = 1
ecuacion = '(x**0.1)*(1.2-x)*(1-exp(20*(x-1)))'
n = 5005
x, y = None, None
mTrapecio(ecuacion, x0, x1, n) """



""" x0 = -1
x1 = 1
ecuacion = '(1/(2*pi)**0.5)*(exp((-x**2)/2))'
n = 1024
mTrapecio(ecuacion, x0, x1, n)
 """
""" x0 = 2
x1 = 8
ecuacion = '(x**2)*(sin(x))'
n = 10

mTrapecio(ecuacion, x0, x1, n)
 """