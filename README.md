# Proyecto_Programacion_Fisica
se desarrolla un código aplicando lo visto en el transcurso del semestre


# Sistema planetario
El código es un script de Python que crea una clase llamada SistemaPlanetario para simular y visualizar un sistema planetario. Utiliza la biblioteca matplotlib para graficar los planetas del sistema y sus órbitas.

El script solicita al usuario que ingrese los detalles de la estrella y los planetas del sistema, incluyendo sus coordenadas y masas. Luego calcula las fuerzas gravitacionales entre la estrella y cada planeta e imprime la información de cada planeta.

Finalmente, el script visualiza el sistema graficando la estrella, los planetas y sus órbitas en un fondo negro con una imagen del espacio proporcionada.

descripción de lo que hace cada función en el código:

1)__init__(self): Es el método constructor de la clase SistemaPlanetario. Inicializa los atributos de la clase, como las coordenadas de la estrella y un diccionario vacío para almacenar los planetas.

2)ingresar_estrella(self): Solicita al usuario que ingrese las coordenadas x e y de la estrella, así como su masa. Almacena estos valores en los atributos correspondientes de la clase.

3)ingresar_planeta(self, nombre): Solicita al usuario que ingrese las coordenadas x e y, así como la masa de un planeta específico. Almacena estos valores en el diccionario de planetas, con el nombre del planeta como clave y una tupla de coordenadas x, y y masa como valor.

4)calcular_distancia(self, x1, y1, x2, y2): Calcula la distancia entre dos puntos en un plano utilizando la fórmula de la distancia euclidiana. Recibe las coordenadas x e y de dos puntos y devuelve la distancia entre ellos.

5)calcular_fuerza_gravitacional(self, masa1, masa2, distancia): Calcula la fuerza gravitacional entre dos cuerpos utilizando la ley de gravitación universal de Newton. Recibe las masas de los dos cuerpos y la distancia entre ellos, y devuelve la fuerza gravitacional resultante.

6)imprimir_info_planetas(self): Imprime la información de cada planeta en el sistema. Calcula la distancia entre cada planeta y la estrella, así como la fuerza gravitacional entre la estrella y el planeta. Muestra esta información en la consola.

7)graficar_sistema(self, background_image): Grafica el sistema planetario utilizando la biblioteca matplotlib. Crea una figura y un conjunto de ejes, establece el fondo en negro y grafica la estrella, los planetas y sus órbitas. También detecta colisiones entre planetas y muestra el planeta sobreviviente. Finalmente, muestra el gráfico resultante.

Estas funciones definen el comportamiento del sistema planetario y permiten ingresar información, realizar cálculos y visualizar el sistema de manera gráfica.


# Simulador de Fuerza Eléctrica entre Cargas

Este programa simula la interacción de cargas eléctricas y calcula la fuerza eléctrica total sobre una carga de prueba.

## Requisitos
- Python 3.x
- Biblioteca matplotlib

## Clase `Carga`

La clase `Carga` representa una carga eléctrica con los siguientes atributos:

- `nombre` (str): El nombre de la carga.
- `carga` (float): El valor de la carga en Coulombs.
- `x` (float): La coordenada x de la carga en centímetros.
- `y` (float): La coordenada y de la carga en centímetros.

## Función `calcular_fuerza_electrica`

La función `calcular_fuerza_electrica(carga_prueba, cargas)` calcula la fuerza eléctrica total sobre una carga de prueba debido a otras cargas. Recibe como argumentos:

- `carga_prueba` (Carga): La carga de prueba.
- `cargas` (list): Lista de objetos de tipo Carga que representan las otras cargas.

Retorna:

- `float`: La fuerza eléctrica total sobre la carga de prueba en Newtons.

## Función `graficar_cargas`

La función `graficar_cargas(cargas, carga_prueba)` grafica las cargas y la carga de prueba en un plano cartesiano. Recibe como argumentos:

- `cargas` (list): Lista de objetos de tipo Carga.
- `carga_prueba` (Carga): La carga de prueba.

## Función `ingresar_cargas`

La función `ingresar_cargas()` solicita al usuario ingresar las cargas y sus coordenadas. Retorna:

- `list`: Lista de objetos de tipo Carga.

## Función `verificar_cargas`

La función `verificar_cargas(cargas)` verifica si las cargas tienen las mismas coordenadas. Recibe como argumento:

- `cargas` (list): Lista de objetos de tipo Carga.

Retorna:

- `bool`: True si todas las cargas tienen coordenadas distintas, False de lo contrario.

## Función `info_cargas`

La función `info_cargas(cargas, carga_prueba)` imprime la información de cada carga, incluyendo sus coordenadas, valor en Coulombs, distancia a la carga de prueba y fuerza eléctrica sobre esta. Recibe como argumentos:

- `cargas` (list): Lista de objetos de tipo Carga.
- `carga_prueba` (Carga): La carga de prueba.

## Función `main`

La función `main()` es la función principal que ejecuta el programa. Solicita al usuario ingresar el valor y las coordenadas de la carga de prueba, luego pide ingresar el número de cargas y sus respectivas coordenadas y valores en Coulombs. Imprime la información de las cargas y la fuerza total sobre la carga de prueba. También muestra una gráfica que representa la distribución de las cargas y la carga de prueba en un plano cartesiano.

## Uso

1. Ejecuta el programa en un entorno de Python.
2. Se te solicitará ingresar el valor y las coordenadas de la carga de prueba.
3. Luego, se te pedirá ingresar el número de cargas y sus respectivas coordenadas y valores en Coulombs.
4. La información de las cargas, incluyendo la distancia y la fuerza eléctrica sobre la carga de prueba, se imprimirá en la consola.
5. Se abrirá una gráfica que muestra la distribución de las cargas y la carga de prueba en un plano cartesiano.

## Contribución

Siéntete libre de contribuir a este proyecto realizando mejoras o agregando nuevas funcionalidades. ¡Tus contribuciones son bienvenidas!


