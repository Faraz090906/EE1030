#include <stdio.h>
#include <stdlib.h>

// Define the struct for the Parabola with coefficients a, b, c, and variable x
typedef struct {
    double a;
    double b;
    double c;
    double x;
} Parabola;

// Define the function for the parabola y = ax^2 + bx + c using the Parabola struct
double function(Parabola *p) {
    return p->a * p->x * p->x + p->b * p->x + p->c;
}

// Calculate the area using Riemann sum from lower_limit to upper_limit
double area(Parabola *p, double lower_limit, double upper_limit) {
    double sum = 0.0;
    double delta_x = 1e-7; // Width of each rectangle
    int num_points = (int)((upper_limit - lower_limit) / delta_x);

    for (int i = 0; i < num_points; i++) {
        p->x = lower_limit + i * delta_x; // Set x value from lower limit to upper limit
        sum += function(p) * delta_x; // Height * Width
    }

    return sum;
}

// Generate points in the range from x_start to x_end and store them in the arrays
void generate_points(Parabola *p, double x_start, double x_end, int num_points, double *points_x, double *points_y) 
{
    double delta_x = (x_end - x_start) / (num_points - 1);
    
    for (int i = 0; i < num_points; i++) {
        p->x = x_start + i * delta_x; 
        points_x[i] = p->x;
        points_y[i] = function(p); 
    }
}

