#calcular la capacitancia
capacitancia,carga_electrica,diferencia_de_potencial=0.0,0.0,0.0

#asignacion de valores
carga_electrica=28
diferencia_de_potencial=10

#calculo
capacitancia=carga_electrica/diferencia_de_potencial

#mostrar valores
print("la carga_electrica es:",carga_electrica)
print("la diferencia_de_potencial es:",diferencia_de_potencial)
print("la capacitancia es:",capacitancia)

#verificador
capacitancia_maxima=(capacitancia>400)
print("la capacitancia es maxima:",capacitancia_maxima)