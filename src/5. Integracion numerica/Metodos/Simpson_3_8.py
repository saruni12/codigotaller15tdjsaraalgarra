from math import *


def evaluarFuncion(expr, val):
    x = val
    y = eval(expr)
    return y


def mSimpson38(ecuacion, lim_inf, lim_sup, n):
    h = (lim_sup-lim_inf)/(3*n)
    fxa = evaluarFuncion(ecuacion, lim_inf)
    fxb = evaluarFuncion(ecuacion, lim_sup)
    nn = 3*n
    sfx_3 = 0
    sfx_2 = 0
    for k in range(1, nn):
        eval_x = lim_inf+h*k
        fxeval = evaluarFuncion(ecuacion, eval_x)
        if k % 3 == 0:
            sfx_2 = sfx_2+fxeval
            #u='2'
        else:
            sfx_3 = sfx_3+fxeval
            #u='3'
        #print(f'{u}  k={k}    x={eval_x}  fx={fxeval}')
    integral = (3*h/8)*(fxa+3*sfx_3+2*sfx_2+fxb)
    print(f'\n      METODO DEL SIMPSON 3/8\n')
    print(f'  Nro. de franjas = {n}\n')
    print(f'        I = {"{0:.7f}".format(integral)}')



""" x0 = -1
x1 = 1
ecuacion = '(1/(2*pi)**0.5)*(exp((-x**2)/2))'
n = 10

mSimpson38(ecuacion, x0, x1, n)
 """
""" x0 = 1
x1 = 2
ecuacion = '1/x'
n = 6
mSimpson38(ecuacion, x0, x1, n) """

""" x0 = 2
x1 = 8
ecuacion = '(x**2)*(sin(x))'
n = 15
mSimpson38(ecuacion, x0, x1, n) """


""" x0 = 0
x1 = 1
ecuacion = '(x**0.1)*(1.2-x)*(1-exp(20*(x-1)))'
n = 1000
mSimpson38(ecuacion, x0, x1, n) """
