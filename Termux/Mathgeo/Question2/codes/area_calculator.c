#include <stdio.h>
#include <stdlib.h>

// Define the function for the parabola y = x^2
double function(double x) {
    return x * x;
}

// Calculate the area using Riemann sum from lower_limit to upper_limit
double area(double lower_limit, double upper_limit) {
    double sum = 0.0;
    double delta_x = 1e-7; // Width of each rectangle
    int num_points = (int)((upper_limit - lower_limit) / delta_x); // Total number of rectangles

    // Allocate memory for points
    double *points_x = (double *)malloc(num_points * sizeof(double));
    double *points_y = (double *)malloc(num_points * sizeof(double));
    if (points_x == NULL || points_y == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return -1; // Indicate error
    }

    // Generate points and calculate the area
    for (int i = 0; i < num_points; i++) {
        points_x[i] = lower_limit + i * delta_x; // Calculate x value
        points_y[i] = function(points_x[i]); // Calculate y value
        sum += points_y[i] * delta_x; // Height * Width
    }

    free(points_x); // Free allocated memory for x points
    free(points_y); // Free allocated memory for y points

    return sum;
}

