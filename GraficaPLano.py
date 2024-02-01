import numpy as np
import matplotlib.pyplot as plt

def f(z):
    return np.abs(z)

# Generar discretizacion en polares
R = np.linspace(0.,2,20)
Theta = np.linspace(0.,np.pi/2,20)

x = R*np.cos(Theta)
y = R*np.sin(Theta)

X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

print(Z)

# Calcular los valores de f(z)
W = f(Z)

# Graficar la función en el plano complejo
plt.figure(figsize=(8, 8))
plt.contourf(X, Y, W, 20)
plt.colorbar(label='|f(z)|')
plt.title('Gráfica de la función f(z) = |z| en el plano complejo')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.grid(True)
plt.show()

