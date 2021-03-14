from math import *


def evaluarFuncion(expr, val):
    x = val
    y = eval(expr)
    return y


def mSimpson13(ecuacion, lim_inf, lim_sup, n):
    if n % 2 != 0:
        n = n+1
    h = (lim_sup-lim_inf)/n
    fxa = evaluarFuncion(ecuacion, lim_inf)
    fxb = evaluarFuncion(ecuacion, lim_sup)
    sumfx_par = 0
    sumfx_impar = 0
    for k in range(1, n):
        eval_x = lim_inf+h*k
        fxeval = evaluarFuncion(ecuacion, eval_x)
        if k % 2 == 0:
            sumfx_par = sumfx_par+fxeval
        else:
            sumfx_impar = sumfx_impar+fxeval
    integral = (h/3)*(fxa+4*sumfx_impar+2*sumfx_par+fxb)
    print(f'\n      METODO DEL SIMPSON 1/3 \n')
    print(f'  Nro. de franjas = {n}\n')
    print(f'        I = {"{0:.7f}".format(integral)}')


""" x0 = -1
x1 = 1
ecuacion = '(1/(2*pi)**0.5)*(exp((-x**2)/2))'
n = 3

mSimpson13(ecuacion, x0, x1, n) """


""" x0 = 1
x1 = 2
ecuacion = '1/x'
n = 10
mSimpson13(ecuacion, x0, x1, n) """

""" x0 = 0
x1 = 1
ecuacion = '(x**0.1)*(1.2-x)*(1-exp(20*(x-1)))'
n = 2000
mSimpson13(ecuacion, x0, x1, n) """

""" x0 = 2
x1 = 8
ecuacion = '(x**2)*(sin(x))'
n = 50
mSimpson13(ecuacion, x0, x1, n) """

""" x0 = 1
x1 = 3
ecuacion = 'x*(exp(exp(x)))'
n = 5000
mSimpson13(ecuacion, x0, x1, n) """
