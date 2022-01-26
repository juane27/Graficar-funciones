import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import EjercicioControlador

app = EjercicioControlador.FuncionesDominio()



ventana = tk.Tk()
ventana.title("Graficar funciones")

ttk.Label(ventana, text="Graficar funciones", font=("Arial Bold", 30)).grid(row=0,column=0, columnspan=2)



def enviarValores(a,b,c):
    dominios = []
    a=int(a)
    b=int(b)
    modelos = (c)
    for i in range(a,b+1):
        dominios.append(int(i))
    app.funciones(dominios,modelos)
    



def chequearDominios():
    modelos = []
    dominio3 = float(dominio1.get())
    dominio4 = float(dominio2.get())

    if(intchk1.get()==1):
        if(dominio3<-4 or dominio4>2):
            messagebox.showerror("Error de dominio", "Revise su valor de dominio para la función 1.\nEl dominio comprende {XϵR: -11/3 ≤ x ≤ 5/2}.")
        else:
            pass

    if(intchk5.get()==1):
        if(dominio3<2 or dominio4<2):
            messagebox.showerror("Error de dominio", "Revise su valor de dominio para la función 5.\nEl dominio comprende {XϵR: x >= 2}.")
        else:
            pass
    if(intchk7.get()==1):
        if(dominio3==1.73 or dominio4==1.73):
            messagebox.showerror("Error de dominio", "Revise su valor de dominio para la función 7.\nEl dominio comprende {XϵR: x≠-√3 & x≠√3}.")
        else:
            pass
    if(intchk8.get()==1):
        number= -2
        if number in range(int(dominio3), int(dominio4)):
            messagebox.showerror("Error de dominio", "Revise su valor de dominio para la función 7.\nEl dominio comprende {XϵR: x≠-2}.")
        else:
            pass

    if(intchk9.get()==1):
        if(dominio3>=3 or dominio4>=3):
            messagebox.showerror("Error de dominio", "Revise su valor de dominio para la función 7.\nEl dominio comprende {XϵR: x<3}.")
        else:
            pass


    intchk = [intchk1,intchk2,intchk3,intchk4,intchk5,intchk6,intchk7,intchk8,intchk9,intchk10]
    for i in range(1,11):
        if(intchk[i-1].get()==(1)):
           modelos.append(int(i))
    enviarValores(dominio3,dominio4,modelos)

    
         
          

####Variables checkboxs####
intchk1= tk.IntVar()
intchk2= tk.IntVar()
intchk3= tk.IntVar()
intchk4= tk.IntVar()
intchk5= tk.IntVar()
intchk6= tk.IntVar()
intchk7= tk.IntVar()
intchk8= tk.IntVar()
intchk9= tk.IntVar()
intchk10= tk.IntVar()
intchk11= tk.IntVar()



####Pregunta####
ttk.Label(ventana, text="¿Qué funciones desea calcular?").grid(row=2,column=0)


####Imagenes
photo1 = tk.PhotoImage(file='imagenes\\formula1.png')
photo2 = tk.PhotoImage(file='imagenes\\formula2.png')
photo3 = tk.PhotoImage(file='imagenes\\formula3.png')
photo4 = tk.PhotoImage(file='imagenes\\formula4.png')
photo5 = tk.PhotoImage(file='imagenes\\formula5.png')
photo6 = tk.PhotoImage(file='imagenes\\formula6.png')
photo7 = tk.PhotoImage(file='imagenes\\formula7.png')
photo8 = tk.PhotoImage(file='imagenes\\formula8.png')
photo9 = tk.PhotoImage(file='imagenes\\formula9.png')
photo10 = tk.PhotoImage(file='imagenes\\formula10.png')


####Checkboxs columna 0####

checkbox1 = tk.Checkbutton(ventana, text='1)', variable=intchk1)
checkbox1.grid(row=3, column=0)
checkbox1.config(image=photo1,compound='right')

checkbox2 = tk.Checkbutton(ventana, text='2)', variable=intchk2)
checkbox2.grid(row=4, column=0)
checkbox2.config(image=photo2,compound='right')

checkbox3 = tk.Checkbutton(ventana, text='3)', variable=intchk3)
checkbox3.grid(row=5, column=0)
checkbox3.config(image=photo3,compound='right')

checkbox4 = tk.Checkbutton(ventana, text='4)', variable=intchk4)
checkbox4.grid(row=6, column=0)
checkbox4.config(image=photo4,compound='right')

checkbox5 = tk.Checkbutton(ventana, text='5)', variable=intchk5)
checkbox5.grid(row=7, column=0)
checkbox5.config(image=photo5,compound='right')


####Checkboxs columna 1####

checkbox6 = tk.Checkbutton(ventana, text='6)', variable=intchk6)
checkbox6.grid(row=3, column=1)
checkbox6.config(image=photo6,compound='right')

checkbox7 = tk.Checkbutton(ventana, text='7)', variable=intchk7)
checkbox7.grid(row=4, column=1)
checkbox7.config(image=photo7,compound='right')

checkbox8 = tk.Checkbutton(ventana, text='8)', variable=intchk8)
checkbox8.grid(row=5, column=1)
checkbox8.config(image=photo8,compound='right')

checkbox9 = tk.Checkbutton(ventana, text='9)', variable=intchk9)
checkbox9.grid(row=6, column=1)
checkbox9.config(image=photo9,compound='right')

checkbox10 = tk.Checkbutton(ventana, text='10)', variable=intchk10)
checkbox10.grid(row=7, column=1)
checkbox10.config(image=photo10,compound='right')



####Ingresar Dominio####
ttk.Label(ventana, text="Ingrese dominio:").grid(row=8,column=0)

ttk.Label(ventana, text="Límite inferior dominio:").grid(row=9,column=0)


ttk.Label(ventana, text="Límite superior dominio:").grid(row=10,column=0)


dominio1 = tk.StringVar()
ttk.Entry(ventana, width=10, textvariable=dominio1).grid(row=9, column=1)
dominio2 = tk.StringVar()
ttk.Entry(ventana, width=10, textvariable=dominio2).grid(row=10, column=1)

tk.Button(ventana, text="Calcular", command= chequearDominios).grid(row=11, column=1)





tk.mainloop()
