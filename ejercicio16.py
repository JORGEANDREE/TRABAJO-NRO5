#calcular la capacidad termica
capacidad_termica,masa,calor_especifio=0.0,0.0,0.0

#asignacion de valores
masa=14
calor_especifio=24

#calculo
capacidad_termica=masa*calor_especifio

#mostrar valores
print("la masa es:",masa)
print("el calor_especifico es:",calor_especifio)
print("la capacidad_termica es:",capacidad_termica)

#verificador
capacidad_termica_maxima=(capacidad_termica>500)
print("la capacidad termica es maxima:",capacidad_termica_maxima)