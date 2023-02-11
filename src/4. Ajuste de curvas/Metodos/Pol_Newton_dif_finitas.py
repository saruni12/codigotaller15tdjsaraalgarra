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
        funcion = (fx-fx0)#/(x-x0)
        d.append(funcion)
    #Para visualizar las diferencias divididas en cada orden
    #print(d)
    return d


def aproxNewtondif(eje_x, eje_y,valor,orden):
    if orden>=len(eje_y):
        orden=len(eje_y)-1
    grado=len(eje_y)-orden
    dif_div=eje_y
    #Coeficientes de la ecuacion s,h
    h=abs(eje_x[0]-eje_x[1])
    s=(valor-eje_x[orden-1])/h
    px=eje_y[orden-1]
    si=1
    fact=1
    print(f'\n               APROXIMACION POLINOMIAL DE NEWTON DE ORDEN {orden}\n')
    for j in range(0,grado):
        d=diferenciasDivididas(eje_x, dif_div,j)
        dif_div=d
        if j==0:
            px=px+s*d[orden-1]
        else:
            fact=fact*(j+1)
            si=si*(s-(j))
            px=px+si*s*d[orden-1]/fact
            #print(si,fact)
        print(f' Polinomio de Grado {j+1}:   x = {valor}   =>   y = {"{0:.5f}".format(px)}\n')


#datos de prueba



""" x=[-2,-1,0,2,3,6]
y=[-18,-5,-2,-2,7,142] """


""" x = [50, 60, 70, 80,90,100]
y = [24.94,30.11,36.05,42.84,50.57,59.3]
x0=68
orden=2

aproxNewton(x, y,x0,orden) """