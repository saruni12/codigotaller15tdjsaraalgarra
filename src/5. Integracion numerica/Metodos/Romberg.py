from math import *
from prettytable import PrettyTable


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
        else:
            sfx_3 = sfx_3+fxeval
    integral = (3*h/8)*(fxa+3*sfx_3+2*sfx_2+fxb)
    return integral


def mRomberg(ecuacion, lim_inf, lim_sup, puntos):
    n = int(2**puntos)
    limite = puntos
    # puntos=int(n**0.5)
    k = 1
    Ii = []
    I = 0
    u = 1
    # Para elaborar la tabla
    tabla = PrettyTable(["Punto", "Fajas", "I: Simpson 3/8"])
    tabla.title = "METODO DE INTEGRACION DE ROMBERG "
    for i in range(0, limite+1):
        I = mSimpson38(ecuacion, lim_inf, lim_sup, k)
        Ii.append(I)
        tabla.add_row([i, k, "{0:.8f}".format(I)])
        k = k*2
        if k == n*2:
            break
    # Valores iniciales obtenidos por integracion
    #print(Ii)

    u = 1
    Ii_1 = Ii
    new_I = []
    for _ in range(0, n):
        for j in range(0, puntos):
            I_1 = Ii_1[j]
            I_2 = Ii_1[j+1]
            # print(Ii[j])
            Ik = ((4**u)*I_2-I_1)/(4**u-1)
            new_I.append(Ik)
            #print(j+1,I_1,I_2, Ik)
        u += 1
        Ii_1 = new_I
        new_I = []
        puntos -= 1
        # Para visualizar integracion de romberg en cada iteracion
        # print(Ii_1)
        if len(Ii_1) == 1:
            break
    solucion = Ii_1[0]
    print(tabla)
    print(f'           I = {"{0:.8f}".format(solucion)}')


""" x0 = 0
x1 = 1
ecuacion = 'sin(pi*x)'
puntos = 4

mRomberg(ecuacion, x0, x1, puntos) """


""" x0 = -1
x1 = 1
ecuacion = '(1/(2*pi)**0.5)*(exp((-x**2)/2))'
puntos = 5
mRomberg(ecuacion, x0, x1, puntos) """

""" x0 = 0
x1 = 1
ecuacion = '(x**0.1)*(1.2-x)*(1-exp(20*(x-1)))'
puntos = 12
mRomberg(ecuacion, x0, x1, puntos) """
