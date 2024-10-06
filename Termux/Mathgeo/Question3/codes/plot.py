import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libcurves.so')

# Define the C functions' argument types
lib.gen_parab.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.gen_circle.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_double]
lib.find_intersections.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.area_parab.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
lib.area_circle.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]

# Define the return types
lib.find_intersections.restype = None
lib.area_parab.restype = ctypes.c_double
lib.area_circle.restype = ctypes.c_double

# Parameters
num_points = 500
a = 1.0  # For the parabola y^2 = 4ax
r = np.sqrt(9 / 4)  # Radius for the circle 4x^2 + 4y^2 = 9
intersection_points = (ctypes.c_double * 4)()  # Space for intersection points

# Generate points for the parabola and circle
x_parab = (ctypes.c_double * num_points)()
y_parab = (ctypes.c_double * num_points)()
x_circle = (ctypes.c_double * num_points)()
y_circle = (ctypes.c_double * num_points)()

lib.gen_parab(x_parab, y_parab, num_points, 0.0, 3.0, a)
lib.gen_circle(x_circle, y_circle, num_points, r)

# Find intersections
lib.find_intersections(intersection_points, 0.0, 3.0, r, a)

# Extract intersection points
x1 = intersection_points[0]
y1_pos = intersection_points[1]
y1_neg = intersection_points[3] 

# Calculating the total area
area_parab = lib.area_parab(ctypes.c_double(0.0), ctypes.c_double(x1), ctypes.c_double(a), ctypes.c_int(num_points))
area_circle = lib.area_circle(ctypes.c_double(x1), ctypes.c_double(r), ctypes.c_double(r), ctypes.c_int(num_points))

total_area = area_parab + area_circle

print(f"Total area between the curves: {total_area:.4f}")


# Plotting
x_parab_np = np.array(x_parab)
y_parab_np = np.array(y_parab)

x_circle_np = np.array(x_circle)
y_circle_np = np.array(y_circle)

plt.figure(figsize=(6, 6))

# Plot parabola
plt.plot(x_parab_np, y_parab_np, label='Parabola: $y^2=4x$', color='blue')
plt.plot(x_parab_np, -y_parab_np, color='blue')  # Negative side of parabola

# Plot circle
plt.plot(x_circle_np, y_circle_np, label='Circle: $4x^2 + 4y^2 = 9$', color='orange')
plt.plot(x_circle_np, -y_circle_np, color='orange')  # Negative side of circle

# Plot intersection points
if x1 != 0 or y1_pos != 0:
    plt.plot(x1, y1_pos, 'ro') 
    plt.text(x1, y1_pos, f'({x1:.2f}, {y1_pos:.2f})')

if x1 != 0 or y1_neg != 0:
    plt.plot(x1, y1_neg, 'ro')  
    plt.text(x1, y1_neg, f'({x1:.2f}, {y1_neg:.2f})')

# Generate the curves 
lib.gen_parab(x_parab, y_parab, num_points, 0.0, 3.0, a)
lib.gen_circle(x_circle, y_circle, num_points, r)

x_parab_np = np.array(x_parab)
y_parab_np = np.array(y_parab)
x_circle_np = np.array(x_circle)
y_circle_np = np.array(y_circle)

# define shading regions
x_bound_parab = x1  # End of parabola's shaded region
x_bound_circle = r  # End of circle's shaded region

# Define regions for shading
shade_parabola = np.logical_and(x_parab_np >= 0, x_parab_np <= x_bound_parab)
shade_circle = np.logical_and(x_circle_np >= x_bound_parab, x_circle_np <= x_bound_circle)

#method7:controlled shading
# Parabola shading (x=0 to x=0.5)
plt.fill_between(x_parab_np, y_parab_np, -y_parab_np, where=shade_parabola, color='pink', alpha=0.5)
# Circle shading (x=0.5 to x=1.5)
plt.fill_between(x_circle_np, y_circle_np, 0, where=shade_circle, color='pink', alpha=0.5, label='Shaded Area (Circle & Parabola)')



plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(0, color='black', lw=0.5, ls='-')
plt.axvline(0, color='black', lw=0.5, ls='-')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Area Between the Parabola and Circle')
plt.legend()
plt.grid()
plt.savefig('../figs/fig.png')
plt.show()

