#include <stdio.h>
#include <math.h>

double function(double x) 
{
    return x * x; // Parabola function y = x^2
}

double area(double lower_limit, double upper_limit) 
{
    double sum = 0.0;
    
    for (double i = lower_limit; i <= upper_limit; i += 1e-7) 
    {
        sum += function(i) * 1e-7; // Riemann sum
    }
    return sum;
}
