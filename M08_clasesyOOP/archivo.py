import sys
sys.path.append(r'C:\Users\flore\OneDrive\Escritorio\Python-Prep\M07_funciones')
import Prep_Course_Homework_07_Resuelto as HW_07


class Funciones:
    def __init__(self,lista_numeros):
        if (type(lista_numeros) != list):
            self.lista_numeros=[]
            raise ValueError('Por favor ingrese una lista')
        else: 
            self.lista_numeros = lista_numeros
        
    def Verificar_primo(self):
        primos=[]
        for i in self.lista_numeros:
            #print(HW_07.verifica_primo(i))              
            if HW_07.verifica_primo(i):
                print(f'{i} es primo')
                primos.append(i)
        return primos
    def Valormodal(self):
        print(HW_07.valor_modal(self.lista_numeros))
        return (HW_07.valor_modal(self.lista_numeros))

    def Conversion(self, unidad1, unidad2):
        nueva_lista=[]
        aceptados=['celsius', 'kelvin', 'farenheit']
        if ((unidad1 not in aceptados) or (unidad2 not in aceptados)):
            print('Los parametros esperados son: ', aceptados)
        else:
            for i in self.lista_numeros:
                print(HW_07.conversion_grados(i,unidad1,unidad2))
                nueva_lista.append(HW_07.conversion_grados(i,unidad1,unidad2))
        return nueva_lista
    
    def Factorial_(self):
        factorial = []
        for i in self.lista_numeros:
            print(HW_07.factorial(i))
            factorial.append(HW_07.factorial(i))
        return factorial