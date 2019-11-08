#calcular la potencia efecto joule
potencia,resistencia_electrica,corriente=0.0,0.0,0.0

#asignacion de valores
resistencia_electrica=45
corriente=13

#calculo
potencia=resistencia_electrica*(corriente*corriente)

#mostrar valores
print("la resistencia_electrica es:",resistencia_electrica)
print("la corriente es:",corriente)
print("la potencia es:",potencia)

#verificador
potencia_maxima=(potencia>900)
print("la potencia es maxima:",potencia_maxima)