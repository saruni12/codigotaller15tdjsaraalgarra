import numpy as np
from prettytable import PrettyTable
from math import *

def funcion(expr, val):
    x = val
    y = eval(expr)
    return y

def Muller(expr,x0,x1,x2,emax,N=100):
    tabla = PrettyTable(["Iteracion", "X0","X1","X2", "X","f(x)", "Error"])
    tabla.title = "METODO DE MULLER"
    for k in range(1, 4):
        f0=funcion(expr,x0)
        f1=funcion(expr,x1)
        f2=funcion(expr,x2)
        fx1_fx0=(f1-f0)/(x1-x0)
        fx2_fx1=(f2-f1)/(x2-x1)
        fx2_x1_x0=(fx2_fx1-fx1_fx0)/(x2-x0)
        a2=fx2_x1_x0
        a1=fx2_fx1-(x2+x1)*a2
        a0=f2-x2*(fx2_fx1-x1*a2)
        b=(a1**2-4*a0*a2)**0.5
        denominador1=-a1+b
        denominador2=-a1-b
        if abs(denominador1)>abs(denominador2):
            x3=2*a0/denominador1
        else:
            x3=2*a0/denominador2
        f3=funcion(expr,x3)
        error=abs(x3-x2)
        #print(a2,a1,a0,denominador1,denominador2,x3)
        tabla.add_row([k,"{0:.7f}".format(x0),"{0:.7f}".format(x1),"{0:.7f}".format(x2), "{0:.7f}".format(x3), "{0:.7f}".format(
            f3), "{0:.7f}".format(error)])
        if error < emax or error == 0:
            break
        x0=x1
        x1=x2
        x2=x3
    print(tabla)
    x = "{0:.8f}".format(x3)
    print(f'''
        la raiz es: {x}
        ''')