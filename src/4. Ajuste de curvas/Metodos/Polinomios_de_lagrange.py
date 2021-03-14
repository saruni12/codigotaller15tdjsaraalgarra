#from sympy import *
import sympy as sp



def funcion(expr):
    x = sp.Symbol('x')
    funcion = sp.expand(expr)
    return funcion


def polLagrange(eje_x, eje_y, orden):
    n_datos = orden
    ecuacion = ''

    for i in range(0, n_datos):
        fx = eje_y[i]
        x = eje_x[i]
        # Valorees auxiliares
        divisor = 1
        x_xi = ''
        polinomio = '1'
        # print(x)
        for j in range(0, n_datos):
            if i != j:
                a = x-eje_x[j]
                x_xi = str(f'(x-{eje_x[j]})')
                polinomio = polinomio+'*'+x_xi
            else:
                a = 1
            divisor = divisor*a
            # print(a)
        constante = fx/divisor
        polinomio = polinomio+'*'+str(constante)
        ecuacion = ecuacion+'+'+polinomio
        # print(polinomio)
    expr = str(f'{ecuacion}')
    x = sp.Symbol('x')
    px = funcion(expr)
    return px


def aproxLagrange(eje_x, eje_y, x0,evaluar):
    cant = len(eje_y)
    if cant >4:
        n=4
    else:
        n=cant
    print('\n                 POLINOMIOS DE LAGRANGE\n')
    print('Las ecuaciones de ajuste son:\n')

    for i in range(2, n+1):
        grado = polLagrange(eje_x, eje_y, i)
        print(f'  Orden {i-1}:  y = {grado}\n')
        if evaluar==True:
            x=x0
            y = eval(str(grado))
            print(f'                Para:  x = {x0}   =>   y = {"{0:.4f}".format(y)}\n')


# datos de prueba


""" x = [0, 1, 3, 6]
y = [-3, 0, 5, 7]
x0 = 4 """



""" x = [1, 5, 20, 40]
y = [56.5, 113, 181, 214.5]
x0=2

evaluar=True
aproxLagrange(x, y, x0,evaluar)
 """