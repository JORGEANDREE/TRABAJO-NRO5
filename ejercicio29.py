cliente=input("ingrese nombre del cliente:")
vendedor=input("ingrese el nombre del vendedor:")
celular=int(input("ingrese el numero de celulares:"))
pu_celular=int(input("ingrese el precio unitario del celular:"))
total_celular=celular*pu_celular
consumo=celular*pu_celular
igv=0.18*consumo
total_pagar=consumo+igv
print("####################BOLETA################")
print("## CLIENTE:",cliente,"vendedor:",vendedor, "#")
print("##############################################")
print("# producto        cantidad  P.U  total     #")
print("# celular:",celular,"  ",pu_celular,"  ",total_celular,"#")
print("# consumo:", consumo, "                            #")
print("# IGV:", igv ,"                                    #")
print("# total a pagar:", total_pagar, "                  #")
