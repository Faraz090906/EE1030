import numpy as np
import matplotlib.pyplot as plt

# Load points from the file
points = np.loadtxt("area_points.txt", delimiter=' ', max_rows=len(list(open("area_points.txt")))-1)

# Extract x and y values
x = points[:, 0]
y = points[:, 1]

# Define points A, B, C, D
A = np.array([0, 0])
B = np.array([-2, 4])
C = np.array([1, 1])
D = np.array([-1, 1])

# Plot the parabola
plt.plot(x, y, label='Parabola', color='blue')

# Plot the specific points
plt.scatter(A[0], A[1], color='green', marker='o', label='Point A (0,0)')
plt.scatter(B[0], B[1], color='red', marker='o', label='Point B (-2,4)')
plt.scatter(C[0], C[1], color='purple', marker='o', label='Point C (1,1)')
plt.scatter(D[0], D[1], color='orange', marker='o', label='Point D (-1,1)')

# Create an x range for shading between the lines
x_fill = np.linspace(-2, 1, 400)
y_parabola = np.interp(x_fill, x, y)

# Shade the region between the lines and the parabola
plt.fill_between(x_fill, y_parabola, 0, where=(y_parabola >= 0), color='green', alpha=0.5, label='Shaded region')

# Plot the lines
plt.axvline(x=-2, label='x = -2', color='orange', linestyle='--')
plt.axvline(x=1, label='x = 1', color='red', linestyle='--')

# Set axis limits
plt.xlim(-3, 2)  # Set x-axis limits
plt.ylim(0, 5)  # Set y-axis limits

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Points A, B and Shaded Region Along Parabola")

# Add grid and legend
plt.grid(True)
plt.legend()

# Save the figure
plt.savefig('../figs/fig.png')
plt.show()
