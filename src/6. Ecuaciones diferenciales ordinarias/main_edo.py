import Metodos.Euler
import Metodos.Euler_modificado
import Metodos.Taylor
import Metodos.Runge_kutta


def datos():
    print("La ecuacion debe estaren funcion de f(x,y)")
    ecuacion = input("  Ecuacion a evaluar: ")
    x0 = float(input("  Intervalo de evaluacion  x0: "))
    x1 = float(input("  Intervalo de evaluacion  x1: "))
    y0 = float(input("  Valor evaluado en     y(x0): "))
    n = int(input("  No. de Subintervalos: "))
    return ecuacion, x0, x1, y0, n


def metodo(opcion):
    if opcion == 1:

        ecuacion, x0, x1, y, n = datos()
        Metodos.Euler.mEuler(ecuacion, x0, x1, y, n)

    elif opcion == 2:
        ecuacion, x0, x1, y, n = datos()
        Metodos.Taylor.mTaylor(ecuacion, x0, x1, y, n)

    elif opcion == 3:
        ecuacion, x0, x1, y, n = datos()
        Metodos.Euler_modificado.mEulerm(ecuacion, x0, x1, y, n)

    elif opcion == 4:
        ecuacion, x0, x1, y, n = datos()
        Metodos.Runge_kutta.mRungeK4orden(ecuacion, x0, x1, y, n)

    else:
        print("Opcion incorrecta, vuelva a seleccionar otra opcion")


if __name__ == '__main__':
    ejecutar = True

    while(ejecutar):
        # print(" \n- - - Ecuaciones no lineales - - -")
        opcion = int(input('''
        - - - integracion Numerica - - -\n
        Elegir un metodo:\n
            [1] Metodo de Euler 1er Orden
            [2] Metodo de Taylor 2do Orden
            [3] Metodo de Euler Modificado
            [4] Metodo de Runge - Kutta 4to Orden
            [5] Salir\n
        Opcion: '''))
        if opcion == 5:
            ejecutar = False
        else:
            metodo(opcion)
            ejecutar = False
