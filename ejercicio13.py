#calcular el impulso
impulso,fuerza,intervalo_tiempo=0.0,0.0,0.0

#asignacion de valores
fuerza=28
intervalo_tiempo=12

#calculo
impulso=fuerza*intervalo_tiempo

#mostrar valores
print("la fuerza es:",fuerza)
print("la intervalo_tiempo es:",intervalo_tiempo)
print("el impulso es:",impulso)

#verificador
impulso_maximo=(impulso>400)
print("el impulso es maximo:",impulso_maximo)