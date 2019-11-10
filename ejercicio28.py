cliente=input("ingrese nombre del cliente:")
mesero=input("ingrese nombre del mesero:")
dulces=int(input("ingrese el numero de dulces:"))
pu_dulces=int(input("ingrese el precio unitario de los dulces:"))
total_dulces=dulces*pu_dulces
queques=int(input("ingrese el numero de queques:"))
pu_queques=int(input("ingrese el precio unitario de los queques:"))
total_de_queques=queques*pu_queques
hamburguesas=int(input("ingrese el numero de hamburguesas:"))
pu_hamburguesas=int(input("ingrese el precio unitario de las hamburguesas:"))
total_hamburguesas=hamburguesas*pu_hamburguesas
consumo=total_dulces+total_de_queques+total_hamburguesas
igv=0.18*consumo
total_pagar=consumo+igv
print("####################FACTURA################")
print("## CLIENTE:",cliente,"  Mesero:",mesero," #")
print("##############################################")
print("# producto        cantidad  P.U  total     #")
print("# dulces:",dulces,"  ",pu_dulces,"  ",total_dulces,"#")
print("# queuqes:",queques,"  ",pu_queques,"  ",total_de_queques,"#")
print("# hamburguesas:",hamburguesas,"  ",pu_hamburguesas,"  ",total_hamburguesas,"#")
print("# consumo:", consumo, "                            #")
print("# IGV:", igv ,"                                    #")
print("# total a pagar:", total_pagar, "                  #")
