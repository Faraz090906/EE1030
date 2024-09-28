# Code by GVV Sharma
# September 12, 2023
# Revised July 21, 2024
# Released under GNU GPL
# Point Vectors

import sys                                          # for path to external scripts
sys.path.insert(0, '/home/faraz090906/Python/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Read points and k from values.dat
def read_values(file_path):
    points = []
    k = None
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.strip()  # Remove any leading/trailing whitespace
            if i == len(lines) - 1:  # Last line should contain k
                k = float(line)  # Directly convert the last line to float
            else:
                if line:  # Ignore empty lines
                    parts = line.split()
                    if len(parts) == 2:
                        try:
                            points.append([float(parts[0]), float(parts[1])])
                        except ValueError:
                            print(f"Skipping line due to error: {line}")
    
    if k is None:
        raise ValueError("The value of k was not found in the file.")
    
    return np.array(points).T, k

# Load the points and k
try:
    tri_coords, k = read_values('values.dat')
except Exception as e:
    print(f"Error reading values: {e}")
    sys.exit(1)

# Assign points A, B, C
A = tri_coords[:, 0].reshape(-1, 1)  # First column
B = tri_coords[:, 1].reshape(-1, 1)  # Second column
C = tri_coords[:, 2].reshape(-1, 1)  # Third column

# Generating all lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

# Plotting all lines
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_BC[0, :], x_BC[1, :], label='$BC$')
plt.plot(x_CA[0, :], x_CA[1, :], label='$CA$')

# Labeling the coordinates
colors = np.arange(1, 4)
plt.scatter(tri_coords[0, :], tri_coords[1, :], c=colors)
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0, i]:.2f}, {tri_coords[1, i]:.2f})',
                 (tri_coords[0, i], tri_coords[1, i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(25, 5),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center

# Use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.grid()  # minor
plt.title('Showing that A,B,C are collinear', loc = 'right', pad = 15)  
plt.axis('equal')
plt.show()

