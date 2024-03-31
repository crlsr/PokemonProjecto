'''
Este modulo es dedicdo a la creación de todas las funciones creadas para darle el funcionamiento a nuestro programa
En este apartados abran aspectos como validaciones, etc...
'''
#Importaciones de librerias necesarias para la creación de funciones


#Función para validar entradas númericas definidas en un rango númerico
def validation(val, minval, maxval): 
    while val<minval or val>maxval:
        try:
            val = int(input (f'Error, recuerde que los valores que puede elegir van desde {minval} hasta {maxval}: '))
        except ValueError:
            print('Valor incorrecto, solo se admiten números')
    return val


#Función para validar valores iniciales (restringiendo el tipo de dato ue puede llegar a ser)
def int_validatión(string):
    while True:
        try: 
            valor = int(input(string))
            return valor 
        except ValueError:
            print('Error, valor incorrecto, solo se admiten números.')
            


#Combinación que permite verificar un valor y a la vez validarlo entre un conjunto numerico definido.
#x = validation(int_validatión(''), 1, 2) 