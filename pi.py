#programa para calcular pi
numerador=4
denominador=1
pi=0
operador=1
iteraciones=int(input("Cuantas iteraciones: "))
for valor in range(iteraciones):
    #print(valor)1
    pi += operador * (numerador / denominador)
    denominador += 2 #// El denominador aumenta de 2 en 2
    operador *= -1   #// Alternamos operador
print(pi)
