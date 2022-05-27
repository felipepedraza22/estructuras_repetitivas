"""Ejercicio4
Programa para calcular la cantidad de multiplos de 5 en un rango numerico"""

print ( "-----------------------------------------------------" )
print ( "-----------Multiplos de 5----------------------------" )
print ( "-----------------------------------------------------" )

# aporte

A = int ( input ( " ponga el valor inicial del rango: " ))
B = int ( input ( " Ponga el valor final del rango: " ))

# Procesando

if  A < B :
    rango = 0
    cant_m5 = 0
    while  rango < B :
        rango = rango + 1
        m = rango % 5
        if  m == 0 :
            cant_m5 = cant_m5 + 1
    print ( "Entre"  +  str ( A ) +  "y"  +  str ( B ) +  "hay"  +  str ( cant_m5 ) +  "multiplos de 5" )
else :
    print ( "El valor inicial no puede ser mayor al valor final" )
