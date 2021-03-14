import numpy as np
import sympy as sp
from scipy.misc import derivative
from prettytable import PrettyTable
import math
from math import *


def nuevosValoresa(ecua, derivadas, Ecuaciones, variables,var):
    valor_ini = []
    func_numerica = []
    derv_numerica = []
    funcs = vars(math)
    for i in range(0, Ecuaciones):
        funcion = ecua[i]
        funcion_eval = eval(funcion, funcs, variables)
        derivada = derivadas[i]
        derivada_eval = eval(derivada, funcs, variables)
        nuevo_valor = variables[f'{var[i]}']-funcion_eval/derivada_eval
        variables[f'{var[i]}'] = nuevo_valor
        valor_ini.append(nuevo_valor)
        func_numerica.append(funcion_eval)
        derv_numerica.append(derivada_eval)
        # print(funcion_eval)
        # print(derivada_eval)
        # print(variables[f'{var[i]}'])
    return valor_ini, func_numerica  # ,derivada_eval


def cambiarValores(dic_var, nuevos_valores, num_ecuaciones, var):
    for i in range(0, num_ecuaciones):
        dic_var[f'{var[i]}'] = nuevos_valores[i]
    return dic_var



def derivadaSimple(ecuaciones, variables, num_ecuaciones):
    derivada_parcial = []
    for i in range(0, num_ecuaciones):
        var = sp.Symbol(variables[i])
        df_dvar = sp.Derivative(ecuaciones[i], var, evaluate=True)
        derivada_parcial.append(str(df_dvar))
    return derivada_parcial


def efunciones(var, valor, Ecuaciones):
    var_valor = {}
    for i in range(0, Ecuaciones):
        variable = var[i]
        anadir = {f'{variable}': valor[i]}
        var_valor.update(anadir)
    return var_valor


def newtonModificado(ecua, var, valor, Ecuaciones, emax, N=50):
    # constructor de la tabla
    encabezados = []
    contenido = []
    encabezados.append("Iteracion")
    for i in var:
        encabezados.append(f'f{var.index(i)}=0')
        #encabezados.append(f'f')
        #print(var.index(i))
        encabezados.append(i)
    encabezados.append(f"Error")
    tabla = PrettyTable(encabezados)
    tabla.title = "METODO DE NEWTON RHAPSON MULTIVARIABLE MODIFICADO"
    # Valores iniciales
    dicc_valores = efunciones(var, valor, Ecuaciones)
    # derivadas de las ecuaciones
    derv_parciales = derivadaSimple(ecua, var, Ecuaciones)

    for k in range(1, N):
        variables = cambiarValores(dicc_valores, valor, Ecuaciones, var)
        derivadas_numericas = []
        nuevos_Valores, funcion_evaluada = nuevosValoresa(
            ecua, derv_parciales, Ecuaciones, variables,var)
        # error
        ea = abs(max(funcion_evaluada))
        eb = abs(min(funcion_evaluada))
        if ea > eb:
            error = ea
        elif eb >= ea:
            error = eb
        # Verificar error
        if error < emax or error == 0:
            break
        # anadir a la tabla
        contenido = []
        contenido.append(k)
        for i in range(0, Ecuaciones):
            contenido.append("{0:.7f}".format(funcion_evaluada[i]))
            contenido.append("{0:.7f}".format(nuevos_Valores[i]))
        contenido.append("{0:.7f}".format(error))
        tabla.add_row(contenido)
        valor = nuevos_Valores
    # Constructor de la tabla de las derivadas parciales

    u = np.array(derv_parciales).T
    derivadas_p = PrettyTable()
    derivadas_p.title = "Derivadas parciales"
    der_res = []
    for j in range(0, Ecuaciones):
        der_res.append(f'df{j}/d{var[j]}')
    derivadas_p.add_row(u)
    derivadas_p.field_names = der_res
    print(derivadas_p)
    # print(f'{u}')
    print(tabla)
    print(f'Solucion del sistema:  ')
    for i in range(0, Ecuaciones):
        print(f'                     {var[i]} = {"{0:.4f}".format(valor[i])}')



""" ecua = ['x**2-10*x+y**2+8', 'x*y**2+x-10*y+8']
var = ['x', 'y']
valori = [0.0, 0.0]
Ecuaciones = 2 """

""" ecua = ['x**2+x-y**2-1', 'y-sin(x**2)']
var = ['x', 'y']
valori = [0.0, 0.0]
Ecuaciones = 2 """

""" ecua = ['x**2+y**2+z**2-9', 'x*y*z-1', 'x+y-z**2']
var = ['x', 'y', 'z']
valori = [2.5, 0.2, 1.6]
Ecuaciones = 3 """

""" #no converge
ecua = ['x**2-625*y**2', '3*x-cos(y*z)-0.5', 'exp(-x*y)+20*z+(10*pi-3)/3']
var = ['x', 'y', 'z']
valori = [1, 1, 1]
Ecuaciones = 3
 """
""" ecua = ['3*x-cos(y*z)-0.5', 'x**2-625*y**2', 'exp(-x*y)+20*z+(10*pi-3)/3']
var = ['x', 'y', 'z']
valori = [1, 0.2, 1]
Ecuaciones = 3
newtonModificado(ecua, var, valori, Ecuaciones, 1e-3) """
