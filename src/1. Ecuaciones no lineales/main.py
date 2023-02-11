# importamos los otros archivos python
import Metodo.Newton_Raphson
import Metodo.secante
import Metodo.punto_fijo
import Metodo.Biseccion
import Metodo.Falsa_Posicion
import Metodo.steffensen
import Metodo.Newton_2do
import Metodo.muller
import numpy as np
import math


def dos_puntos():
    primer_valor = float(input("valor X0: "))
    segundo_valor = float(input("valor x1: "))
    return primer_valor, segundo_valor


def tolerancia():
    error = float(input("Error:  "))
    return error


def ecuacion():
    expr = input("Ecuacion a evaluar: ")
    return expr


def metodo(opcion):
    if opcion == 1:
        print("La ecuacion debe ser despejada de forma tal que: f(x)=x")
        expr = ecuacion()
        valor_inicial = float(input("valor inicial: "))
        error = tolerancia()
        Metodo.punto_fijo.punto_fijo(expr, valor_inicial, error)

    elif opcion == 2:
        expr = ecuacion()
        valor_inicial = float(input("valor a inicial: "))
        error = tolerancia()
        Metodo.Newton_Raphson.Newton_R(expr, valor_inicial, error)

    elif opcion == 3:
        expr = ecuacion()
        primer_valor, segundo_valor = dos_puntos()
        error = tolerancia()
        Metodo.secante.secante_x(
            expr, primer_valor, segundo_valor, error)

    elif opcion == 4:
        expr = ecuacion()
        primer_valor, segundo_valor = dos_puntos()
        error = tolerancia()
        fx0 = Metodo.Falsa_Posicion.funcion(expr, primer_valor)
        fx1 = Metodo.Falsa_Posicion.funcion(expr, segundo_valor)
        signo = fx0 * fx1
        if signo > 0:
            print("Valores incorrectos")
        else:
            Metodo.Falsa_Posicion.falsa_Posicion(
                expr, primer_valor, segundo_valor, error*0.1)

    elif opcion == 5:
        expr = ecuacion()
        primer_valor, segundo_valor = dos_puntos()
        error = tolerancia()
        fx0 = Metodo.Biseccion.funcion(expr, primer_valor)
        fx1 = Metodo.Biseccion.funcion(expr, segundo_valor)
        signo = fx0 * fx1
        if signo > 0:
            print("Valores iniciales incorrectos")
        elif fx0 > 0 or fx1 < 0:
            Metodo.Biseccion.biseccion(
                expr, segundo_valor, primer_valor, error)
        else:
            Metodo.Biseccion.biseccion(
                expr, primer_valor, segundo_valor, error)

    elif opcion == 6:
        print("La ecuacion debe ser despejada de forma tal que: f(x)=x")
        expr = ecuacion()
        valor_inicial = float(input("valor inicial: "))
        error = tolerancia()
        Metodo.steffensen.Steffensen(expr, valor_inicial, error)
    elif opcion == 7:
        expr = ecuacion()
        valor_inicial = float(input("valor a inicial: "))
        error = tolerancia()
        Metodo.Newton_2do.Newton_R2do_orden(expr, valor_inicial, error)
    elif opcion == 8:
        expr = ecuacion()
        print("Valores Iniciales")
        x0 = float(input("    x0: "))
        x1 = float(input("    x1: "))
        x2 = float(input("    x2: "))
        error = tolerancia()
        Metodo.muller.Muller(expr, x0, x1, x2, error, N=100)
    else:
        print("Opcion incorrecta, vuelva a seleccionar otra opcion")


if __name__ == '__main__':
    ejecutar = True

    while(ejecutar):
        # print(" \n- - - Ecuaciones no lineales - - -")
        opcion = int(input('''
        - - - Ecuaciones no lineales - - -\n
        Elegir un metodo:\n
            [1] Metodo de Punto Fijo
            [2] Metodo de Newton Rhapson
            [3] Metodo de la Secante
            [4] Metodo de la Falsa Posicion
            [5] Metodo de la Biseccion
        Metodos Acelerados
            [6] Metodo de Steffensen
            [7] Metodo de Newton Rhapson de 2do orden
            [8] Metodo de Muller
            [9] Salir\n
        Opcion: '''))
        if opcion == 9:
            ejecutar = False
        else:
            metodo(opcion)
            ejecutar = False
# ecuaciones de ejemplo


""" def f(x):
    return x**3+2*x**2+10*x-20
# 20/(x**2+2*x+10)


def g(x):
    return math.cos(x)-3*x """
