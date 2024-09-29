import numpy as np
import matplotlib.pyplot as plt

# Load the points from the text file
points = np.loadtxt("points.dat", delimiter=',',max_rows=len(list(open("./points.dat")))-1)

# Extract the x and y coordinates
x = points[:, 0]
y = points[:, 1]

A = np.array([points[0,0],points[0,1]])
B = np.array([points[20,0],points[20,1]])
C = np.array([points[41,0],points[41,1]])

plt.figure()  # Create a new figure for the plot
plt.plot(A[0], A[1], 'ro', label='Point A')  # Red dot for point A
plt.plot(B[0], B[1], 'bo', label='Point B')  # Blue dot for point B
plt.plot(C[0], C[1], 'go', label='Point C')  # Green dot for point C

# Display the coordinates of each point near the point marker
plt.text(A[0], A[1], f'({A[0]:.2f}, {A[1]:.2f})', fontsize=12, ha='right', color='red')
plt.text(B[0], B[1], f'({B[0]:.2f}, {B[1]:.2f})', fontsize=12, ha='right', color='blue')
plt.text(C[0], C[1], f'({C[0]:.2f}, {C[1]:.2f})', fontsize=12, ha='right', color='green')

# Plot the triangle
plt.plot(x, y, label='Line')
plt.xlabel("x")
plt.ylabel("y")
plt.title("The given points are collinear at k=2, and their coordinates")
plt.grid(True)
plt.legend()

# Save the plot to figs directory
#plt.savefig('../figs/fig.png')
plt.show()
