fin = False

print('***************\n**CALCULADORA**\n***************')
print('MENU\n1)Sumar\n2)Resta\n3)Multiplicación\n4)División\n5)Cerrar')
while not fin:
    opcion = int(input('Introduzca la opción que desee: '))
    if (opcion == 1):
        suma1 = int(input('Introduzca el primer sumando: '))
        suma2 = int(input('Introduzca el segundo sumando: '))
        print('La suma es: ', suma1 + suma2)
    elif (opcion == 2):
        resta1 = int(input('Introduzca el minuendo: '))
        resta2 = int(input('Introduzca el sustraendo: '))
        print('La resta es: ', resta1 - resta2)
    elif (opcion == 3):
        multi1 = int(input('Introduzca el multiplicando: '))
        multi2 = int(input('Introduzca el multiplicador'))
        print('La multiplicación es: ', multi1 * multi2)
    elif (opcion == 4):
        divi1 = int(input('Introduzca el dividendo: '))
        divi2 = int(input('Introduzca el divisor: '))
        print('La división es: ', divi1 / divi2)
    elif (opcion == 5):
        fin = True