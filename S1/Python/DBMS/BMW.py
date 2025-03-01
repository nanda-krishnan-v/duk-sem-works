import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_aspect('equal')

# Create outer black circle
outer_circle = plt.Circle((0.5, 0.5), 0.45, color='black', lw=2, fill=True)
ax.add_artist(outer_circle)

# Create inner white circle
inner_circle = plt.Circle((0.5, 0.5), 0.4, color='white', lw=2, fill=True)
ax.add_artist(inner_circle)

# Define the quadrants and add colors
theta1 = np.linspace(np.pi/2, np.pi, 100)
x1 = 0.5 + 0.4 * np.cos(theta1)
y1 = 0.5 + 0.4 * np.sin(theta1)
ax.fill(x1, y1, 'blue')

theta2 = np.linspace(0, np.pi/2, 100)
x2 = 0.5 + 0.4 * np.cos(theta2)
y2 = 0.5 + 0.4 * np.sin(theta2)
ax.fill(x2, y2, 'blue')

theta3 = np.linspace(-np.pi/2, 0, 100)
x3 = 0.5 + 0.4 * np.cos(theta3)
y3 = 0.5 + 0.4 * np.sin(theta3)
ax.fill(x3, y3, 'white')

theta4 = np.linspace(-np.pi, -np.pi/2, 100)
x4 = 0.5 + 0.4 * np.cos(theta4)
y4 = 0.5 + 0.4 * np.sin(theta4)
ax.fill(x4, y4, 'white')

# Set limits and hide axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.show()
