"""Ejercicio3
Programa para calcular la cantidad de numeros pares en un rango numerico"""

print("------------------------------")
print("---cantidad numeros pares-----")
print("------------------------------")

#input
A=int(input("Digite el valor incial del rango: "))
B=int(input("Digite el valor final del rango: "))

#processing
if A<B:
    cant_pares=0
    rango=A
    while rango<B:
        rango=rango+1
        p=rango%2
        if p==0:
            cant_pares=cant_pares+1
    print("La cantidad denumeros pares en este rango es de " +str(cant_pares))
else:
    print("El valor inicial no puede ser mayor al valor final. ")
