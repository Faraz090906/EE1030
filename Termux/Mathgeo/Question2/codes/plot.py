import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared C library
lib = ctypes.CDLL('./libarea_calculator.so')

# Define the C function argument and return types
lib.area.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.area.restype = ctypes.c_double

lib.generate_points.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_int,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]

def main(a, b, c, x_start, x_end, num_points):
    # Calculate the area using the C function
    area = lib.area(a, b, c, -2.0, 1.0)  # Calculate area from -2 to 1
    print(f"Calculated Area (using Riemann sum) from (-2, {function(a, b, c, -2):.2f}) to (1, {function(a, b, c, 1):.2f}): {area:.2f}")

    # Allocate memory for points
    points_x = (ctypes.c_double * num_points)()
    points_y = (ctypes.c_double * num_points)()

    # Generate points using the C function
    lib.generate_points(a, b, c, x_start, x_end, num_points, points_x, points_y)

    # Prepare data for plotting
    plot_x_vals = np.array(points_x)
    plot_y_vals = np.array(points_y)

    # Plot the lines
    plt.axvline(x=-2, label='x = -2', color='orange', linestyle='--')
    plt.axvline(x=1, label='x = 1', color='red', linestyle='--')

    plt.axhline(y=0, label='y = 0', color='black', linestyle='-')  # Horizontal line for y=0
    plt.axvline(x=0, label='x = 0', color='black', linestyle='-')  # Vertical line for x=0

    # Plot the parabola
    plt.plot(plot_x_vals, plot_y_vals, label='Parabola', color='blue')

    # Shade the area under the curve between -2 and 1
    plt.fill_between(plot_x_vals, plot_y_vals, 0, where=((plot_x_vals >= -2) & (plot_x_vals <= 1)), color='green', alpha=0.5, label='Shaded Area')

    # Get points at the limits -2 and 1
    limit_points = [(-2, function(a, b, c, -2)), (1, function(a, b, c, 1))]
    
    # Plot the limit points
    for x, y in limit_points:
        plt.scatter(x, y, color='red', marker='o')
        plt.text(x, y, f'({x:.2f}, {y:.2f})', fontsize=10, verticalalignment='bottom', horizontalalignment='right')

    plt.title('Points on the Parabola and Area Calculation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.legend()
    plt.savefig('../figs/fig.png')
    plt.show()

def function(a, b, c, x):
    return a * x**2 + b * x + c

if __name__ == "__main__":
    # Example usage
    main(a=1, b=0, c=0, x_start=-3, x_end=3, num_points=1000)

