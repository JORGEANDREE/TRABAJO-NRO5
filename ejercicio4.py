#calcular la posicion final
posion_final,posion_inicial,velocidad,tiempo=0.0,0.0,0.0,0.0

#asignacion de valores
posion_inicial=34.6
velocidad=20
tiempo=12

#calculo
posion_final=posion_inicial+(velocidad*tiempo)

#mostrar valores
print("la pocicion_inicial es:",posion_inicial)
print("la velocidad es:",velocidad)
print("el tiempo es:",tiempo)
print("la posicion_final es:",posion_final)

#verificador
posicion_final_maxima=(posion_final>420)
print("la posicion final es maxima:",posicion_final_maxima)