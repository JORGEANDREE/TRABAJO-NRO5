#calcular el area de un trapecio
area,base_menor,base_mayor,altura=0,0,0,0

#asignacion de valores
base_menor=40
base_mayor=45
altura=10

#calculo
area=(altura*(base_menor*base_mayor))/2

#mostrar valores
print("la base_menor es:",base_menor)
print("la altura es:",altura)
print("la base_mayor es:",base_mayor)
print("el area es:",area)

#verifiador
area_maxima=(area>9500)
print("el area es maxima:",area_maxima)