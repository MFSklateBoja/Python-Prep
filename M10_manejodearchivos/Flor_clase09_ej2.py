# print("Hello, Python!") 
import datetime
import sys
import os

if len(sys.argv) == 4: 
    temperatura=sys.argv[1]
    humedad =sys.argv[2]
    llovio = sys.argv[3]

    archivo = open('clase09_ej2.csv','a')
    x = datetime.datetime.now()
    marca_de_tiempo = datetime.datetime.timestamp(x)
    marca_de_tiempo = int(marca_de_tiempo)
    # print('Timestamp: ', marca_de_tiempo)       
    linea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + llovio
    print(linea)
    archivo.write(linea +'\n')
    archivo.close()
else:
    print('Ingrese la temperatura, humedad y si llovio o no')       


    # print("Ahora =",x)
    # x = datetime.datetime(2020, 5, 10)
    # print("Fecha fija =",x)

    # fecha_hora = '2022-05-10 12:30:00'
    # objeto_datetime = datetime.datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M:%S')
    # print("objeto datetime =", objeto_datetime)
    # marca_de_tiempo = datetime.datetime.timestamp(objeto_datetime)
    # print("timestamp =", marca_de_tiempo)
    # fecha_hora2 = datetime.datetime.fromtimestamp(marca_de_tiempo)
    # print("fecha hora =", fecha_hora2)