"""Ejercicios2
Program para calcular la cantidad de numeros que hay en un rango numerico"""

from re import A


print("----------------------")
print("----Rango numerico----")
print("----------------------")

# input 
A=int(input("Digite el valor inicial de rango"))
B=int(input("Digite el valor final del rango"))
cant_num=0
rango=A+1

# processing
if A>B:
    print("El valor inicial no se puede ser mayor al valor final")
else:
    while rango<B:
        cant_num=cant_num+1
        rango=rango+1
    print(" Entre "+ str(A) +" y" +str(B)+ " hay " +str(cant_num)+ " numeros. ")