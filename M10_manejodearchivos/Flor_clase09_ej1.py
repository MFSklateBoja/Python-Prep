import sys
# print(len(sys.argv))
if len(sys.argv) != 4:
    print('La cantidad de argumentos debe ser 4')
else:
    print(f'El primer parametro es {sys.argv[1]}, el 2do {sys.argv[2]} y el 3ero {sys.argv[3]}.')

