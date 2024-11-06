import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared C library
lib = ctypes.CDLL('./libarea_calculator.so')

# Define the Parabola struct equivalent in Python
class Parabola(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double),
                ("b", ctypes.c_double),
                ("c", ctypes.c_double),
                ("x", ctypes.c_double)]

# Define the C function argument and return types
lib.area.argtypes = [ctypes.POINTER(Parabola), ctypes.c_double, ctypes.c_double]
lib.area.restype = ctypes.c_double

lib.generate_points.argtypes = [
    ctypes.POINTER(Parabola), ctypes.c_double, ctypes.c_double,
    ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]

# Function to calculate the value of the parabola at a given x
def function(a, b, c, x):
    return a * x**2 + b * x + c

def main(a, b, c, x_start, x_end, num_points, area_start, area_end):
    # Create a Parabola struct and set the values of a, b, c
    p = Parabola(a=a, b=b, c=c, x=0.0)

    # Calculate the area using the C function from area_start to area_end
    area = lib.area(ctypes.byref(p), area_start, area_end)  # Calculate area using C function

    # Corrected print statement for area calculation
    print(f"Calculated Area (using Riemann sum) from ({area_start},"
          f"{function(a, b, c, area_start):.2f}) to ({area_end}, "
          f"{function(a, b, c, area_end):.2f}): {area:.2f}")

    # Allocate memory for points
    points_x = (ctypes.c_double * num_points)()
    points_y = (ctypes.c_double * num_points)()

    # Generate points using the C function for the range from x_start to x_end
    lib.generate_points(ctypes.byref(p), x_start, x_end, num_points, points_x, points_y)

    # Prepare data for plotting
    plot_x_vals = np.array(points_x)
    plot_y_vals = np.array(points_y)

    # Plot the lines for x_start and x_end
    plt.axvline(x=area_start, label=f'x = {area_start}', color='orange', linestyle='--')
    plt.axvline(x=area_end, label=f'x = {area_end}', color='red', linestyle='--')

    plt.axhline(y=0, label='y = 0', color='black', linestyle='-')  # Horizontal line for y=0
    plt.axvline(x=0, label='x = 0', color='black', linestyle='-')  # Vertical line for x=0

    # Plot the parabola
    plt.plot(plot_x_vals, plot_y_vals, label='Parabola', color='blue')

    # Shade the area under the curve between area_start and area_end
    plt.fill_between(plot_x_vals, plot_y_vals, 0, where=((plot_x_vals >= area_start) & (plot_x_vals <= area_end)), color='green', alpha=0.5, label='Shaded Area')

    # Get points at the limits area_start and area_end
    limit_points = [(area_start, function(a, b, c, area_start)), (area_end, function(a, b, c, area_end))]
    
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

if __name__ == "__main__":
    # Example usage with x_start = -3, x_end = 3 for generating points
    # and area_start = -2, area_end = 1 for area calculation
    main(a=1, b=0, c=0, x_start=-3, x_end=3, num_points=1000, area_start=-2, area_end=1)

