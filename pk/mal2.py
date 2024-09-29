import numpy as np
import matplotlib.pyplot as plt

# Definer funksjonen K_n(y)
def Kn(y, n):
    return (1 / n) * (np.sin(n * y / 2)**2) / (np.sin(y / 2)**2)

# Generer y-verdier mellom -2π og 2π
y_vals = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
n = 5  # Sett n til for eksempel 5
Kn_vals = Kn(y_vals, n)

# Plot funksjonen
plt.figure(figsize=(8, 6))
plt.plot(y_vals, Kn_vals, label=r'$K_n(y)$ for n=5', color='blue')
plt.title(r'Visualization of $K_n(y)$ for n=5')
plt.xlabel('y')
plt.ylabel(r'$K_n(y)$')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()


