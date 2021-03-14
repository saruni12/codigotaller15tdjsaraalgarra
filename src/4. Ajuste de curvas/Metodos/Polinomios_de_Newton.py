
def evalua(ecuacion,val):
    x=val
    y = eval(str(ecuacion))
    return y

def diferenciasDivididas(eje_x, eje_y,j):
    cant = len(eje_y)
    d=[]
    for i in range(0, cant-1):
        fx = eje_y[i+1]
        fx0 = eje_y[i]
        x = eje_x[i+1+j]
        x0 = eje_x[i]
        funcion = (fx-fx0)/(x-x0)
        d.append(funcion)
    #Para visualizar las diferencias divididas en cada orden
    #print(d)
    return d


def aproxNewton(eje_x, eje_y,valor,orden,evaluar):
    if orden>=len(eje_y):
        orden=len(eje_y)-1
    grado=len(eje_y)-orden
    dif_div=eje_y
    ecuacion=f'{eje_y[orden-1]}'
    m=''
    #orden_dif_dv=[eje_y[0]]
    print(f'\n               APROXIMACION POLINOMIAL DE NEWTON DE ORDEN {orden}\n')
    for j in range(0,grado):
        d=diferenciasDivididas(eje_x, dif_div,j)
        dif_div=d
        #orden_dif_dv.append(dif_div[0])
        var=f'(x-{eje_x[j+orden-1]})'
        m=m+'*'+var
        ecuacion=ecuacion+'+'+str("{0:.4f}".format(dif_div[orden-1]))+m
        print(f'  Grado {j+1}:     {ecuacion}\n')
        if evaluar==True:
            y_eval=evalua(ecuacion,valor)
            print(f'                Para:  x = {valor}   =>   y = {"{0:.4f}".format(y_eval)}\n')


#datos de prueba
""" x = [1, 5, 20, 40]
y = [56.5, 113, 181, 214.5] """


""" x=[-2,-1,0,2,3,6]
y=[-18,-5,-2,-2,7,142] """

""" x = [50, 60, 70, 80,90,100]
y = [24.94,30.11,36.05,42.84,50.57,59.3] """

""" x=[1,2,5,10,20,30,40]
y=[65.5,78.6,113,144.5,181,205,214.5]
x0=4
orden=2
evaluar=True
aproxNewton(x, y,x0,orden,evaluar) """
