#Multiplicar dos numeros sin usar el simbolo de multiplicacion

num1 = 4
num2 = 8
r = 0
for x in range(num2):
    r += num1

print(r)

#Ingresa nombre y apellido y los devuelve alrevez

nombre = 'Raul'
apellido = 'Villamizar'
concatenacion = nombre + ' ' + apellido
print(concatenacion[:: -1])

# Escribir una funcion que encuentre el elemento menor de una lista

lista = [1, 2,5 ,6 , 7 ,14, -12]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor
print('menor', menor)

#Escribir una funcion que evalue si el usuario es mayor de edad

def evaluacion(e):
    if e < 18:
        print('El usuario es menor de edad')
    else: print('Es mayor de edad ')

resultado = evaluacion(19)
print(resultado)


#Escribir una fncion que indique cuanta vocales tiene una palabra

palabra =  'chAncIto'
palabra = palabra.lower()
vocales = 0 

for x in palabra:

    vocales += 1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0

print (vocales)


#Escribir una aplicacion que recciba infinidad de numeros hasta que el usuario diga basta
# y lego calcule la suma de los nueros ingresados
lista = []
print('Ingrese numeros y para salir escriba la palabra basta')
while True: 
    valor = input('Ingrese un valor ---->  ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('El dato fue erroneo ')
            
print(lista)   
resultado = 0
for x in lista:
    resultado += x


print('La suma de su lista es ---->  ',resultado)



#diseñe un programa que escriba el nombre y apellido y lo guarde en un archivo


def agregarNombreArchivo(nombre, apellido):
    c = open('nombreCompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

agregarNombreArchivo('Raul Andres', 'Villamizar')






















