#include <stdio.h>
#include <stdlib.h>

// Define the function for the parabola y = ax^2 + bx + c
double function(double a, double b, double c, double x) {
    return a * x * x + b * x + c;
}

// Calculate the area using Riemann sum from lower_limit to upper_limit
double area(double a, double b, double c, double lower_limit, double upper_limit) {
    double sum = 0.0;
    double delta_x = 1e-7; // Width of each rectangle
    int num_points = (int)((upper_limit - lower_limit) / delta_x); // Total number of rectangles

    for (int i = 0; i < num_points; i++) {
        double x = lower_limit + i * delta_x; // Calculate x value
        sum += function(a, b, c, x) * delta_x; // Height * Width
    }

    return sum;
}

// Generate points in the range from x_start to x_end
void generate_points(double a, double b, double c, double x_start, double x_end, int num_points, double *points_x, double *points_y) {
    double delta_x = (x_end - x_start) / (num_points - 1);
    
    for (int i = 0; i < num_points; i++) {
        points_x[i] = x_start + i * delta_x; // Calculate x value
        points_y[i] = function(a, b, c, points_x[i]); // Calculate y value
    }
}

