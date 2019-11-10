cliente=input("ingrese nombre del cliente:")
mesero=input("ingrese nombre del mesero:")
arroz_con_pato=int(input("ingrese el numero de platos de arroz con pato:"))
pu_arrroz_con_pato=int(input("ingrese elprecio unitario del arroz con pato:"))
total_arroz_con_pato=arroz_con_pato*pu_arrroz_con_pato
jarra_de_chicha=int(input("ingrese el numero de jarras de chicha:"))
pu_jarra_de_chicha=int(input("ingrese el precio unitario de jarras de chicha:"))
total_jarras_de_chicha=jarra_de_chicha*pu_jarra_de_chicha
gelatina=int(input("ingrese el numero de gelatinas:"))
pu_gelatina=int(input("ingrese el precio unitario de las gelatinas:"))
total_gelatinas=gelatina*pu_gelatina
consumo=total_arroz_con_pato+total_jarras_de_chicha+total_gelatinas
igv=0.18*consumo
total_pagar=consumo+igv
print("####################RESTAURANT################")
print("## CLIENTE:",cliente,"  MESERO:",mesero," #")
print("##############################################")
print("# producto        cantidad  P.U  total     #")
print("# arroz con pato:",arroz_con_pato,"  ",pu_arrroz_con_pato,"  ",total_arroz_con_pato,"#")
print("# jarra de chicha:",jarra_de_chicha,"  ",pu_jarra_de_chicha,"  ",total_jarras_de_chicha,"#")
print("# gelatina:",gelatina,"  ",pu_gelatina,"  ",total_gelatinas,"#")
print("# consumo:", consumo, "                            #")
print("# IGV:", igv ,"                                    #")
print("# total a pagar:", total_pagar, "                  #")
