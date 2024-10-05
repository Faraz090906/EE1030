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
    num_points = 1000  # Total number of points for plotting

    # Generate points for the area calculation from -2 to 1
    area_x_start, area_x_end = -2, 1
    area_points = generate_points(a, b, c, area_x_start, area_x_end, num_points)

    # Load the shared C library
    lib = ctypes.CDLL('./area_calculator.so')
    
    # Define the function argument and return types
    lib.area.argtypes = [ctypes.c_double, ctypes.c_double]
    lib.area.restype = ctypes.c_double
    
    # Calculate the area using the C function
    area = lib.area(area_x_start, area_x_end)  # Calculate area from -2 to 1
    
    print(f"Calculated Area (using Riemann sum) from ({area_x_start}, {area_x_start**2}) to ({area_x_end}, {area_x_end**2}): {area:.2f}")

    # Prepare data for plotting the full range from -3 to 3
    plot_x_start, plot_x_end = -3, 3
    plot_x_vals = np.linspace(plot_x_start, plot_x_end, num_points)
    plot_y_vals = a * (plot_x_vals ** 2) + b * plot_x_vals + c
    
    # Plot the lines
    plt.axvline(x=-2, label='x = -2', color='orange', linestyle='--')
    plt.axvline(x=1, label='x = 1', color='red', linestyle='--')
    
    plt.axhline(y=0, label='y = 0', color='black', linestyle='-')  # Horizontal line for y=0
    plt.axvline(x=0, label='x = 0', color='black', linestyle='-')  # Vertical line for x=0

    # Plot the parabola
    plt.plot(plot_x_vals, plot_y_vals, label='Parabola', color='blue')

    # Shade the area under the curve between -2 and 1
    plt.fill_between(plot_x_vals, plot_y_vals, 0, where=((plot_x_vals >= -2) & (plot_x_vals <= 1)), color='green', alpha=0.5, label='Shaded Area')

    # Extract specific points from the generated points for the area calculation
    specific_points = [(area_points[0].x, area_points[0].y), (area_points[-1].x, area_points[-1].y)]
    
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

