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
        self.planetas = []

    def ingresar_estrella(self):
        self.estrella_x = float(input("Ingrese la coordenada x de la estrella (en km): "))
        self.estrella_y = float(input("Ingrese la coordenada y de la estrella (en km): "))
        self.estrella_masa = float(input("Ingrese la masa de la estrella (en kg): "))

    def ingresar_planeta(self):
        planeta_x = float(input("Ingrese la coordenada x del planeta (en km): "))
        planeta_y = float(input("Ingrese la coordenada y del planeta (en km): "))

    # Verificar colisión con la estrella
        if planeta_x == self.estrella_x and planeta_y == self.estrella_y:
            print("Las coordenadas ingresadas coinciden con la ubicación de la estrella. El planeta colisiona con la estrella.")
            return

    # Verificar colisión con los planetas existentes
        for planeta in self.planetas:
            x, y, _ = planeta
            if x == planeta_x and y == planeta_y:
                print("Las coordenadas ingresadas ya existen. Los planetas colisionan.")
                return

        masa = float(input("Ingrese la masa del planeta (en kg): "))
        self.planetas.append((planeta_x, planeta_y, masa))

    def calcular_distancia(self, x1, y1, x2, y2):
        distancia = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distancia

    def calcular_fuerza_gravitacional(self, masa1, masa2, distancia):
        constante_gravitacional = 6.67430e-11
        fuerza = (constante_gravitacional * masa1 * masa2) / (distancia ** 2)
        return fuerza

    def imprimir_info_planetas(self):
        print("=== Información de los planetas ===")
        for i, planeta in enumerate(self.planetas):
            planeta_x, planeta_y, masa = planeta
            distancia = self.calcular_distancia(self.estrella_x, self.estrella_y, planeta_x, planeta_y)
            fuerza = self.calcular_fuerza_gravitacional(self.estrella_masa, masa, distancia)

            print(f"Planeta {i+1}:")
            print(f"Coordenadas: ({planeta_x}, {planeta_y})")
            print(f"Distancia a la estrella: {distancia} km")
            print(f"Fuerza gravitacional de la estrella: {fuerza} N")
            print("==========================")

    def graficar_sistema(self, background_image):
        # Verificar si la estrella tiene la mayor masa
        for planeta in self.planetas:
            _, _, masa = planeta
            if masa > self.estrella_masa:
                print("La estrella no tiene la mayor masa. Los planetas no orbitan alrededor de ella.")
                return

        fig, ax = plt.subplots()
        ax.set_facecolor('black')

        ax.scatter(self.estrella_x, self.estrella_y, c="yellow", label="Estrella")
        ax.text(self.estrella_x, self.estrella_y, "Star", color="white", ha='center', va='bottom') #texto encima del punto

        for i, planeta in enumerate(self.planetas):
            planeta_x, planeta_y, masa = planeta

            # Generar color aleatorio
            color = np.random.rand(3)  # Genera tres valores de color RGB aleatorios

            ax.scatter(planeta_x, planeta_y, color=[color], label=f"Planeta {i+1}")
            ax.plot([self.estrella_x, planeta_x], [self.estrella_y, planeta_y], linestyle='--', color='gray', alpha=0.8)

            theta = np.linspace(0, 2 * np.pi, 100)
            distancia = self.calcular_distancia(self.estrella_x, self.estrella_y, planeta_x, planeta_y)
            orbita_x = self.estrella_x + distancia * np.cos(theta)
            orbita_y = self.estrella_y + distancia * np.sin(theta)
            ax.plot(orbita_x, orbita_y, color='gray', alpha=0.5)
            plt.text(planeta_x, planeta_y, f"Planet {i+1}", ha='center', va='bottom', color="white")

        plt.xlabel("Coordenada x (km)")
        plt.ylabel("Coordenada y (km)")
        plt.title("Sistema Planetario")

        # Ajustar la imagen de fondo
        x_min, x_max = ax.get_xlim()
        y_min, y_max = ax.get_ylim()
        ax.imshow(background_image, extent=[x_min, x_max, y_min, y_max], aspect='auto')

        plt.axis('equal')
        #plt.legend()
        plt.show()

# Ejemplo de uso
sistema = SistemaPlanetario()
sistema.ingresar_estrella()

num_planetas = int(input("Ingrese el número de planetas: "))
for i in range(num_planetas):
    print(f"Ingresando planeta {i+1}:")
    sistema.ingresar_planeta()

sistema.imprimir_info_planetas()

# Cargar la imagen de fondo
background_image = mpimg.imread("/content/espacio_2.jpg")  # Reemplaza "ruta_de_la_imagen.jpg" con la ruta de tu imagen

sistema.graficar_sistema(background_image)

