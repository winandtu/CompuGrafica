import numpy as np
import pylab as pl


#Para graficar
# pintar línea
def pintar_linea_basico( punto_inicial, punto_final):
  xpin=[]
  ypin=[]

  x_inc = 1
  x_i = punto_inicial[0]
  y_i = punto_inicial[1]
  delta_y = abs( punto_final[1] - punto_inicial[1] )
  delta_x = abs( punto_final[0] - punto_inicial[0] )
  m = delta_y / delta_x

  for i in range ( delta_x ):
    y_i = punto_final[0] +  m * x_inc
    x_inc += 1
    x_i += 1

    xpin.append(x_i)
    ypin.append(y_i)
    pl.plot(xpin,ypin)

def midpoint_circunferencia( punto, radio ):
  xpin=[]
  ypin=[]
  p_i = 1 - radio
  x_i = punto [0]
  y_i = punto [1] + radio

  for i in range (radio):
    if (p_i >= 0 ):
      x_i += 1
      y_i -= 1
      p_i += - 2 * y_i + 2 * x_i
    else:
      x_i += 1     
      p_i += 2 * x_i + 1
    
    xpin.append(x_i)
    ypin.append(y_i)
    pl.plot(xpin,ypin)


def algDda(puntoIni, puntoFin):
  xpin=[]
  ypin=[]
  x_i = puntoIni[0]
  y_i = puntoIni[1]
  delta_y = abs( puntoFin[1] - puntoIni[1] )
  delta_x = abs( puntoFin[0] - puntoIni[0] )
  step = 0
  if ( delta_x > delta_y ):
      step = delta_x
  else:
      step = delta_y
  x_inc = delta_x / step
  y_inc = delta_y / step

  for i in range ( step ):
    x_i += x_inc
    y_i += y_inc
    xpin.append(x_i)
    ypin.append(y_i)
    pl.plot(xpin,ypin)

def algBresenham(puntoIni,puntoFin):
    xpin=[]
    ypin=[]
    x_i = puntoIni[0]
    y_i = puntoIni[1]
    delta_y = abs( puntoFin[1] - puntoIni[1] )
    delta_x = abs( puntoFin[0] - puntoIni[0] )
    p_i = 2 * delta_y - delta_x
    for i in range( delta_x ):
      if( p_i < 0 ):
          x_i += 1
          p_i += ( 2 * delta_y )
      else:
          x_i += 1
          y_i += 1
          p_i += ( 2 * delta_y - 2 * delta_x)
      xpin.append(x_i)
      ypin.append(y_i)
      pl.plot(xpin,ypin)
      



#Graficar los algoritmos
def pintarBasico():
  #Aqui se podra ingresar los puntos del espacio
  puntI=[-2,1]
  puntF=[2,5] 
  pintar_linea_basico(puntI , puntF)
  pl.title(f"PUNTOS---> Punto Inicial: {puntI}  Punto Final: {puntF}")
  pl.show()

def pintarCirculo():
  #Aqui se podra ingresar los puntos del espacio
  puntI=[2,6]
  radio=4
  midpoint_circunferencia(puntI,radio)
  pl.title(f"PUNTOS---> Punto Inicial: {puntI}  Radio: {radio}")
  pl.show()

def pintarDda():
  #Aqui se podra ingresar los puntos del espacio
  puntI=[-3,2]
  puntF=[2,5]
  algDda( puntI,puntF)
  pl.title(f"PUNTOS---> Punto Inicial: {puntI}  Punto Final: {puntF}")
  pl.show()

def pintarBres():
  #Aqui se podra ingresar los puntos del espacio
  puntI=[7,20]
  puntF=[17,25]
  algBresenham(puntI ,puntF )
  pl.title(f"PUNTOS---> Punto Inicial: {puntI}  Punto Final: {puntF}")
  pl.show()



