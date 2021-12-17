import sys
import math
import time

# esercizio con liste

lista1=[]
print("lista vuota: ", lista1)

lista2=['Io', 'sono', 'Letizia']
print("Stampo alcuni elementi della lista: ")
print(lista2[1], lista2[2])
print(lista2[0])
print(lista2[-1])

lista3=range(1,10,2)
print("lista a passi di 2 creata con la funzione range: ", lista3[0], lista3[1], lista3[2], lista3[3], lista3[4])

lista4=[el*2 for el in lista3]
print("lista precedente, moltiplicata per due: ", lista4)
lista4.reverse()
print("lista precedente, al contrario: ", lista4)
lista4.reverse()
lista4.append(20)
lista4.append(22)
lista4.append(24)
print("lista estesa: ", lista4)

# esercizio efficienza

l1=list(range(10000000))
l2=list(range(100000))
t1=time.time()
l3=l1+l2

print("tempo di esecuzione della somma: ", t1-time.time())

