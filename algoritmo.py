import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size

class Algoritmos:

    #constructor
    def __init__(self, nombreAlg, puntoIni, puntoFin):
        self.nombreAlg=nombreAlg
        self.puntoIni=puntoIni
        self.puntoFin=puntoFin


    
    #Algoritmos de lineas
    def algBasico (self):
        print(f"--------Puntos: ({self.puntoIni}) y ({self.puntoFin})---------\n")
        x_inc = 1
        x_i = self.puntoIni[0]
        y_i = self.puntoIni[1]
        delta_y = abs( self.puntoFin[1] - self.puntoIni[1] )
        delta_x = abs( self.puntoFin[0] - self.puntoIni[0] )
        m = delta_y / delta_x
        print('m -->', m )
        print("x =", x_i," / y = ", round( y_i ), "--------- x_inc : ", x_inc)
        for i in range ( delta_x ):
            y_i = self.puntoFin[0] +  m * x_inc
            x_inc += 1

            x_i += 1
            
            print("x =", x_i," / y = ", round( y_i ), "x incrementa-->: ", x_inc)

    def algDda(self):
        print(f"--------Puntos: ({self.puntoIni}) y ({self.puntoFin})---------\n")
        x_i = self.puntoIni[0]
        y_i = self.puntoIni[1]
        delta_y = abs( self.puntoFin[1] - self.puntoIni[1] )
        delta_x = abs( self.puntoFin[0] - self.puntoIni[0] )
        step = 0
        if ( delta_x > delta_y ):
            step = delta_x
        else:
            step = delta_y
        x_inc = delta_x / step
        y_inc = delta_y / step
        print("incremental x, y =>", x_inc, y_inc)
        print("x =", round( x_i )," / y = ", round( y_i ))
        for i in range ( step ):
            x_i += x_inc
            y_i += y_inc
            print("x =", round(x_i)," / y = ", round (y_i))



    def algBresenham(self):
        print(f"--------Puntos: ({self.puntoIni}) y ({self.puntoFin})---------\n")
        x_i = self.puntoIni[0]
        y_i = self.puntoIni[1]
        delta_y = abs( self.puntoFin[1] - self.puntoIni[1] )
        delta_x = abs( self.puntoFin[0] - self.puntoIni[0] )
        p_i = 2 * delta_y - delta_x
        print( "P inicial ", p_i)
        for i in range( delta_x ):
            if( p_i < 0 ):
                x_i += 1
                p_i += ( 2 * delta_y )
            else:
                x_i += 1
                y_i += 1
                p_i += ( 2 * delta_y - 2 * delta_x)
            print("x =", x_i," / y = ", y_i, "---- P : ", p_i)
    
    # algoritmo para una circunferencia
        
    def algMidpoint(self):
        radio=self.puntoFin
        print(f"--------Punto: ({self.puntoIni}) y Radio: ({radio})---------\n")
        p_i = 1 - radio
        x_i = self.puntoIni [0]
        y_i = self.puntoIni [1] + radio
        print("x =", x_i," / y = ", y_i, "---- P : ", p_i)
        
        
        for i in range (radio):
            if (p_i >= 0 ):
                x_i += 1
                y_i -= 1
                p_i += - 2 * y_i + 2 * x_i
            else:
                x_i += 1     
                p_i += 2 * x_i + 1
            print("x =", x_i," / y = ", y_i, "---- P : ", p_i)
        


    
    def getAlgoritmo(self):

        if self.nombreAlg =="Algoritmo Basico":
             self.algBasico()

        elif self.nombreAlg=="Algoritmo DDA":
            self.algDda()

        elif self.nombreAlg=="Algoritmo Bresenham":
            self.algBresenham()
        
        elif self.nombreAlg=="Algoritmo Punto Medio":
            self.algMidpoint()
        else:
            print("Aun no esta implementado")

print("\n 1.Algoritmo Basico \n 2.Algoritmo DDA \n 3.Algoritmo Brsenham \n 4.Algoritmo Punto Medio \n 5.Salir ")
op=int(input("Ingrese la opcion:"))

while op!=5:
    basico= Algoritmos("Algoritmo Basico",[4,1],[3,5]) #punto de prueba en donde los podra modificar
    dda = Algoritmos("Algoritmo DDA",[-3,2],[2,5])
    bresenham=Algoritmos( "Algoritmo Bresenham",[7,20], [17,25] )
    circunferencia = Algoritmos("Algoritmo Punto Medio",[2,6], 4)

    if op==1:
        print("-----------------ALGORITMO BASICO-----------------\n")
        basico.getAlgoritmo()
        break
    elif op==2:
        print("----------------ALGORITMO DDA------------------\n")
        dda.getAlgoritmo()
        break
    elif op==3:
        print("--------------ALGORITMO BRESENHAM------------------\n")
        bresenham.getAlgoritmo()
        break
    elif op==4:
        print("----------------ALGORITMO PUNTO MEDIO-----------------\n")
        circunferencia.getAlgoritmo()
        break

    else:
        print("\ningrese otra opcion")
        
    op=int(input("\nOpcion:"))
print("\nAdios")
    
    #basico.getAlgoritmo()



