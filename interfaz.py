import tkinter as tk
import graficas
import pylab as pl
#colores boton
def Interfaz():
    colorBasico = "#ff914d"
    colorDda = "#ff66c4"
    colorBres = "#8c52ff"
    colorPoint = "#f0a5d3"

    ventana = tk.Tk()
    ventana.title("Algoritmos de discretizacion")
    ventana.geometry("1024x768+500+50")
    ventana.resizable(width=False, height=False) #Para no cambiar el tamaño de la interfaz
    fondo = tk.PhotoImage(file="plantilla.png") #carga la plantilla
    fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1,relheight=1)

    #################

    def ejecutarBasico():
        graficas.pintarBasico()
        

    def ejecutarDda():
        graficas.pintarDda()
    
    def ejecutarBres():
        graficas.pintarBres()
    
    
    def ejecutarPoint():
        graficas.pintarCirculo()

    #Botones

    botonBasico = tk.Button(ventana, text="Algoritmo Basico",command=ejecutarBasico,cursor="hand2",bg=colorBasico, width=12, relief="flat", font=("Comic Sans MS",12,"bold"))
    botonBasico.place(x=450, y=150)

    botonDda = tk.Button(ventana, text="Algoritmo DDA",command=ejecutarDda,cursor="hand2",bg=colorDda, width=12, relief="flat", font=("Comic Sans MS",12,"bold"))
    botonDda.place(x=450, y=270)

    botonBres = tk.Button(ventana, text="Alg. Bressehan",command=ejecutarBres,cursor="hand2",bg=colorBres, width=20, relief="flat", font=("Comic Sans MS",12,"bold"))
    botonBres.place(x=415, y=400)

    botonPoint = tk.Button(ventana, text="Alg. Punto Medio",command=ejecutarPoint,cursor="hand2",bg=colorPoint, width=15, relief="flat", font=("Comic Sans MS",12,"bold"))
    botonPoint.place(x=440, y=540)



    ventana.mainloop()

Interfaz()