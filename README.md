# Portafolio
# Qué es Python?
Python es un lenguaje de programación de propósito general de alto nivel, orientado a objetos, con una semántica dinámica integrada, principalmente para el desarrollo web y de aplicaciones informáticas.
# Qué es una variable?
Una variable esta formada por un espacio en un sistema de almacenamiento, una variable es como una caja en la cual podemos almanecenar o agregar un valor
## Nombrando una variable
La creación de variables se realiza a través de la asignación de un valor a la misma. El operador de asignación en Python es “=“.

Ejemplo del uso y creacion de variable:
```Python
Numero = 13
```
Como se puede apreciar en el ejemplo nombramos a nuestra variable "numero" y le agreamos como valor el numero 13.
Primero debemos asignar la variable luego utilizamos el operador "=" y agregamos el valor de tendra dicha variable, en ese orden especifico.

2do ejemplo:
```Python
Animal = 'perro'
```
## Asignando valores a una variable
Luego de a ver creado y nombrado a la variable, le debemos asignar una variable la cual puede ser del tipo numerica o textual

Algo que hay que tener claro es que al momento de escribir un texto en la variable se debe utilizar las comillas, esto debido a que asi python identifique que es un texto.
```Python
Armas = 'cuchillo'
```
Cuando asignamos un valor numerico no se nesecita usar las comillas.
```Python
Edad = 18
```
## Operadores básicos
Entre los operadores basicos en python encontramos los siguientes y cada uno con su respectivo signo con el cual se representa:

•	suma (+)

•	resta (-)

•	multiplicacion (*)

•	division (/)

•	módulo (%)

Para hacer operaciones con estos operadores logicos debemos asignar valores y dependiendo de la operacion que vayas a realizar, sea resta, division, etc. debemos colocar su signo y al final utilizaremos el "print" acompañado de unos parentesis el cual es una funcion en python, esta funcion se utiliza para imprimir un resultado.

Ejemplo breve de la funcion print:
```Python
print(variable)
```

### Suma
El operador suma tal como su nombre lo indica trata sobre una suma matematica entre los valores asignados.

Ejemplos de como realizar una suma en Python:
```Python
variable = 17 + 18
print(variable)
```

```Python
valor1 = 13
valor2 = 7
suma_valor = valor1 + valor2
print(suma_valor)
```
### Resta
Al igual que la suma, primero asignaremos valores para restarlos

ejemplo de resta en python:
```Python
variable = 6 - 9
print(variable)
```

```python
valor1 = 1
valor2 = 56
resta_valor = valor1 - valor2
print(resta_valor)
```
### Multiplicación
Para la multiplicacion en python utilizaremos *

Ejemplo de multiplicacion en Python:
```Python
variable = 61 * 98
print(variable)
```

```python
valor1 = 43
valor2 = 63
multiplicacion_valor = valor1 * valor2
print(multiplicacion_valor)
```
### División
En la division se utilizara el slash / el cual dara a entender a python que se trata de una division

Ejemplo de division en Python:
```Python
variable = 24 / 12
print(variable)
```

```python
valor1 = 201
valor2 = 2
division_valor = valor1 / valor2
print(division_valor)
```
### Módulo
El módulo es una operación aritmética en la que se divide un valor por otro, y el residuo se devuelve. El simbolo usado para este operador es el % (en Python este simbolo se usa para obtener el módulo de una operación), la aplicación de la operación es igual de simple que el de los anteriores operadores.

Ejemplo de modulo en Python:
```Python
num1=8
num2=30
modulo=num1%num2
print(num1,'%',num2,'=',modulo)
```
# Tipos de datos en Python
Entre los tipos de datos de Python tenemos los siguientes:

•	Numeros enteros (Integer)

•	Numeros de punto flotante (Float)

•	Texto (cadenas de caracteres) (String)

## Integer
En el Integer se utilizara "int" para representarlo en el lenguaje de programacion seguido del int , este tipo de dato se corresponde con los numeros enteros.

Ejemplo de Integer:
```Python
H = int(18)
print(H)
```
## Float
El tipo numérico float permite representar un número positivo o negativo con decimales, es decir, números reales. La función float() devuelve un tipo de datos número entero float.

Si declaramos una variable y le asignamos un valor decimal, por defecto la variable será de tipo float.

Ejemplo de Float:
```Python
f = 0.10093
print(f)       #0.10093
print(type(f)) #<class 'float'>
```
## String
Estos son datos compuestos por caracteres que reprentan textos, estas cadenas de texto se representan mediante comillas.

Ejemplo de String:
```Python
nombre = " Hugo Villacis"
print(nombre)

nombre = 'Hugo Villacis'
print(nombre)
```
## Casting en Python
El casting o cast en python, se trata en convertir un tipo de dato a otro.

Ejemplo de conversión (float a int):
```Python
a = 5.5
a = int(a)
print(a)
print(type(a)) #resultado <class 'int'>
```
## List
Una lista es una estructura de datos en Python, que es una secuencia ordenada de elementos que son mutables o editables. las cadenas se definen como caracteres entre comillas dobles, las listas se definen como valores entre corchetes []

Ejemplo de list:
```Python
list = [ 2,6,8,["dos",seis","ocho"]]
print(list)
```
## Tuple
Tuple o tuplas en python es un conjunto ordenado de elementos que se encuentran encerrados por paréntesis y separados por comas, casi como si fuera una lista.

La tupla es una colección de objetos de Python separados por comas. 

ejemplo de Tuple:
```Python
(1,2,4,5,6,7,8,9,10)
("Yo", "soy", "la","venganza","")
```
## Dictionary
El dato Dictionary es una caracteristica de almacenamiento en la cual podemos asignar valores sean enteron, cadenas, listas, etc.

Ejemplo de Dictionary:
```Python
diccionario = {'Nombre': 'Mickey', 'Edad': 20}
print(diccionario)
```
# Tomando decisiones
Las decisiones en python son importantes al momento de decidir si nuestro programa debe ejecutar una orden, solo si se cumple con alguna condición anterior, para lograr esto en python, hacemos uso de la sentencia if.
## Sentencia if
La estructura if / elif / else es una forma común de controlar el flujo de un programa, lo que te permite ejecutar bloques de código específicos según el valor de algunos datos. Si la condición que sigue a la palabra clave if se cumple o evalúa como verdadera, el bloque de código se ejecutará.

Ejemplo de la sentencia if:
```Python
#Escribir un programa que solicite un valor entero al usuario
#determine si es par o impar
num=int(input("ingrese numero:"))

if (num%2==0):
    print("El numero es par",)
    print(num,"es par")
else:
    print("El numero es impar")  
```
## Ciclo For
En python el ciclo for es una estructua que se  repite una serie de instrucciones por un numero determinado de veces (bucle) estos bucles, como su nombre indica, nos permiten ejecutar una o más líneas de código de forma iterativa.

Ejemplo de For:
```Python
from turtle import position


mascotas = ['gatos','perros','peces','loros']

result = len(mascotas) 

m0 = mascotas[0]
m2 = mascotas[2]

print(result)
print(m2)

for index, mascota in enumerate(mascotas):
    print(index, mascota)

position_peces = 0
for index, mascota in enumerate(mascotas):
    if mascota == "peces":
        position_peces = index

print(" se encontro un pez en la posicion ", position_peces)

```
## Ciclo While
La declaración o ciclo while al igual que el ciclo for, evalúa una condición y luego ejecuta un bloque de código solo si la condición dada por el programa es verdadera, el código seguirá ejecutandose hasa que la condición sea falsa.

Ejemplo de Ciclo While:
```Python
x = 0
while x < 5:
    print('El valor actual es:', x)
    x += 1
```
## Break
Break proporciona la capacidad de cerrar un ciclo cuando se activa una condición externa, se lo representa con "break".

Ejemplo de Break:
```Python
j=0
for i in range (10):
    j+=2
    print ("i;",i,"j:",j)
    if j==10:
        break
```
## Continue
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle.

Ejemplo de Continue:
```Python
x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)

#Salida: 4, 2, 1, 0
```
