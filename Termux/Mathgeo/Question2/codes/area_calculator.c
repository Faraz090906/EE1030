#include <stdio.h>

// Define the function for the parabola y = x^2
double function(double x) {
    return x * x;
}

// Calculate the area using Riemann sum from lower_limit to upper_limit
double area(double lower_limit, double upper_limit) {
    double sum = 0.0;
    double delta_x = 1e-7; // Width of each rectangle

    for (double i = lower_limit; i <= upper_limit; i += delta_x) {
        sum += function(i) * delta_x; // Height * Width
    }
    return sum;
}

