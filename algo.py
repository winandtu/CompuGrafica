import numpy as np

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
        #print("x_inc", x_inc)
            x_i += 1
            
            print("x =", x_i," / y = ", round( y_i ), "x incrementa-->: ", x_inc)

    def algDda(self):
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

        #algDda( [9,18], [14,22] )
    
    def getAlgoritmo(self):

        if self.nombreAlg =="Algoritmo Basico":
             self.algBasico()

        elif self.nombreAlg=="Algoritmo DDA":
            self.algDda()
        else:
            print("Aun no esta implementado")

print("\n 1.Algoritmo Basico \n 2.Algoritmo DDA \n 3.Salir ")
op=int(input("Ingrese la opcion:"))

while op!=0:
    basico= Algoritmos("Algoritmo Basico",[-2,1],[2,5]) #punto de prueba en donde los podra modificar
    dda = Algoritmos("Algoritmo DDA",[-2,1],[2,5])

    if op==1:
        basico.getAlgoritmo()
        break
    elif op==2:
        dda.getAlgoritmo()
        break
    else:
        print("\ningrese otra opcion")
        
    op=int(input("\nOpcion:"))
print("\nAdios")
    
    #basico.getAlgoritmo()



