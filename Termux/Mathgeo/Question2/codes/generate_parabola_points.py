import numpy as np

class Parabola:
    def __init__(self, a=1, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def calculate_point(self, x):
        # Calculate y using the parabola equation: y = ax^2 + bx + c
        return self.a * (x ** 2) + self.b * x + self.c

def generate_points(parabola, x_start, x_end, num_points):
    # Generate x values
    x_values = np.linspace(x_start, x_end, num_points)
    points = []

    for x in x_values:
        y = parabola.calculate_point(x)
        points.append((x, y))
    
    return points

def write_points_to_file(points, filename):
    with open(filename, 'w') as f:
        for x, y in points:
            f.write(f"{x:.6f}, {y:.6f}\n")

if __name__ == "__main__":
    # Create a Parabola instance for y = x^2
    parabola = Parabola(a=1, b=0, c=0)

    # Generate 57 points between x = -2 and x = 1
    points = generate_points(parabola, -2, 5, 57)

    # Write the points to a file
    write_points_to_file(points, 'points.dat')

    print("Points have been written to points.dat")

