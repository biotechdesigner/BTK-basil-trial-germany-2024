import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
edades = [25, 30, 35, 40, 45, 50, 55, 60]
ingresos = [30000, 45000, 60000, 75000, 90000, 105000, 120000, 135000]
tallas = [1.65, 1.70, 1.75, 1.80, 1.85, 1.90, 1.95, 2.00]

# Crear una figura y ejes
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

# Graficar la distribución de edades
axes[0].hist(edades, bins=8, edgecolor='black')
axes[0].set_title('Distribución de Edades')
axes[0].set_xlabel('Edad')
axes[0].set_ylabel('Frecuencia')

# Graficar la distribución de ingresos
axes[1].hist(ingresos, bins=8, edgecolor='black')
axes[1].set_title('Distribución de Ingresos')
axes[1].set_xlabel('Ingreso')
axes[1].set_ylabel('Frecuencia')

# Graficar la distribución de tallas
axes[2].hist(tallas, bins=8, edgecolor='black')
axes[2].set_title('Distribución de Tallas')
axes[2].set_xlabel('Talla')
axes[2].set_ylabel('Frecuencia')

# Ajustar el espaciado entre subplots
plt.subplots_adjust(wspace=0.5)

# Mostrar el gráfico
plt.show()