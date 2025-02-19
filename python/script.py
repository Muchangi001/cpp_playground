import numpy as np
import matplotlib.pyplot as plt

# 1. Draw a Line using Parametric Equations
t = np.linspace(0, 1, 100)  # Parameter t from 0 to 1
x_line = 1 + 3 * t  # x = x0 + t * dx (Starting at (1,2) with direction (3,1))
y_line = 2 + 1 * t  # y = y0 + t * dy

# 2. Draw a Parabola (y = x^2)
x_parabola = np.linspace(-5, 5, 100)
y_parabola = x_parabola ** 2

# 3. Draw a Circle (Parametric Equation)
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

# 4. Draw a Bézier Curve (Cubic)
def bezier_curve(P0, P1, P2, P3, n=100):
    t = np.linspace(0, 1, n)
    curve_x = (1 - t)**3 * P0[0] + 3 * (1 - t)**2 * t * P1[0] + 3 * (1 - t) * t**2 * P2[0] + t**3 * P3[0]
    curve_y = (1 - t)**3 * P0[1] + 3 * (1 - t)**2 * t * P1[1] + 3 * (1 - t) * t**2 * P2[1] + t**3 * P3[1]
    return curve_x, curve_y

# Define Control Points for Bézier Curve
P0, P1, P2, P3 = np.array([0, 0]), np.array([2, 4]), np.array([4, 4]), np.array([6, 0])
x_bezier, y_bezier = bezier_curve(P0, P1, P2, P3)

# Plotting
plt.figure(figsize=(10, 6))

# Plot Line
plt.plot(x_line, y_line, label="Line (Parametric)", linestyle='dashed', color='blue')

# Plot Parabola
plt.plot(x_parabola, y_parabola, label="Parabola (y = x^2)", color='red')

# Plot Circle
plt.plot(x_circle, y_circle, label="Circle (Parametric)", color='green')

# Plot Bézier Curve
plt.plot(x_bezier, y_bezier, label="Bézier Curve", color='purple')

# Plot Bézier Control Points
control_x, control_y = zip(P0, P1, P2, P3)
plt.scatter(control_x, control_y, color='black', label="Bézier Control Points")

plt.axhline(0, color='black', linewidth=0.5)  # X-axis
plt.axvline(0, color='black', linewidth=0.5)  # Y-axis
plt.legend()
plt.title("Mathematical Drawing of Lines and Curves")
plt.grid(True)
plt.show()
