import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Define the structure for points in C-style
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

def generate_points(a, b, c, x_start, x_end, num_points):
    # Allocate memory for points
    point_array_type = Point * num_points
    points = point_array_type()

    x_values = np.linspace(x_start, x_end, num_points)
    
    for i in range(num_points):
        points[i].x = x_values[i]
        points[i].y = a * (x_values[i] ** 2) + b * x_values[i] + c
    
    return points

if __name__ == "__main__":
    # Parameters for the parabola y = x^2
    a, b, c = 1, 0, 0
    x_start, x_end = -2, 1  # Area from -2 to 1
    num_points = 1000
    
    # Generate points on the parabola
    points = generate_points(a, b, c, x_start, x_end, num_points)

    # Load the shared C library
    lib = ctypes.CDLL('./area_calculator.so')
    
    # Define the function argument and return types
    lib.area.argtypes = [ctypes.c_double, ctypes.c_double]
    lib.area.restype = ctypes.c_double
    
    # Calculate the area using the C function
    area = lib.area(-2.0, 1.0)  # Calculate area from -2 to 1
    
    print(f"Calculated Area (using Riemann sum) from (-2, 0) to (1, 1): {area:.2f}")

    # Prepare data for plotting the full range from -4 to 4
    x_vals = np.linspace(-3, 3, 400)
    y_vals = a * (x_vals ** 2) + b * x_vals + c
    
    # Plot the lines
    plt.axvline(x=-2, label='x = -2', color='orange', linestyle='--')
    plt.axvline(x=1, label='x = 1', color='red', linestyle='--')
    
    plt.axhline(y=0, label='y-axis', color='black', linestyle='-')  # Horizontal line for y=0
    plt.axvline(x=0, label='x-axis', color='black', linestyle='-')  # Vertical line for x=0

    # Plot the parabola
    plt.plot(x_vals, y_vals, label='Parabola', color='blue')

    # Shade the area under the curve between -2 and 1
    plt.fill_between(x_vals, y_vals, 0, where=(x_vals >= -2) & (x_vals <= 1), color='green', alpha=0.5, label='Shaded Area')

    # Extract specific points from the generated points using pointers
    specific_points = [(points[0].x, points[0].y), (points[-1].x, points[-1].y)]
    
    # Plot the specific points
    for (x, y) in specific_points:
        plt.scatter(x, y, color='red', marker='o')
        plt.text(x, y, f'({x:.2f}, {y:.2f})', fontsize=10, verticalalignment='bottom', horizontalalignment='right')

    plt.title('Points on the Parabola and Area Calculation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.legend()
    plt.savefig('../figs/fig.png')
    plt.show()

