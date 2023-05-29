# Simulador de Sistema Planetario

Esta clase representa un sistema planetario y proporciona métodos para ingresar la información de la estrella y los planetas en el sistema, calcular distancias y fuerzas gravitacionales, imprimir información de los planetas y graficar el sistema en un plano.
## Clase `SistemaPlanetario`

## Requisitos
- Python 3.x
- Biblioteca matplotlib
### Método `__init__()`

El constructor de la clase. Inicializa los atributos de la instancia `SistemaPlanetario`, incluyendo las coordenadas y masa de la estrella, así como un diccionario para almacenar los planetas.

### Método `ingresar_estrella()`

Permite ingresar la información de la estrella del sistema planetario. Solicita las coordenadas (x, y) de la estrella y su masa.

### Método `ingresar_planeta(nombre)`

Permite ingresar la información de un planeta en el sistema planetario. Solicita las coordenadas (x, y) del planeta y su masa. Verifica que las coordenadas no sean iguales a las de la estrella.

### Método `calcular_distancia(x1, y1, x2, y2)`

Calcula la distancia euclidiana entre dos puntos en un plano. Toma como parámetros las coordenadas (x, y) de dos puntos y devuelve la distancia entre ellos.

### Método `calcular_fuerza_gravitacional(masa1, masa2, distancia)`

Calcula la fuerza gravitacional entre dos cuerpos utilizando la ley de gravitación universal. Toma como parámetros las masas de los dos cuerpos y la distancia entre ellos, y devuelve la fuerza gravitacional.

### Método `imprimir_info_planetas()`

Imprime la información de los planetas en el sistema. Muestra las coordenadas, la distancia a la estrella y la fuerza gravitacional de cada planeta.

### Método `graficar_sistema(background_image)`

Grafica el sistema planetario en un plano. Muestra la estrella, los planetas y las órbitas de los planetas alrededor de la estrella. Toma como parámetro una imagen de fondo para el plano.

## Uso

1. Ejecuta el programa en un entorno de Python.
2. Se te solicitará ingresar el valor y las coordenadas de la estrella.
3. Luego, se te pedirá ingresar el número de plamteas y sus respectivas coordenadas ($Km$) y valores de masa en ($kg$).
4. La información de los planetas, incluyendo la distancia y la fuerza gravitacional de la estrella, se imprimirá en la consola.
5. Se abrirá una gráfica que muestra las orbitas de los plaetas (asumidas como circulares) y la estrella en un plano cartesiano.



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


# Tiro Parabólico

Este proyecto implementa un simulador de tiro parabólico utilizando la biblioteca `matplotlib` en Python. Permite calcular y visualizar la trayectoria de un proyectil lanzado con un ángulo y una velocidad inicial determinados.

## Funciones y métodos

### Clase `TiroParabolico`

La clase `TiroParabolico` representa un tiro parabólico y contiene los siguientes métodos:

#### `__init__(altura, velocidad_inicial, angulo)`

Inicializa los atributos de la clase `TiroParabolico`.

- Parámetros:
  - `altura` (float): Altura inicial del proyectil.
  - `velocidad_inicial` (float): Velocidad inicial del proyectil.
  - `angulo` (float): Ángulo de lanzamiento del proyectil.

#### `calcular_tiempo_vuelo()`

Calcula el tiempo total de vuelo del proyectil.

- Retorna:
  - float: Tiempo total de vuelo del proyectil.

#### `calcular_alcance_horizontal()`

Calcula el alcance horizontal del proyectil.

- Retorna:
  - float: Alcance horizontal del proyectil.

#### `calcular_altura_maxima()`

Calcula la altura máxima alcanzada por el proyectil.

- Retorna:
  - float: Altura máxima alcanzada por el proyectil.

#### `calcular_posicion(tiempo)`

Calcula la posición (x, y) del proyectil en un tiempo dado.

- Parámetros:
  - `tiempo` (float): Tiempo en el que se desea conocer la posición.

- Retorna:
  - tuple: Posición (x, y) del proyectil en el tiempo dado.

### Decorador `verificar_valores_numericos`

El decorador `verificar_valores_numericos` verifica que los argumentos de una función sean valores numéricos.

- Parámetros:
  - `func` (function): Función a decorar.

- Retorna:
  - function: Función decorada.

### Función `main(altura, velocidad_inicial, angulo)`

La función principal `main` realiza los cálculos y muestra la animación del tiro parabólico.

- Parámetros:
  - `altura` (float): Altura inicial del proyectil.
  - `velocidad_inicial` (float): Velocidad inicial del proyectil.
  - `angulo` (float): Ángulo de lanzamiento del proyectil.

- Retorna:
  - str: Representación en formato de video HTML5 de la animación del tiro parabólico.

### Loop de entrada de datos

Se utiliza un loop de entrada de datos para asegurar que se ingresen valores numéricos válidos para la altura inicial, velocidad inicial y ángulo de lanzamiento del proyectil.

## Uso

Para utilizar el simulador de tiro parabólico, siga los siguientes pasos:

1. Ingrese la altura inicial (en metros).
2. Ingrese la velocidad inicial (en m/s).
3. Ingrese el ángulo de lanzamiento (en grados).

El programa calculará los resultados del tiro parabólico, imprimirá los valores y generará un video animado de la trayectoria del proyectil. El video se guardará en el archivo `trayectoria.mp4` y se mostrará en el navegador web.

**Nota:** Asegúrese de tener instalada la biblioteca `matplotlib` y el códec de video `ffmpeg` para generar y guardar el video de la animación.

¡Disfrute del simulador de tiro parabólico!



## Contribución

Siéntete libre de contribuir a este proyecto realizando mejoras o agregando nuevas funcionalidades. ¡Tus contribuciones son bienvenidas!


