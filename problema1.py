
import numpy as np
import random
import math
from tabulate import tabulate



def Montecarlo():
    try:
        a1 = float(input("\nValor a1: "))
        b1 = float(input("Valor b1: "))
        a2 = float(input("Valor a2: "))
        b2 = float(input("Valor b2: "))
        n = int(input("Numero de experimentos: "))
    
    except:
        a1 =  -1
        b1 = -1
        a2 =  -1
        b2 = -1
        n = -1
        

    if a1 >= 0 and b1 >= 0 and a2 >= 0 and b2 >= 0 and b1 > a1:
        numerosAleatorios = []
        alturas = []
        areas = []

        for i in range(n):
            xi = random.uniform(a1,b1) #Numero aleatorio dentro del intervalo a1 y b1
            numerosAleatorios.append(xi)
            f_x = lambda x: a1 * math.sin(b1 * x) + a2 * math.sin(b2 * x)
            alturas.append(abs(f_x(xi)))
            area =  ((b2 - a2) / n) * abs(f_x(xi))
            areas.append(area)
    
        estimacionIntegral =  sum(areas)
        experimentosNumber = [i for i in range(n)]
        # Create a list of lists representing an empty table with three columns
        table_data = [["Experimento","Números aleatorio", "Altura", "Área"]]

        # Combine the values into rows and append them to the table
        for val1, val2, val3,val4 in zip(experimentosNumber,numerosAleatorios, alturas, areas):
            table_data.append([val1, val2, val3,val4])

        # Use the tabulate function to format and print the table
        table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
        print(table)
        print(f'\nEstimacion de la integral: {estimacionIntegral}\n')

    elif b1 < a1:
        print("Elige un valor de b1 mayor a a1")

    else:
        print("Ingresa valores validos y numericos para a1,b1,a2,b2")







    





