#calcular la posicion final
posicion_final,posicion_inicial,velocidad,tiempo=0.0,0.0,0.0,0.0

#asignacion de valores
posicion_inicial=34.6
velocidad=20
tiempo=12

#calculo
posicion_final=posicion_inicial+(velocidad*tiempo)

#mostrar valores
print("la pocicion_inicial es:",posicion_inicial)
print("la velocidad es:",velocidad)
print("el tiempo es:",tiempo)
print("la posicion_final es:",posicion_final)

#verificador
posicion_final_maxima=(posicion_final>420)
print("la posicion final es maxima:",posicion_final_maxima)