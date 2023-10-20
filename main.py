from problema1 import *
from problema2 import *


def main():

    print("\nExamen Argumentativo 2 MA2004B")
    print("\nDocente: Dr. Rafael Muñoz Sánchez")
    print("\nAlumno Rubén Darío Castro Terrazas - A00833945")
    flag = True
    
    while flag:

        print("\n\n\t1.- Problema 1")
        print("\n\t2.- Problema 2")
        print("\n\t3.- Salir del programa")

        try:
            opcion = int(input("\n¿Qué opción decides ejecutar? "))
        except:
            opcion = -1
        
        if opcion == 1:
            Montecarlo()

        elif opcion == 2:
            Simulacion()
        
        elif opcion == 3:
            flag =  False
        
        else:
            print("\nIntroduce una opcion válida")

        




main()