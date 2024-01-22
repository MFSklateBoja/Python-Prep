import sys
sys.path.append(r'C:\Users\flore\OneDrive\Escritorio\Python-Prep\M07_funciones')
import Prep_Course_Homework_07_Resuelto as HW_07

class Funciones:
    def __init__(self,Lista_numeros):
        self.lista_numeros = Lista_numeros

    def Verificar_primo(self):
        for i in self.lista_numeros:
            #print(HW_07.verifica_primo(i))              
            if HW_07.verifica_primo(i):
                print(f'{i} es primo')
    def Valormodal(self):
        print(HW_07.valor_modal(self.lista_numeros))

    def Conversion(self, unidad1, unidad2):
        for i in self.lista_numeros:
            print(HW_07.conversion_grados(i,unidad1,unidad2))
    
    def Factorial_(self):
        for i in self.lista_numeros:
            print(HW_07.factorial(i))