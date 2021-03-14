import Metodos.Polinomios_de_lagrange
import Metodos.Polinomios_de_Newton
import Metodos.Pol_Newton_dif_finitas
import Metodos.regresion_polinomial
import Metodos.MC_multilineal



def metodo(opcion):
    if opcion == 1:
        # Variables
        x = [1, 5, 20, 40]
        y = [56.5, 113, 181, 214.5]
        # X0: El valor a evaluar
        x0 = 2
        # True: Paraevaluar, False: Para solo mostrar las ecuaciones
        evaluar = True
        # aproxLagrange(Var. dependiente, Var. Independiente, numero a evaluar, activar desactivar )
        Metodos.Polinomios_de_lagrange.aproxLagrange(x, y, x0,evaluar)
    elif opcion == 2:
        # regresion de Polinimios de newton
        x = [1, 2, 5, 10, 20, 30, 40]
        y = [65.5, 78.6, 113, 144.5, 181, 205, 214.5]
        # X0: El valor a evaluar
        x0 = 4
        # El orden de diferencias finitas que se desea utilizar
        orden = 2
        evaluar = True
        # aproxNewton(Var. dependiente, Var. Independiente,numero a evaluar, orden , activar o descativar la evaluacion)
        Metodos.Polinomios_de_Newton.aproxNewton(x, y, x0, orden, evaluar)
    elif opcion == 3:
        # Polinomio de newton por diferencias finitas
        x = [50, 60, 70, 80, 90, 100]
        y = [24.94, 30.11, 36.05, 42.84, 50.57, 59.3]
        # X0: El valor a evaluar
        x0 = 68
        # El orden de diferencias finitas que se desea utilizar
        orden = 2
        # aproxNewtondif(Var. dependiente, Var. Independiente, numero a evaluar,orden)
        Metodos.Pol_Newton_dif_finitas.aproxNewtondif(x, y, x0, orden)

    elif opcion == 4:
        #Regresion polinomial por minimos cuadrados
        x = [50, 60, 70, 80,90,100]
        y = [24.94,30.11,36.05,42.84,50.57,59.3]#grado del polinomio
        grado=2
        Metodos.regresion_polinomial.rPolinomial(x, y, grado)
    elif opcion == 5:
        # Regresion Lineal Multiple
        # variable dependiente
        agua = [27.5, 28, 28.8, 29.1, 30, 31, 32]
        # variables independientes
        cal = [2, 3.5, 4.5, 2.5, 8.5, 10.5, 13.5]
        puzolana = [18, 16.5, 10.5, 2.5, 9, 4.5, 1.5]
        # Crear la data de todas las variables
        variables_data = [cal, puzolana]
        # nombre con los que se asignara a las variables
        nombre_variable = ['cal', 'puzolana']
        # multilineal(Variable dependiente,variables independientes,nombre de las variables)
        Metodos.MC_multilineal.multilineal(agua, variables_data, nombre_variable)
    else:
        print("Opcion incorrecta elige otra opcion")


if __name__ == '__main__':
    ejecutar = True

    while(ejecutar):
        opcion = int(input('''
        - - - Aproximacion funcional e Interpolacion - - -\n
        Elegir un metodo de Ajuste:\n
            [1] Polinomios de Lagrange
            [2] Ponomios de Newton
            [3] Ponomios de Newton por Diferencias Finitas
            [4] Regresion Polinomial
            [5] Regresion Multilineal

            [6] Salir\n
        Opcion: '''))
        if opcion == 6:
            ejecutar = False
        else:
            metodo(opcion)
            ejecutar = False
