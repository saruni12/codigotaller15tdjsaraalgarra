
import Metodos.pf_multivariable
import Metodos.pf_desplazado
import Metodos.NewthonR_Mult
import Metodos.Newton_modificado
import math



def datos():
    ecua = []
    var = []
    valor = []
    Ecuaciones = int(input("Numero de ecuaciones:"))
    print("Variables:")
    for i in range(1, Ecuaciones+1):
        variables = input(f"   variable {i}:")
        var.append(variables)
    print("Ecuaciones:")
    for i in range(1, Ecuaciones+1):
        expr = input(f"   Ecuacion {i}:")
        ecua.append(expr)
    print("Valores iniciales:")
    #expr = ecuacion(Ecuaciones)
    for i in var:
        valor_inicial = float(input(f"   valor inicial de {i}="))
        valor.append(valor_inicial)
    error = 1e-3
    return ecua, var, valor, Ecuaciones, error


def metodo(opcion):
    if opcion == 1:
        print("\n                Metodo de Punto Fijo Multivariable")
        print("\nLas ecuaciones deben ser despejada (fi) de forma tal que: x=f1, y=f2, z=f3, etc. ")
        funciones, variables, valor_inic, cant_ecuaciones, error = datos()
        Metodos.pf_multivariable.punto_fijo_multivariable(
            funciones, variables, valor_inic, cant_ecuaciones, error)
    elif opcion == 2:
        print("\n                Metodo de Punto Fijo con Desplazamientos Sucesivos")
        print("\nLas ecuaciones deben ser despejada (fi) de forma tal que: x=f1, y=f2, z=f3, etc. ")
        funciones, variables, valor_inic, cant_ecuaciones, error = datos()
        Metodos.pf_desplazado.pfijo_des(
            funciones, variables, valor_inic, cant_ecuaciones, error)
    elif opcion == 3:
        print("\n                Metodo de Newton Rhapson")
        print("")
        funciones, variables, valor_inic, cant_ecuaciones, error = datos()
        Metodos.NewthonR_Mult.newtonR_multivariable(
            funciones, variables, valor_inic, cant_ecuaciones, error)
    elif opcion == 4:
        print("\n                Metodo de Newton Rhapson Modificado")
        print("")
        funciones, variables, valor_inic, cant_ecuaciones, error = datos()
        Metodos.Newton_modificado.newtonModificado(
            funciones, variables, valor_inic, cant_ecuaciones, error)
    else:
        print("Opcion incorrecta elige otra opcion")


if __name__ == '__main__':
    ejecutar = True

    while(ejecutar):
        # print(" \n- - - Ecuaciones no lineales - - -")
        opcion = int(input('''
        - - - Ecuaciones no lineales - - -\n
        Elegir un metodo:\n
            [1] Metodo de Punto Fijo Multivariable
            [2] Metodo de Punto Fijo con Desplazamientos Sucesivos
            [3] Metodo de Newton Rhapson
            [4] Metodo de Newton Rhapson Modificado

            [5] Salir\n
        Opcion: '''))
        if opcion == 5:
            ejecutar = False
        else:
            metodo(opcion)
            ejecutar = False

