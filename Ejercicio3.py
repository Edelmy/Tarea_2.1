import numpy as np
import matplotlib.pyplot as plt
#Chay Dzul Edelmy
# Definir la función
def f(x):
    return np.cos(x) - x

# Algoritmo del método de bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en el intervalo dado.")
        return None

    iteraciones = []
    errores_abs = []
    errores_cuad = []
    errores_rel = []
    c_old = a

    print("\nIteraciones del Método de Bisección:")
    print("Iter |       a       |       b       |       c       |      f(c)      |     Error Abs     |     Error Rel     |     Error Cuad     ")
    print("-" * 120)

    for i in range(max_iter):
        c = (a + b) / 2
        iteraciones.append(c)

        # Cálculo de errores
        error_abs = abs(c - c_old) #Se calcula el error absoluto como la diferencia absoluta entre el punto medio actual c y el punto medio de la iteración anterior
        error_cuad = error_abs**2 #Se calcula el error cuadrático como el cuadrado del error absoluto
        error_rel = error_abs / abs(c) if c != 0 else 0 #Se calcula el error relativo como el error absoluto dividido por el valor absoluto del punto medio actual
        #Se añaden los errores calculados a las listas 
        errores_abs.append(error_abs)
        errores_cuad.append(error_cuad)
        errores_rel.append(error_rel)

        print(f"{i+1:4d} | {a:.8f} | {b:.8f} | {c:.8f} | {f(c):.8f} | {error_abs:.8e} | {error_rel:.8e} | {error_cuad:.8e}")
#Se verifica si el valor absoluto de f(c) o el error absoluto es menor que la tolerancia tol. Si es así, el bucle se interrumpe porque se ha encontrado una raíz con la precisión deseada
        if abs(f(c)) < tol or error_abs < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c

    return iteraciones, errores_abs, errores_cuad, errores_rel

# Parámetros iniciales
a, b = 0, 1 # Se cambia el intervalo
iteraciones, errores_abs, errores_cuad, errores_rel = biseccion(a, b)

# Crear la figura
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica de la función y la convergencia de iteraciones
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

ax[0].plot(x, y, label=r'$f(x) = cos (x)-x', color='b')
ax[0].axhline(0, color='k', linestyle='--', linewidth=1)  # Línea en y=0
ax[0].scatter(iteraciones, [f(c) for c in iteraciones], color='red', label='Iteraciones')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title("Convergencia del Método de Bisección")
ax[0].legend()
ax[0].grid()

# Gráfica de errores
ax[1].plot(range(1, len(errores_abs) + 1), errores_abs, marker='o', linestyle='-', label="Error Absoluto", color='r')
ax[1].plot(range(1, len(errores_cuad) + 1), errores_cuad, marker='s', linestyle='--', label="Error Cuadrático", color='g')
ax[1].plot(range(1, len(errores_rel) + 1), errores_rel, marker='^', linestyle='-.', label="Error Relativo", color='b')
ax[1].set_yscale("log")  # Escala logarítmica
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Errores")
ax[1].set_title("Errores en cada Iteración")
ax[1].legend()
ax[1].grid()

# Guardar la figura
plt.savefig("biseccion_errores.png", dpi=300)
plt.show()