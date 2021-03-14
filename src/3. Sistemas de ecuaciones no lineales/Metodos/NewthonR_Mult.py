import numpy as np
import sympy as sp
from scipy.misc import derivative
from prettytable import PrettyTable
import math
from math import *


def nuevosValores(ecua, Ecuaciones, variables, signo):
    valor_ini = []
    funcs = vars(math)
    for i in range(0, Ecuaciones):
        expr = ecua[i]
        funcion = eval(expr, funcs, variables)
        if signo == 1:
            funcion = -funcion
        elif signo == 2:
            funcion = funcion
        valor_ini.append(funcion)
        # variables[f'{var[i]}']=funcion
    return valor_ini


def cambiarValores(dic_var, nuevos_valores, num_ecuaciones, var):
    for i in range(0, num_ecuaciones):
        dic_var[f'{var[i]}'] = nuevos_valores[i]
    return dic_var


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


def efunciones(var, valor, Ecuaciones):
    var_valor = {}
    for i in range(0, Ecuaciones):
        variable = var[i]
        anadir = {f'{variable}': valor[i]}
        var_valor.update(anadir)
    return var_valor


def newtonR_multivariable(ecua, var, valor, Ecuaciones, emax, N=50):
    # constructor de la tabla
    encabezados = []
    contenido = []
    encabezados.append("Iteracion")
    for i in var:
        encabezados.append(f'D{i}')
        encabezados.append(i)
    encabezados.append(f"Error |Max(Correccion)|")
    tabla = PrettyTable(encabezados)
    tabla.title = "METODO DE NEWTON RHAPSON MULTIVARIABLE"
    # Valores iniciales
    dicc_valores = efunciones(var, valor, Ecuaciones)
    # derivadas de las ecuaciones
    derivadas = derivar(ecua, var, Ecuaciones)

    #u = derivadas[0][1]

    for k in range(1, N):
        variables = cambiarValores(dicc_valores, valor, Ecuaciones, var)
        derivadas_numericas = []
        eval_funciones = nuevosValores(ecua, Ecuaciones, variables, 1)
        for i in derivadas:
            eval_deriv = nuevosValores(i, Ecuaciones, variables, 2)
            derivadas_numericas.append(eval_deriv)
        # Solucion del sistema de ecuaciones
        inv_derivadas = np.linalg.inv(derivadas_numericas)
        Correccion = inv_derivadas.T.dot(eval_funciones)
        # error
        ea = abs(max(Correccion))
        eb = abs(min(Correccion))
        if ea > eb:
            error = ea
        elif eb >= ea:
            error = eb
        for j in range(0, Ecuaciones):
            valor[j] = valor[j]+Correccion[j]
        if error < emax or error == 0:
            break
        # anadir a la tabla
        contenido = []
        contenido.append(k)
        for i in range(0, Ecuaciones):
            contenido.append("{0:.7f}".format(Correccion[i]))
            contenido.append("{0:.7f}".format(valor[i]))
        contenido.append("{0:.7f}".format(error))
        tabla.add_row(contenido)
        
    # Constructor de la tabla de las derivadas parciales

    deriv_por_func = np.array(derivadas).T
    derivadas_p = PrettyTable()
    derivadas_p.title="Derivadas parciales"
    der_res = []
    der_res.append('funcion')
    for j in range(0, Ecuaciones):
        der_res.append(f'dfi/d{var[j]}')
        #derivadas_p.add_row(['k'])
        fila=np.append(j,deriv_por_func [j])
        derivadas_p.add_row(fila)
    derivadas_p.field_names = der_res
    #derivadas_p.add_column=("hola",[1,2])
    print("")
    print(derivadas_p)
    print(tabla)
    print(f'Solucion del sistema:  ')
    for i in range(0, Ecuaciones):
        print(f'                     {var[i]} = {"{0:.4f}".format(valor[i])}')



""" ecua = ['x**2-10*x+y**2+8', 'x*y**2+x-10*y+8']
var = ['x', 'y']
valori = [0.0, 0.0]
Ecuaciones = 2 """

#ecua = ['x**2+y**2+z**2-9', 'x*y*z-1', 'x+y-z**2']
#var = ['x', 'y', 'z']
#valori = [2.5, 0.2, 1.6]
#Ecuaciones = 3

#ecua = ['3*x-cos(y*z)-0.5', 'x**2-625*y**2', 'exp(-x*y)+20*z+(10*pi-3)/3']
#var = ['x', 'y', 'z']
#valori = [1, 0.2, 1]
#Ecuaciones = 3

""" #si converge
ecua = ['x**2-625*y**2', '3*x-cos(y*z)-0.5', 'exp(-x*y)+20*z+(10*pi-3)/3']
var = ['x', 'y', 'z']
valori = [1, 1, 1]
Ecuaciones = 3 """

ecua = ['exp(-x*y)+20*z+(10*pi-3)/3','x**2-625*y**2', '3*x-cos(y*z)-0.5', ]
var = ['x', 'y', 'z']
valori = [1, 1, 1]
Ecuaciones = 3


newtonR_multivariable(ecua, var, valori, Ecuaciones, 1e-5)