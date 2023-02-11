import Metodos.Simpson_1_3
import Metodos.Trapezoidal
import Metodos.Simpson_3_8
import Metodos.Romberg


def datos():
    print("La ecuacion debe estaren funcion de (x)")
    ecuacion = input("  Ecuacion a evaluar: ")
    x0 = float(input("  Limite inferior: "))
    x1 = float(input("  Limite superior: "))
    return ecuacion, x0, x1


def metodo(opcion):
    if opcion == 1:

        ecuacion, x0, x1 = datos()
        n = int(input("Numero de franjas: "))
        Metodos.Trapezoidal.mTrapecio(ecuacion, x0, x1, n)

    elif opcion == 2:
        ecuacion, x0, x1 = datos()
        n = int(input("Numero de franjas: "))
        Metodos.Simpson_1_3.mSimpson13(ecuacion, x0, x1, n)

    elif opcion == 3:
        ecuacion, x0, x1 = datos()
        n = int(input("Numero de franjas: "))
        Metodos.Simpson_3_8.mSimpson38(ecuacion, x0, x1, n)

    elif opcion == 4:
        ecuacion, x0, x1 = datos()
        n = int(input("Numero de puntos: "))
        Metodos.Romberg.mRomberg(ecuacion, x0, x1, n)

    else:
        print("Opcion incorrecta, vuelva a seleccionar otra opcion")


if __name__ == '__main__':
    ejecutar = True

    while(ejecutar):
        # print(" \n- - - Ecuaciones no lineales - - -")
        opcion = int(input('''
        - - - integracion Numerica - - -\n
        Elegir un metodo:\n
            [1] Metodo del Trapecio
            [2] Metodo de Simpson 1/3
            [3] Metodo de Simpson 3/8
            [4] Metodo de Romberg
            [5] Salir\n
        Opcion: '''))
        if opcion == 5:
            ejecutar = False
        else:
            metodo(opcion)
            ejecutar = False
