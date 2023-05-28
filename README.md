# Proyecto_Programacion_Fisica
se desarrolla un código aplicando lo visto en el transcurso del semestre


# Sistema planetario
El código que proporcionaste es un script de Python que crea una clase llamada SistemaPlanetario para simular y visualizar un sistema planetario. Utiliza la biblioteca matplotlib para graficar los planetas del sistema y sus órbitas.

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
