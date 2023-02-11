
import numpy as np


def sisEcua(mat_A, mat_B):
    a_inv = np.linalg.inv(mat_A)
    C = a_inv.dot(mat_B.T)
    return C


def matrices(sm, smm, smy, smn, datos, cant_datos):
    dimension = datos+1
    s = (dimension, dimension)
    mat_A = np.zeros(s)
    mat_B = np.matrix(smy)
    # contadores
    n = len(smn)
    fin = datos-1
    con_master = fin-1
    ini = 0
    fil = 1
    col = 1
    # primer numero ubicado
    mat_A[0][0] = cant_datos
    for i in range(0, datos):
        mat_A[i+1][i+1] = smm[i]
        mat_A[0][i+1] = sm[i]
        mat_A[i+1][0] = sm[i]
    # ubicacion de la variables multiplicadas por otras variables
    for i in range(1, datos):
        for j in range(ini, fin):
            mat_A[i][col+1] = smn[j]
            mat_A[col+1][i] = smn[j]
            col += 1
        fil += 1
        col = col-con_master
        ini = fin
        fin = fin+con_master
        con_master -= 1
    #para visualizar las matrices
    # print(mat_A)
    # print(mat_B)
    return sisEcua(mat_A, mat_B)


def multilineal(var_dependiente, var_independiente, nombre_variables):
    variables = len(nombre_variables)
    sis_ecuaciones = len(nombre_variables)+1
    cant_datos = len(var_dependiente)
    # vectores auxiliares
    var_al_cuadrado = []
    var_por_y = []
    var_multiplicadas = []
    # vectores de las sumas
    suma_var_al_cuadrado = []
    suma_var = []
    suma_por_y = []
    suma_de_var_por_var = []
    # variable dependiente
    y = np.array(var_dependiente)
    sum_y = np.sum(y)
    suma_por_y.append(sum_y)
    # multiplicaciones de m*n, m*p y n*p
    k = 1
    # operaciones
    for var_i in range(variables):
        m = np.array(var_independiente[var_i])
        y_por_m = y*m
        m_cuadrado = m*m
        # anade las m**2 y los m*y
        var_al_cuadrado.append(m_cuadrado)
        var_por_y.append(y_por_m)
        # sumas
        suma_mm = np.sum(m_cuadrado)
        suma_var_al_cuadrado.append(suma_mm)
        suma_m = np.sum(m)
        suma_var.append(suma_m)
        suma_my = np.sum(y_por_m)
        suma_por_y.append(suma_my)

        # multiplicaciones cor cada variable
        for i in range(k, variables):
            n = np.array(var_independiente[i])
            multipl = m*n
            var_multiplicadas.append(multipl)
            # suma de las multiplicaciones
            suma_mn = np.sum(multipl)
            suma_de_var_por_var.append(suma_mn)
        k += 1

    """ #para visualizar las sumatorias
    print(var_al_cuadrado)
    print(var_por_y)
    print(var_multiplicadas)
    print(suma_var)
    print(suma_var_al_cuadrado)
    print(suma_por_y)
    print(suma_de_var_por_var) """
    resultado=matrices(suma_var, suma_var_al_cuadrado,
             suma_por_y, suma_de_var_por_var, variables, cant_datos)
    #resultados finales
    ecuacion_final='y = '
    print('\n     COEFICIENTES DEL AJUSTE LINEAL MULTIPLE\n')
    for i in range(0,variables+1):
        solucion=float(resultado[i])
        sol_redondeada="{0:.7f}".format(solucion)
        print(f'             a{i} = {sol_redondeada} ')
        if i>0:
            ec=' + '+str(sol_redondeada)+'*'+str(nombre_variables[i-1])
        else:
            ec=str(sol_redondeada)
        ecuacion_final=ecuacion_final+ec
    print('\n La ecuacion de ajuste es:\n')
    print(f'            {ecuacion_final}')
    print('\nNota: y = Var. Dependiente')




# datos de prueba
#set 1
""" agua = [27.5, 28, 28.8, 29.1, 30, 31, 32]
cal = [2, 3.5, 4.5, 2.5, 8.5, 10.5, 13.5]
puzo = [18, 16.5, 10.5, 2.5, 9, 4.5, 1.5]
dr = [5, 2, 3, 4, 1, 2, 3]
gh = [7, 2, 1, 1, 1, 6, 7]
puzos = [15, 15.5, 11.5, 5, 5, 3, 1]

variables_data = [cal, puzo]
variable = ['u', 'v']

variables_data = [cal, puzo, dr, gh, puzos]
variable = ['u', 'v', 'w', 'z', 's'] """

#set 2
""" u=[0.02,0.02,0.02,0.02,0.1,0.1,0.1,0.1,0.18,0.18,0.18,0.18]
v=[1000,1100,1200,1300,1000,1100,1200,1300,1000,1100,1200,1300]
fuv=[78.9,65.1,55.2,56.4,80.9,69.7,57.4,55.4,85.3,71.8,60.7,58.9]
variables_data = [u,v]
variable = ['u', 'v'] """

""" agua = [27.5, 28, 28.8, 29.1, 30, 31, 32]
cal = [2, 3.5, 4.5, 2.5, 8.5, 10.5, 13.5]
puzo = [18, 16.5, 10.5, 2.5, 9, 4.5, 1.5]

variables_data = [cal, puzo]
variable = ['u', 'v']


multilineal(agua, variables_data, variable) """
