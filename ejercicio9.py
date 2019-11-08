#calcular el area de un pentagono
area,base,apotema=0.0,0,0

#asignacion de valores
base=57
apotema=18

#calculo
area=(base*apotema)/2

#mostrar valores
print("la base es:",base)
print("la apotema es:",apotema)
print("el area es:",area)

##verificador
area_maxima=(area>200)
print("el area es maxima:",area_maxima)