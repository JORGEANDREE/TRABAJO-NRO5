cliente=input("ingrese nombre del cliente:")
mesero=input("ingrese nombre del mesero:")
jugo_de_fresa=int(input("ingrese el numero de jugos de fresa:"))
pu_jugos_de_fresa=int(input("ingrese el precio unitario del jugo de fresa:"))
total_jugo_de_fresa=jugo_de_fresa*pu_jugos_de_fresa
jugo_de_piña=int(input("ingrese el numero de jugos de piña:"))
pu_jugo_De_piña=int(input("ingrese el precio unitario de jugos de piña:"))
total_jugo_de_piña=jugo_de_piña*pu_jugo_De_piña
jugo_de_maracuya=int(input("ingrese el numero de jugos de maracuya:"))
pu_jugo_maracuya=int(input("ingrese el precio unitario del jugo de maracuya:"))
total_jugo_de_maracuya=jugo_de_maracuya*pu_jugo_maracuya
consumo=total_jugo_de_fresa+total_jugo_de_piña+total_jugo_de_maracuya
igv=0.18*consumo
total_pagar=consumo+igv
print("####################JUGOS################")
print("## CLIENTE:",cliente,"  MESERO:",mesero," #")
print("##############################################")
print("# producto        cantidad  P.U  total     #")
print("# JUGOS DE FRESA:",jugo_de_fresa,"  ",pu_jugos_de_fresa,"  ",total_jugo_de_fresa,"#")
print("# JUGOS DE PIÑA:",jugo_de_piña,"  ",pu_jugo_De_piña,"  ",total_jugo_de_piña,"#")
print("# JUGOS DE MARACUYA:",jugo_de_maracuya,"  ",pu_jugo_maracuya,"  ",total_jugo_de_maracuya,"#")
print("# consumo:", consumo, "                            #")
print("# IGV:", igv ,"                                    #")
print("# total a pagar:", total_pagar, "                  #")
