#calcular el area de un rombo
area,diagonal_menor,digonal_mayor,=0.0,0,0

#asignacion de valores
diagonal_menor=45
digonal_mayor=69

#calculo
area=(digonal_mayor*diagonal_menor)/2

#mostrar valores
print("la diagonal_menor es:",diagonal_menor)
print("la diagonal_mayor es:",digonal_mayor)
print("el area es:",area)

#verificador
area_maxima=(area>400)
print("el area es maxima:",area_maxima)