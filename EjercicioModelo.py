import numpy as np
import matplotlib.pyplot as plt

class Graficos:
    
    def __init__(self, lista, modelos):
        self.DomX1 = np.array(lista)
        self.DomY1= np.array(lista)

            
        ####Funcion 1####
        def funcion1(lista):
            DomX1 = np.array(lista)
            listay = []
            for i in range(len(lista)):
                x=lista[i]
                y= np.sqrt(5-2*x)+ np.sqrt(3*x+11)   
                listay.append(int(y))
            DomY1= np.array(listay)            
            plt.figure(1)
            plt.plot(DomX1, DomY1)
            plt.title('Gráfico de  f(x)=√(5-2x)+√(3x+11)')
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y', color='#1C2833')
            plt.grid()
        
            

        ####Funcion 2####
        def funcion2(lista):
            DomX1 = np.array(lista)
            listay = []
            for i in range(len(lista)):
                x=lista[i]
                y= np.sin(x)+ np.cos(x)   
                listay.append(int(y))
                DomY1= np.array(listay)            
            plt.figure(2)
            plt.plot(DomX1, DomY1)
            plt.title('Gráfico de  f(x)=sen(x)+cos(x)')
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y', color='#1C2833')
            plt.grid()

            
        
        ####Funcion 3####
        def funcion3(lista):
            DomX1 = np.array(lista)
            listay = []
            for i in range(len(lista)):
                x=lista[i]
                y= (5*x**2-4*x+7)/2   
                listay.append(int(y))
            DomY1= np.array(listay)            
            plt.figure(3)
            plt.plot(DomX1, DomY1)
            plt.title('Gráfico de  f(x)=(5x^2-4x+7)/2')
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y', color='#1C2833')            
            plt.grid()

        
        ####Funcion 4####
        def funcion4(lista):
            DomX1 = np.array(lista)
            listay = []
            for i in range(len(lista)):
                x=lista[i]
                y= -x**2+2*x-2   
                listay.append(int(y))
            DomY1= np.array(listay)            
            plt.figure(4)
            plt.plot(DomX1, DomY1)
            plt.title('Gráfico de  f(x)=-x^2+2x-2')
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y', color='#1C2833')             
            plt.grid()

        
        ####Funcion 5####
        def funcion5(lista):
            DomX1 = np.array(lista)
            listay = []
            for i in range(len(lista)):
                x=lista[i]
                y= np.sqrt(6*x-12)   
                listay.append(int(y))
            DomY1= np.array(listay)            
            plt.figure(5)
            plt.plot(DomX1, DomY1)
            plt.title('Gráfico de  f(x)=√(6x-12)')
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y', color='#1C2833')         
            plt.grid()

        
        ####Funcion 6####
        def funcion6(lista):
            DomX1 = np.array(lista)
            listay = []
            for i in range(len(lista)):
                x=lista[i]
                y= 1/10*(x-5)*(x-3)*(x**2-4)   
                listay.append(int(y))
            DomY1= np.array(listay)            
            plt.figure(6)
            plt.plot(DomX1, DomY1)
            plt.title('Gráfico de  f(x)=1/10(x-5)(x+3)(x^2-4)')
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y', color='#1C2833')              
            plt.grid()

            
        ####Funcion 7####
        def funcion7(lista):
            DomX1 = np.array(lista)
            listay = []
            for i in range(len(lista)):
                x=lista[i]
                y= (x-2)/((x**2)-3) 
                listay.append(int(y))
            DomY1= np.array(listay)
            plt.figure(7)
            plt.plot(DomX1, DomY1)
            plt.title('Gráfico de  f(x)=(x-2)/(x^2-3)')
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y', color='#1C2833')            
            plt.grid()

        
        ####Funcion 8####
        def funcion8(lista):
            DomX1 = np.array(lista)
            listay = []
            for i in range(len(lista)):
                x=lista[i]
                y= (7*x+19)/((x+2)**5) 
                listay.append(int(y))
            DomY1= np.array(listay)            
            plt.figure(8)
            plt.plot(DomX1, DomY1)
            plt.title('Gráfico de  f(x)=(7x+19)/(x+2)^5')
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y', color='#1C2833')              
            plt.grid()

        
        ####Funcion 9#### 
        def funcion9(lista):
            DomX1 = np.array(lista)
            listay = []
            for i in range(len(lista)):
                x=lista[i]
                y= np.log(3-x)/np.log(3) 
                listay.append(int(y))
            DomY1= np.array(listay)            
            plt.figure(9)
            plt.plot(DomX1, DomY1)
            plt.title('Gráfico de  f(x)=log_3⁡(3-x)')
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y', color='#1C2833')       
            plt.grid()

        
        ####Funcion 10####
        def funcion10(lista):
            DomX1 = np.array(lista)
            listay = []
            for i in range(len(lista)):
                x=lista[i]
                y= 3**(4-x) - 9
                listay.append(int(y))
            DomY1= np.array(listay)            
            plt.figure(10)
            plt.plot(DomX1, DomY1)
            plt.title('Gráfico de  f(x)=3^(4-x)-9')
            plt.xlabel('x', color='#1C2833')
            plt.ylabel('y', color='#1C2833')
            plt.grid()
             



                

        funciones=[funcion1,funcion2,funcion3,funcion4,funcion5,funcion6,funcion7,funcion8,funcion9,funcion10]
        for i in modelos:
            funciones[i-1](lista)
        plt.show()
