#calcular la presion
area,fuerza,presion=0.0,0.0,0.0

#asignacion de valores
area=56.7
fuerza=116.5

#calculo
presion=fuerza*area

#mostrar valores
print("la fuerza es:",fuerza)
print("el area es:",area)
print("la presion es:",presion)

#verificador
presion_maxima=(presion>500)
print("la presion es maxima:",presion_maxima)