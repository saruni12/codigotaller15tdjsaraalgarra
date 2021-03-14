
def minCuadrados(eje_x, eje_y):
    n = len(x)
    s_x = 0
    s_y = 0
    s_xy = 0
    s_xx = 0
    s_yy = 0
    for i in range(0, n):
        #operaciones entre las columnas
        xy = eje_x[i]*eje_y[i]
        xx = (eje_x[i])**2
        yy = (eje_y[i])**2
        # sumatorias
        s_x = s_x+eje_x[i]
        s_y = s_y+eje_y[i]
        s_xy = s_xy+xy
        s_xx = s_xx+xx
        s_yy = s_yy+yy
    #calculo de coeficientes
    r = (n*s_xy-s_x*s_y)/((n*s_xx-s_x**2)*(n*s_yy-s_y**2))**0.5
    b = (n*s_xy-s_x*s_y)/(n*s_xx-s_x**2)
    a = (s_y-s_x*b)/n
    print(s_x, s_y, s_xy, s_xx, s_yy)
    print(r, b, a)
    print(f'El coeficiente de correlacion es: r = {"{0:.3f}".format(r)}')
    print(f'La ecuacion:    y = {"{0:.4f}".format(a)} + {"{0:.4f}".format(b)} * x')
    #error  cuadratico medio = funcion de coste (calcula que tan mal esta nuestra funcion)
    y_new=[]
    suma_y_y=0
    for j in range (0,n):
        y=a+b*eje_x[j]
        y_new.append(y)
        suma_y_y=(y-eje_y[j])**2+suma_y_y
    ecm=suma_y_y/n
    print(y_new)
    print(ecm)



""" x = [1976, 1992, 2001, 2012]
y = [20542, 28921, 27645, 30185] """


x = [0,20,30,40,50,60]
y = [100,150,200,180,250,230]
minCuadrados(x, y)
