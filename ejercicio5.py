#calcular la velocidad (M.C.U)
velocidad,velocidad_angular,radio=0.0,0.0,0.0

#asignacion de valores
velocidad_angular=10
radio=4
#calculo
velocidad=velocidad_angular*radio

#mostrar valores
print("la velocidad _angular es:",velocidad_angular)
print("el radio es:",radio)
print("la velocidad es:",velocidad)

#verificador
velocidad_maxima=(velocidad>400)
print("la velocidad es maxima:",velocidad_maxima)