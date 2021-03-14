import numpy as np
import sympy as sp
import math
from scipy.misc import derivative
from prettytable import PrettyTable
from math import *

from sympy.core.numbers import I


def derivar(ecuaciones, variables, num_ecuaciones):
    derivadas = []
    der_resp = []
    for var_respect in variables:
        var = sp.Symbol(f'{var_respect}')
        for i in range(0, num_ecuaciones):
            primera_derivada = sp.Derivative(ecuaciones[i], var, evaluate=True)
            der_resp.append(str(primera_derivada))
        derivadas.append(der_resp)
        der_resp = []
    return derivadas


def nuevosValores(ecua, Ecuaciones, variables,var):
    valor_ini = []
    funcs = vars(math)
    for i in range(0, Ecuaciones):
        expr = ecua[i]
        funcion = eval(expr,funcs, variables)
        valor_ini.append(funcion)
        variables[f'{var[i]}']=funcion
    return valor_ini


def cambiarValores(dic_var, nuevos_valores,num_ecuaciones,var ):
    for i in range (0,num_ecuaciones):
        dic_var[f'{var[i]}']=nuevos_valores[i]
    return dic_var


def efunciones(var, valor, Ecuaciones):
    var_valor = {}
    for i in range(0, Ecuaciones):
        variable = var[i]
        anadir = {f'{variable}': valor[i]}
        var_valor.update(anadir)
    return var_valor


def pfijo_des(ecua, var, valor, Ecuaciones, emax, N=50):
    # constructor de la tabla
    encabezados = []
    contenido = []
    encabezados.append("Iteracion")
    for i in var:
        encabezados.append(i)
    encabezados.append(f"Error |{var[0]}(i)-{var[0]}(i-1)|")
    tabla = PrettyTable(encabezados)
    tabla.title = "METODO DE PUNTO FIJO MULTIVARIABLE CON DESPLAZAMIENTOS"
    # derivadas de las ecuaciones
    #derivadas = derivar(ecua, var, Ecuaciones)
    #u = derivadas[0][1]
    #for i in derivadas:
        #eval_deriv = nuevosValores(i, Ecuaciones, evalu_func)
    evalu_func = efunciones(var, valor, Ecuaciones)
    for k in range(1, N):
        #print(valor)
        variables = cambiarValores(evalu_func, valor, Ecuaciones,var)
        #variables = efunciones(var, valor, Ecuaciones)
        corregidos = nuevosValores(ecua, Ecuaciones, variables,var)
        error = abs(valor[0]-corregidos[0])
        valor = corregidos
        #anadir a la tabla
        contenido = []
        contenido.append(k)
        for i in range(0, Ecuaciones):
            contenido.append("{0:.7f}".format(valor[i]))
        contenido.append("{0:.7f}".format(error))
        tabla.add_row(contenido)
        if error < emax or error == 0:
            break
    #funcion = eval(expr, {f'{var1}': valor[0],f'{var2}':  valor[1]})
    #w = {f'{var1}': valor[0], f'{var2}':  valor[1]}
    print(tabla)
    print(f'Solucion del sistema:  ')
    for i in range (0,Ecuaciones):
        print(f'                     {var[i]} = {"{0:.5f}".format(valor[i])}')



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
#pfijo_des(ecua, var, valori, Ecuaciones, 1e-5, N=50)
