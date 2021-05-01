# Proyecto de diseño de lenguajes
## Diseño de la aplicación
###  \_\_main__
Este script es el encargado de la interfaz del usuario y el encargado de enviar a la clase de escritura de nuevo documento todo lo que debe escribir.

### infixtopostfix
Este script tiene dos tareas principales:
* Verificar que la expresión no tenga errores
* Convertir la expresión a un estado que le convenga al programa

#### Funciones
```sh
def validChar(char):
```
Esta función recibe un carácter y regresa un valor booleano. En caso de que el carácter no sea un operador devolverá un True, sino devolverá un False.

```sh
def getAlphabet(expresion):
```
Recibe una expresión y devuelve un alfabeto (todas las etiquetas) de la expresión.

```sh
def computableExpresion(expresion):
```
Recibe una expresión y la convierte en una expresión que la computadora pueda entenderla.

```sh
def isEmpty(arrayContent):
```
Verifica si una lista está vacía.

```sh
def lastElement(arrayContent):def lessThan(arrayContent,character):
```
Devuelve el ultimo elemento de una lista
```sh
def lessThan(arrayContent,character):
```
Compara la precedencía entre dos caracteres y devuelve True si el segundo carácter tiene un valor menor o igual al primero, sino devuelve un False.
```sh
def infixaPostfix(exp):
```
Recibe una expresión infix y devuelve una expresión postfix
```sh
def convertOperators(expresion):
```
Convierte los operadores “especiales” en sus operaciones equivalentes. ej: a+ = aa*.
```sh
def expresionParaArbol(expresion):
```
Recibe una expresión infix y la convierte a postfix, con la diferencia que le agrega al final la concatenación de #

### fileReader
Script que tiene la función para abrir y analizar ATGs

#### Funciones
```sh
def read_file(file):
```
Esta función recibe el nombre y la extensión del documento que se leerá. Lo que cabe resaltar de esta función es sus cuatro variables importantes:
* Flag: al observar los ATGs se puede concluir que existen tres encabezados importantes los cuales nos indican el inicio de los characters, keywords y tokens. Debido a esto, flag irá cambiando de valor dependiendo de cual fue el último encabezado que se encontró.
* Characters: guardará en una lista todas las líneas que esten debajo del encabezado characters.
* Keywords: guardará en una lista todas las líneas que esten debajo del encabezado keywords.
* Tokens: guardará en una lista todas las líneas que esten debajo del encabezado tokens.
Al finalizar el analisis del ATG, se retornan las listas y el nombre del ATG

### Converter
Esta clase es la encargada de generar los diccionarios de los caracteres, tokens, keywords y además de crear la primera versión de los automatas.
#### Funciones (principales)

```sh
def createCharactersDict(characters):
```
Función encargada de generar el diccionario de los caracteres. 
```sh
#línea que se analiza
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".
#primer elemento que se crea
'letter': {65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}
```
Esta función lo que realiza primero es la busqueda del primer '=' en la línea que se esta analizando, en una variable guarda el nombre (lo que esta antes del igual) y en otra la información relevante (lo que esta después del igual). Convierte todo lo relevante en sus valores ascci y lo guarda dentro de un set. Una vez realizado esto, se guarda en un diccionario el nombre (como key) y los valores ascii (como value). Una vez todos los elementos del diccionarios han sido creados, se retorna al main.

```sh
def createKeywordsDict(charactersDict, keywords):
```
Función encargada de generar el diccionario de los keywords. 
```sh
#línea que se analiza
while = "while".
#primer elemento que se crea
while': 'while'
```
Esta función lo que realiza primero es la busqueda del primer '=' en la línea que se esta analizando, en una variable guarda el nombre (lo que esta antes del igual) y en otra la información relevante (lo que esta después del igual). Una vez finalizada la busqueda, guarda en un diccionario el nombre (como key) y la información relevante (como value). Una vez todos los elementos del diccionarios han sido creados, se retorna al main.
```sh
def createTokensDict(charactersDict, tokens, specialCharacters, special):
```
Esta función es la encargada de crear los diccionarios de los Tokens
```sh
#línea que se analiza
number = digit{digit}.
#primer elemento que se crea
'ident': '0(0|1)*'
```
Esta función lo que realiza primero es la busqueda del primer '=' en la línea que se esta analizando, en una variable guarda el nombre (lo que esta antes del igual) y en otra la información relevante (lo que esta después del igual). Una vez finalizada la busqueda, busca en todos los elementos de charactersDict dentro de la variable con la información relevante. En caso de que encuentre su nombre, cambia el nombre por el indice donde se encuentra en el diccionario para generar una expresión regular similar a la del primer proyecto. Una vez todos los elementos del diccionarios han sido creados, se retorna al main.
```sh
def functionsCreator(tokensDict, KeywordsDict):
```
Recibe el diccionario de tokens y el de keywords. Analiza elemento por elemento dentro del diccionario tokensDict y crea automatas con sus expresiones regulares guardas:

```sh
# Ejemplo de elemento del diccionario
'number' : '0(0|1)*''
# Ejemplo de transiciones de los automatas
[(0, '0', 1), (1, '0', 1), (1, '1', 1)]
# (0, '0', 1) -> su primer y tercer elemento es un nodo y el tercero es lo que se necesita para pasar de un nodo al otro
# Ejemplo de diccionario con los estados de aceptación
{0: False, 1: True}
```

### AFD (primera versión, esta es la misma clase utilizada en el [Primer proyecto](https://github.com/rmonzon98/Dise-o-de-lenguajes))
script que tiene la clase leaf, esta clase se utiliza para representar las hojas de un árbol con la expresión ingresada. Y tiene la función de validar que un carácter sea un carácter válido.
#### Funciones
```sh
def validChar(char):
```
Esta función recibe un carácter y regresa un valor booleano. En caso de que el carácter no sea un operador devolverá un True, sino devolverá un False.
#### clase
class leaf
Representa cada hoja de un árbol sintactico
Tiene los atributos:
* typeLeaf: identifica si la hoja es un operador, carácter o epsilon
* label: guarda su etiqueta en caso de ser tipo carácter o epsilon
* primerapos: primera pos de la hoja
* ultimapos: ultima pos de la hoja
* pos: pos de la hoja:

Tiene las funciones:
* setX: establece el valor de un atributo según el valor que se le paso
* getX: regresa el valor de cada atributo.
* toString: regresa un string con la información de la hoja

### builder
Script encargado de crear el árbol sintáctico y el AFD.
#### Funciones
```sh
def buildAFD(expresion):
```
Recibe una expresión para devolver el AFD.

### AFD fixed (segunda versión del AFD)
#### Clase AFD
```sh
Ejemplo de las transiciones de un automata
{0: {1: ['0']}, 1: {1: ['0', '1']}}
```
##### Funciones principales
```sh
def simulation(expresion):
```
Esta función realiza la función de una expresión. Para esto evalua caracter por caracter de la expresión y devuelve sun False o True dependiendo de si llego a un nodo de aceptación. Para saber si puede pasar a un nodo, evalua el caracter con la función nextMove.
```sh
def nextMove(initialNode, value):
```
Esta función evalua si el caracter (value) se encuentra dentro de la lista que tiene la "etiqueta". En caso de ser así, devuelve un True y el siguiente nodo al que puede dirigirse.

#### Clase Node
Clase encargada de tener la información de de los nodos. Tiene el valor de si es un nodo de aceptación y las transiciones que tiene. 
```sh
#Ejemplo del diccionario con las transiciones que tiene el nodo
1: {1: ['0', '1']}
#Lo que esta fuera de las llaves es el nodo actual, las llaves que estan dentro de los brackets son los nodos a los que puede llegar y los números dentro de la lista son las etiquetas por las cuales pasa el nodo actual para llegar al siguiente nodo.
```
##### Funciones
```sh
def correctTransitions(keys, values, specialCharacters, special):
```
Convierte todos los valores de las etiquetas en los valores ascci que acepta
```sh
#Estado inicial del diccionario
1: {1: ['0', '1']}
#Ejemplo del diccionario con las transiciones en el que se convierte 
1: [{65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}, {48, 49, 50, 51, 52, 53, 54, 55, 56, 57}]
```

### fileWritter
Clase encargada de escribir el scanner. El main le dice a esta clase lo que debe escribir. Primero se creo un scanner a mano para saber la estructua que debía tener.  Luego en el main se escribió línea por línea lo que debía tener el scanner y se lo pasa al fileWritter para que lo escriba. 

### Scanners
Al scanner se le pasa las transiciones y los estados de aceptación para que cree los automatas en base a eso. Lee el .txt y guarda toda su información en una variable como si fuera en un string. Esto para evaluar esa variable, caracter por caracter, e ir buscando tokens. Para esto se van formando strings con los caracteres que hayan sido aceptados. Por ejemplo con el ATG de HexNumber, si encuentra el 12 de primero podría ser un number pero si el siguiente caracter que encuentra es una H. La simulación da que el 12H no es un number pero sí es un Hexnumber. Una vez que haya finalizado de encontrar los tokens, busca entre el arreglo de keywords y si encuentra una keyword (en minusculas), cambia el valor del arreglo de tokens y lo vuelve una keyword.

## Anexos
* Link a vídeo de Youtube de pruebas: https://youtu.be/uWOR17EG8W