import os

montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

import os
archivo = open('clase09_ej3.csv', 'w')
encabezado =list (montañas.keys())
print(encabezado)
linea0=''

for i in encabezado:
    if (i != 'altura'):
        linea0 = linea0 + i + ','
    else:
        linea0 = linea0 + i + '\n'
print(linea0)
archivo.write(linea0)

for j in range(len(montañas['altura'])):
    linea =''
    for i in encabezado:
        linea = linea + str(montañas[i][j]) + ','
    linea = linea[:-1] + '\n'
    archivo.write(linea)

archivo.close()

size = os.path.getsize('clase09_ej3.csv')
print(size)