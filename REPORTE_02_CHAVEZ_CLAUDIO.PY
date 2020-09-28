# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#/\/\/\/\/\/\/\/\Variables a usar
lista_Datos=[]
direccion="Exports"
contador=0
monto=0
rutas_contadas=[]
conteo_rutas=[]
conteo_rutas_imp=[]
direccion_2="Imports"
rutas_contadas_2=[]

#/\/\/\/\/\/\/\/\abre el csv
import csv

with open("synergy_logistics_database.csv","r")as archivo_csv:
    lector=csv.reader(archivo_csv)
    next(lector,None)
#/\/\/\/\/\/\/\/\convierte los datos del csv en una lista
    for linea in lector:
        lista_Datos.append(linea)
#/\/\/\/\/\/\/\/\ crea una lista sobre la que trabajamos con una llave para poder distinguirlos

#/\/\/\/\/\/\/\/\ Obtiene una lista con los principales datos de exportaciones


for ruta in lista_Datos:
    if ruta[1] ==direccion:
        ruta_actual=[ruta[2],ruta[3]]
        
        if ruta_actual not in rutas_contadas:
            for movimiento in lista_Datos:
                if ruta_actual == [movimiento[2],movimiento[3]]:
                    contador+=1
                    monto+=int(movimiento[9])
            rutas_contadas.append(ruta_actual)
            
            conteo_rutas.append([ruta[1],ruta[2],ruta[3],contador,monto])
            contador=0
            monto=0

#/\/\/\/\/\/\/\/\ Obtiene una lista con los principales datos de importaciones

for ruta in lista_Datos:
    if ruta[1] ==direccion_2:
        ruta_actual=[ruta[2],ruta[3]]
        
        if ruta_actual not in rutas_contadas_2:
            for movimiento in lista_Datos:
                if ruta_actual == [movimiento[2],movimiento[3]]:
                    contador+=1
                    monto+=int(movimiento[9])
            rutas_contadas_2.append(ruta_actual)
            
            conteo_rutas_imp.append([ruta[1],ruta[2],ruta[3],contador,monto])
            contador=0
            monto=0
            
transportes_valor=[]
transportes_final=[]
transportes=[]
#/\/\/\/\/\/\/\/\ Saca las ganancias por trasnporte


for medio in lista_Datos:        
    transporte=[medio[7]]
    
    if transporte not in transportes:
        transportes.append(transportes)
        
        for tipo in lista_Datos:
            if transporte==[tipo[7]]:
                contador+=1
                monto+=int(tipo[9])
        
        transportes_final.append([medio[7],contador,monto])
        contador=0
        monto=0

consigna_2=[]
for trans in transportes_final:
    if trans not in consigna_2:
        consigna_2.append(trans)


#/\/\/\/\/\/\/\/\ Menu para sacar la informacion en la consola    
menu=[]
bandera=0

menu=input("Seleccione el numero que desea visualizar:  \n 1 Exportaciones mas frecuentes. \n 2 Importaciones mas frecuentes. \n 3 Exportaciones mas valiosas \n 4 Importaciones mas valiosas. \n 5 Monto por transporte. \n opción: ")
if menu=="1":
    bandera+=1
elif menu=="2":
    bandera+=2
elif menu=="3":
    bandera+=3
elif menu=="4":
      bandera+=4
elif menu=="5":
      bandera+=5
elif menu=="6":
      bandera+=6
elif menu=="7":
    bandera+=7
#/\/\/\/\/\/\/\/\llama la primera opcion con la exportaciones mas frecuentes
if bandera==1:
    conteo_rutas.sort(key=lambda x:x[3],reverse=True)
    for indice in range (1,11):
        print ("La ruta: ", conteo_rutas[indice][1]+"-"+conteo_rutas[indice][2], "con un total de:", conteo_rutas[indice][3], "y con un monto de: ", conteo_rutas[indice][4])
#/\/\/\/\/\/\/\/\llama la segunda opcion con las importaciones mas frecuentes
if bandera==2:
        conteo_rutas_imp.sort(key=lambda x:x[3],reverse=True)
        for indice in range (1,12):
            print ("La ruta: ", conteo_rutas_imp[indice][1]+"-"+conteo_rutas_imp[indice][2], "con un total de:", conteo_rutas_imp[indice][3],"y con un monto de: ", conteo_rutas_imp[indice][4])
#/\/\/\/\/\/\/\/\llama la tercera opcion con las exportaciones mas valiosas
if bandera==3:
        conteo_rutas.sort(key=lambda x:x[4],reverse=True)
        for indice in range (1,11):
            print ("La ruta: ", conteo_rutas[indice][1]+"-"+conteo_rutas[indice][2], "con un total de:", conteo_rutas[indice][4]," y una frecuencia de: ",conteo_rutas[indice][3])
#/\/\/\/\/\/\/\/\llama la segunda opcion con las importaciones mas valiosas
if bandera==4:
        conteo_rutas_imp.sort(key=lambda x:x[4],reverse=True)
        for indice in range (1,12):
            print ("La ruta: ", conteo_rutas_imp[indice][1]+"-"+conteo_rutas_imp[indice][2], "con un total de:", conteo_rutas_imp[indice][4]," y una frecuencia de: ",conteo_rutas_imp[indice][3])
#/\/\/\/\/\/\/\/\llama los transportes con los montos que mueven
if bandera==5:
    consigna_2.sort(key=lambda x:x[1],reverse=True)    
    for porte in consigna_2:
        print("Medio de transporte: ",porte[0],"Total: ",porte[2], "con una frecuencia de: ", porte[1])


#/\/\/\/\/\/\/\/\reporte final frecuencia.
# if bandera==6:
#     lista_final.sort(key=lambda x:x[3],reverse=True)
#     for indice in range(1,11):
#         print("La ruta de: ", lista_final[indice][0],"que va de: ", lista_final[indice][1]+"-"+lista_final[indice][2], "con una frecuencia de: ", lista_final[indice][3], "y un monto de: ", lista_final[indice][4])
# #/\/\/\/\/\/\/\/\reporte final valor.
# if bandera==7:
#     lista_final.sort(key=lambda x:x[4],reverse=True)
#     for indice in range(1,11):
#         print("La ruta de: ",lista_final[indice][0],"que va de: ", lista_final[indice][1]+"-"+lista_final[indice][2], "con una frecuencia de: ", lista_final[indice][3], "y un monto de: ", lista_final[indice][4])
