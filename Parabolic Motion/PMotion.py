import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Entrada de Datos
v0 = float(input('v0: '))
theta = float(input('theta: '))
x0 = float(input('x0: '))
y0 = float(input('y0: '))
n = int(input('npasos: '))
print("")

# Procedimiento
sigmar = 3.16
pi = math.pi
theta = theta * (pi / 180.0)
grave = 9.81
v0x = v0 * math.cos(theta)
v0y = v0 * math.sin(theta)

xmax = (v0 * v0 / (2.0 * grave)) * math.sin(2.0 * theta)
ymax = (v0 * v0 / (2.0 * grave)) * math.sin(theta) * math.sin(theta)

print("xmax = " + str(xmax))
print("ymax = " + str(ymax))
dt = 0.05

# Inicialización del Tiempo
tiempo = 0.0
cotay = 0.0

# Listas para almacenar datos para la animación
x_data = []
y_data = []

for i in range(n + 1):
    x = x0 + v0x * tiempo
    y = y0 + v0y * tiempo - 0.5 * tiempo * tiempo * grave
    x = x * sigmar
    y = y * sigmar
    if y >= cotay:
        x_data.append(x)
        y_data.append(y)
    tiempo += dt

# Configuración de la figura y el eje
fig, ax = plt.subplots()
ax.set_xlim(0, max(x_data) + 10)
ax.set_ylim(0, max(y_data) + 10)
line, = ax.plot([], [], 'o-', lw=2)

# Función de inicialización para la animación
def init():
    line.set_data([], [])
    return line,

# Función de actualización para la animación
def update(frame):
    line.set_data(x_data[:frame], y_data[:frame])
    return line,

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=len(x_data), init_func=init, blit=True, repeat=False)

# Mostrar la animación
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Tiro Parabólico")
plt.show()
