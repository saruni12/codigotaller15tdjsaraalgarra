import numpy as np
import sympy as sp
from prettytable import PrettyTable
import math
from math import cos, sin , exp
from sympy import cos, sin , exp


def cambiarValores(dic_var, nuevos_valores, num_ecuaciones, var):
    for i in range(0, num_ecuaciones):
        dic_var[f'{var[i]}'] = nuevos_valores[i]
    return dic_var


def nuevosValores(ecua, Ecuaciones, variables):
    valor_ini = []
    funcs = vars(math)
    for i in range(0, Ecuaciones):
        expr = ecua[i]
        funcion = eval(expr,funcs, variables)
        valor_ini.append(funcion)
    return valor_ini


def efunciones(var, valor, Ecuaciones):
    var_valor = {}
    for i in range(0, Ecuaciones):
        variable = var[i]
        anadir = {f'{variable}': valor[i]}
        var_valor.update(anadir)
    return var_valor


def punto_fijo_multivariable(ecua, var, valor, Ecuaciones, emax, N=50):
    encabezados = []
    encabezados.append("Iteracion")
    for i in var:
        encabezados.append(i)
    encabezados.append(f"Error |{var[0]}(i)-{var[0]}(i-1)|")
    contenido = []
    tabla = PrettyTable(encabezados)
    tabla.title = "METODO DE PUNTO FIJO MULTIVARIABLE"
    evalu_func = efunciones(var, valor, Ecuaciones)
    for k in range(1, N):

        variables = cambiarValores(evalu_func, valor, Ecuaciones, var)
        corregidos = nuevosValores(ecua, Ecuaciones, variables)
        error = abs(valor[0]-corregidos[0])
        valor = corregidos

        contenido = []
        contenido.append(k)
        for i in range(0, Ecuaciones):
            contenido.append("{0:.7f}".format(valor[i]))
        contenido.append("{0:.7f}".format(error))
        # tabla.add_row([k, "{0:.7f}".format(valor[0]), "{0:.7f}".format(
        #    valor[1]), "{0:.7f}".format(error)])
        tabla.add_row(contenido)
        if error < emax or error == 0:
            break
        # print(valor)
    #funcion = eval(expr, {f'{var1}': valor[0],f'{var2}':  valor[1]})
    #w = {f'{var1}': valor[0], f'{var2}':  valor[1]}
    print(tabla)
    print(f'Solucion del sistema:  ')
    for i in range(0, Ecuaciones):
        print(f'                     {var[i]} = {"{0:.4f}".format(valor[i])}')


#ecua = ['(x**2+y**2+8)/10', '(x*y**2+x+8)/10']
#var = ['x', 'y']
#valori = [0.0, 0.0]
#Ecuaciones = 2

#ecua = ['(9-y**2-z**2)**0.5', '1/(x*z)','(x+y)**0.5']
#var = ['x', 'y','z']
#valori = [2.5, 0.2,1.6]
#Ecuaciones = 3


#ecua = ['(0.5+cos(y*z))/3', 'x/(625)**0.5','(-exp(-x*y)-(10*pi-3)/3)/20']
#var = ['x', 'y', 'z']
#valori = [1, 1, 1]
#Ecuaciones = 3

#punto_fijo_multivariable(ecua, var, valori, Ecuaciones, 1e-3, N=50)
