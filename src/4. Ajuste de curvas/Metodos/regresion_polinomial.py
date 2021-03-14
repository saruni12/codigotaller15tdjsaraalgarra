import numpy as np
import sys

np.seterr(all='warn')

def sisEcua(mat_A, mat_B):
    a_inv = np.linalg.inv(mat_A)
    C = a_inv.dot(mat_B.T)
    return C


def sisDeEcuaciones(yx, x_elev, grado, n_datos):
    dimension = grado+1
    total_suma = len(x_elev)
    sistema = (dimension, dimension)
    mat_A = np.zeros(sistema)
    mat_B = np.matrix(yx)
    # ubicacion de datos en la matriz
    # primera fila
    col = 1
    for i in range(0, dimension-1):
        mat_A[0][col] = x_elev[i]
        col += 1
    # el resto de la ubicciones
    col = 0
    inicio = 0
    fin = dimension
    mat_A[0][0] = n_datos
    for i in range(1, dimension):
        for j in range(inicio, fin):
            mat_A[i][col] = x_elev[j]
            col += 1
        inicio += 1
        fin += 1
        col = 0
    # Para visualizar las matrices del sistema de ecuaciones
    #print(mat_A, mat_B)
    return sisEcua(mat_A, mat_B)


def multiplicacion(eje_y, datos_elev, cant_de_datos):
    datos_yx=[]
    for k in range(0, cant_de_datos):
        yx = eje_y[k]*datos_elev[k]
        datos_yx.append(yx)
        #print(datos_yx)
    return datos_yx


def potencia(eje_x, cant_de_datos, i):
    x_elev_i = []
    suma_x = 0
    for j in range(0, cant_de_datos):
        potencia = eje_x[j]**i
        x_elev_i.append(potencia)
        suma_x = suma_x+potencia
    return suma_x, x_elev_i


def rPolinomial(eje_x, eje_y, grado_del_polinomio):
    cant_de_datos = len(eje_y)
    cant_de_val_elevados = int(grado_del_polinomio*2)
    eje_y = np.array(eje_y)
    # vectores auxiliares
    suma_val_elevados_x = []
    suma_yx = []
    suma_y = np.sum(eje_y)
    suma_yx.append(suma_y)
    for i in range(1, cant_de_val_elevados+1):
        sumatoria, datos_elev = potencia(eje_x, cant_de_datos, i)
        suma_val_elevados_x.append(sumatoria)
        if i <= grado_del_polinomio:
            m = np.array(datos_elev)
            datos_yx = m*eje_y  # aqui falla
            suma_datos_yx = np.sum(datos_yx)
            suma_yx.append(suma_datos_yx)
            # Para visualizar las multiplicaciones de y*xi, y*x**2, etc.
            # print(datos_yx)
            # print(m)
            #print(datos_yx)
            # print(suma_yx)
    coeficientes = sisDeEcuaciones(
        suma_yx, suma_val_elevados_x, grado_del_polinomio, cant_de_datos)
    # visualizacion de los resultados
    print('\n     COEFICIENTES DEL AJUSTE POLINOMIAL\n')
    ecuacion_final = 'y = '
    for k in range(0, grado_del_polinomio+1):
        a = float(coeficientes[k])
        a_redondeada = "{0:.7f}".format(a)
        print(f'             a{k} = {a_redondeada} ')
        if k == 0:
            ec = str(a_redondeada)
        elif k == 1:
            ec = ' + '+str(a_redondeada)+'*x'
        else:
            ec = ' + '+str(a_redondeada)+'*x^'+str(k)
        ecuacion_final = ecuacion_final+ec
    print('\n La ecuacion de ajuste es:\n')
    print(f'         {ecuacion_final}')



#datos de prueba
""" x = [280, 650, 1000, 1200, 1500, 1700]
y = [32.7, 45.4, 52.15, 53.7, 52.9, 50.3]
grado = 2
rPolinomial(x, y, grado) """


""" x = [1976, 1992, 2001, 2012]
y = [205.42, 289.21, 276.45, 301.85]
grado = 2
rPolinomial(x, y, grado) """


""" x=[273,283,293,303,313,323,333,343,353,363,373]
y=[1.00738,1.00129,0.99883,0.99802,0.99804,0.99854,0.99943,1.00067,1.00229,1.00437,1.00697]
grado=4
rPolinomial(x, y, grado) """

""" x=[2,3,4,7,8,9,5,5]
y=[9,6,5,10,9,11,2,3] """

""" x = [50, 60, 70, 80,90,100]
y = [24.94,30.11,36.05,42.84,50.57,59.3]
grado=2
rPolinomial(x, y, grado) """


