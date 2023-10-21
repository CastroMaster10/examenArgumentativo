import numpy as np
import random
import math
from tabulate import tabulate
import statistics

# Assuming 'my_list' is your list
my_list = [1, 2, 3, 4, 5]

mean = statistics.mean(my_list)

print(mean)


def Simulacion():
    try:
        pasos = int(input("\nNumero de pasos a realizar: "))
        dim =  int(input("Numero de dimensiones (1/2): "))
        n = int(input("Numero de experimentos: "))

    except:
        n = -1
        pasos = -1
        dim = -1

    if n > 0 and dim == 1 and pasos > 0:
        p1 = 0.5 #umbral de probabilidad para ver donde avanza
        table_data = [["Experimento","Distancia Máxima", "Última distancia"]]

        for i in range(n):
            coordenada = 0
            distancias = [] #lista de distancias desde el punto de origen
            for j in range(pasos):
                xi =  random.uniform(0,1)
                if xi >= p1:
                    coordenada += 1
                else:
                    coordenada -= 1
                distancias.append(abs(coordenada))
            
            new_row = [i,max(distancias),distancias[-1]]
            table_data.append(new_row)
        
        table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
        print(table)

    if n > 0 and pasos > 0 and dim == 2:
        p1 = 0.5
        p2  = 0.5
        table_data = [["Experimento","Distancia Máxima", "Última distancia"]]
        distanciasMax = []

        for i in range(n):
            coordenadas = [0,0] #Coordenadas de origen
            distancias = []
            for j in range(pasos):
                xi = random.uniform(0,1)
                yi = random.uniform(0,1)

                #eje horizontal
                if xi >= p1:
                    coordenadas[0] += 1
                else:
                    coordenadas[0] -= 1
                
                if yi >= p2:
                    coordenadas[1] += 1
                else:
                    coordenadas[1] -= 1
                
                distancia = math.sqrt(coordenadas[0] ** 2 + coordenadas[1] ** 2) #distancia euclediana
                distancias.append(distancia)

            
            new_row = [i,max(distancias),distancias[-1]]
            table_data.append(new_row)
            distanciasMax.append(max(distancias))
        

        table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
        print(table)
        print(f'Distancia maxima promedio dentro de los {n} experimentos: {statistics.mean(distanciasMax)}')

    elif dim > 2 or dim <= 0:
        print("Introduzca un numero valido de dimensiones (1 o 2)")
    else:
        print("Introduzca un numero entero para el numero de experimentos")

