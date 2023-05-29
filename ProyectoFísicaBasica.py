import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from math import sqrt

"""Esta clase permite graficar la posición de una estrella y unos planetas asociados a esta,
   se calcula la distancia entre la estrella y los planetas con calcular_distancia y se calcula
   la fuerza gravitacional ejercida por los planetas, por esto se define la masa de estos y 
   de la estrella, si la estrella tiene menor masa que algunos de los planetas se imprime
   un mensaje al usurio advirtiendo que los planetas no orbitan al rededor de esta y 
   no se grafica el sistema planetario. Se asume una orbita circular con centro en la estrella
   usando curvas paramétricas con numpy y graficadas con matplotlib.pyplot."""

class SistemaPlanetario:
    def __init__(self):
        self.estrella_x = 0
        self.estrella_y = 0
        self.estrella_masa = 0
        self.planetas = {}

    def ingresar_estrella(self):
      #Permite ingresar la información de la estrella del sistema planetario.
      #Solicita las coordenadas (x, y) de la estrella y su masa.
        while True:
            try:
                self.estrella_x = float(input("Ingrese la coordenada x de la estrella (en km): "))
                self.estrella_y = float(input("Ingrese la coordenada y de la estrella (en km): "))
                self.estrella_masa = float(input("Ingrese la masa de la estrella (en kg): "))
                break
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

    def ingresar_planeta(self, nombre):

        """
        Permite ingresar la información de un planeta del sistema planetario.
        Solicita las coordenadas (x, y) del planeta y su masa.
        Verifica que las coordenadas no sean iguales a las de la estrella.
        """
        while True:
            try:
                planeta_x = float(input("Ingrese la coordenada x del planeta (en km): "))
                planeta_y = float(input("Ingrese la coordenada y del planeta (en km): "))

                if planeta_x == self.estrella_x and planeta_y == self.estrella_y:
                    print("Error: Las coordenadas del planeta no pueden ser iguales a las de la estrella.¡La estrella desintegra al planeta!")
                    continue

                masa = float(input("Ingrese la masa del planeta (en kg): "))
                self.planetas[nombre] = (planeta_x, planeta_y, masa)
                break
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

    def calcular_distancia(self, x1, y1, x2, y2):
        """
        Calcula la distancia euclidiana entre dos puntos en un plano.
        """
        distancia = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distancia

    def calcular_fuerza_gravitacional(self, masa1, masa2, distancia):
        """
        Calcula la fuerza gravitacional entre dos cuerpos utilizando la ley de gravitación universal.
        """
        constante_gravitacional = 6.67430e-11
        fuerza = (constante_gravitacional * masa1 * masa2) / (distancia ** 2)
        return fuerza

    def imprimir_info_planetas(self):
        """
        Imprime la información de los planetas en el sistema.
        Muestra las coordenadas, distancia a la estrella y fuerza gravitacional de cada planeta.
        """
        print("=== Información de los planetas ===")
        for nombre, planeta in self.planetas.items():
            planeta_x, planeta_y, masa = planeta
            distancia = self.calcular_distancia(self.estrella_x, self.estrella_y, planeta_x, planeta_y)
            fuerza = self.calcular_fuerza_gravitacional(self.estrella_masa, masa, distancia)

            print(f"{nombre}:")
            print(f"Coordenadas: ({planeta_x}, {planeta_y})")
            print(f"Distancia a la estrella: {distancia} km")
            print(f"Fuerza gravitacional de la estrella: {fuerza} N")
            print("==========================")

    def graficar_sistema(self, background_image):
        """
        Grafica el sistema planetario en un plano.
        Muestra la estrella, los planetas y las órbitas de los planetas alrededor de la estrella.
        """
        fig, ax = plt.subplots()
        ax.set_facecolor('black')

        if self.estrella_masa > max([planeta[2] for planeta in self.planetas.values()]):
            ax.scatter(self.estrella_x, self.estrella_y, c="yellow", label="Estrella")
            ax.text(self.estrella_x, self.estrella_y, "Star", color="white", ha='center', va='bottom')

            colisionados = []
            mayor_masa = 0
            planeta_sobreviviente = ""

            for nombre, planeta in self.planetas.items():
                planeta_x, planeta_y, masa = planeta

                color = np.random.rand(3)

                ax.plot([self.estrella_x, planeta_x], [self.estrella_y, planeta_y], linestyle='--', color='gray',
                        alpha=0.8)

                theta = np.linspace(0, 2 * np.pi, 100)
                distancia = self.calcular_distancia(self.estrella_x, self.estrella_y, planeta_x, planeta_y)
                orbita_x = self.estrella_x + distancia * np.cos(theta)
                orbita_y = self.estrella_y + distancia * np.sin(theta)
                ax.plot(orbita_x, orbita_y, color='gray', alpha=0.5)

                if masa > mayor_masa:
                    mayor_masa = masa
                    planeta_sobreviviente = nombre

                for colisionado, datos in self.planetas.items():
                    if colisionado != nombre and colisionado not in colisionados:
                        colisionado_x, colisionado_y, colisionado_masa = datos
                        colisionado_distancia = self.calcular_distancia(planeta_x, planeta_y, colisionado_x,
                                                                        colisionado_y)

                        if colisionado_distancia < 5 or distancia == colisionado_distancia:
                            colisionados.append(nombre)
                            colisionados.append(colisionado)
                            print(f"Colisión detectada entre {nombre} y {colisionado}.")

            if planeta_sobreviviente != "":
                print(f"\nEl planeta sobreviviente es: {planeta_sobreviviente}")

                planeta_x, planeta_y, _ = self.planetas[planeta_sobreviviente]

                ax.scatter(planeta_x, planeta_y, color="red", label=f"{planeta_sobreviviente}")
                ax.text(planeta_x, planeta_y, f"{planeta_sobreviviente}", ha='center', va='bottom', color="white")

            for nombre, planeta in self.planetas.items():
                if nombre not in colisionados and nombre != planeta_sobreviviente:
                    planeta_x, planeta_y, _ = planeta

                    ax.scatter(planeta_x, planeta_y, color=[color], label=f"{nombre}")
                    ax.text(planeta_x, planeta_y, f"{nombre}", ha='center', va='bottom', color="white")

        else:
            print("La estrella no tiene la mayor masa. Los planetas no rotan alrededor de la estrella.")

        plt.xlabel("Coordenada x (km)")
        plt.ylabel("Coordenada y (km)")
        plt.title("Sistema Planetario")

        x_min, x_max = ax.get_xlim()
        y_min, y_max = ax.get_ylim()
        ax.imshow(background_image, extent=[x_min, x_max, y_min, y_max], aspect='auto')

        plt.axis('equal')
        #plt.legend()
        plt.show()


sistema = SistemaPlanetario()
sistema.ingresar_estrella()

num_planetas = int(input("Ingrese el número de planetas: "))
for i in range(num_planetas):
    nombre = input(f"Ingrese el nombre del planeta {i + 1}: ")
    print(f"Ingresando planeta {nombre}:")
    sistema.ingresar_planeta(nombre)

sistema.imprimir_info_planetas()

background_image = mpimg.imread("/content/espacio_2.jpg")  # Reemplaza "ruta_de_la_imagen.jpg" con la ruta de tu imagen

sistema.graficar_sistema(background_image)
