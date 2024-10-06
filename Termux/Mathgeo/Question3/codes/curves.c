#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Generating points of parabola y^2 = 4ax, a=1
void gen_parab(double* x_values, double* y_values, int num_points, double x_min, double x_max, double a) 
{
    double step = (x_max - x_min) / (num_points - 1);
    for (int i = 0; i < num_points; i++) 
    {
        x_values[i] = x_min + i * step;
        y_values[i] = sqrt(4 * a * x_values[i]);
    }
}

// Generating points of circle 4x^2 + 4y^2 = 9, r^2 = 9/4
void gen_circle(double* x_values, double* y_values, int num_points, double r) 
{
    double inclination_step = (2 * M_PI) / num_points;
    for (int i = 0; i < num_points; i++) 
    {
        double inclination = inclination_step * i;
        x_values[i] = r * cos(inclination);
        y_values[i] = r * sin(inclination);
    }
}

// Calculating the points of intersections
void find_intersections(double* intersection_points, double x_min, double x_max, double r, double a) 
{
	double x_p = 0;
	double y_p;
	for(double i=0; x_p <= x_max ; i+=0.5)
	{
		x_p = x_min + i;
		y_p = sqrt( 4 * a * x_p);
		double y_c = sqrt(pow(r, 2) - pow(x_p, 2));
		if(y_c == y_p)
		{
			*intersection_points = x_p; 
			*(intersection_points+1) = y_p;
			*(intersection_points+2) = x_p; 
			*(intersection_points+3) = -y_p;
			break;
		} 
		else continue;
	}

}


// Calculating the area using trapezoidal rule
double area_parab(double x_start, double x_end, double a, int num_points) 
{
    double step = (x_end - x_start) / (num_points - 1);
    double area = 0.0;

    for (int i = 0; i < num_points - 1; i++) 
    {
        double x_left = x_start + i * step;
        double x_right = x_start + (i + 1) * step;

        double y_left = sqrt(4 * a * x_left);
        double y_right = sqrt(4 * a * x_right);

        area += (y_left + y_right) * step / 2; // Trapezoidal area
    }

    return 2 * area;
}

// Area under the circle
double area_circle(double x_start, double x_end, double r, int num_points) 
{
    double step = (x_end - x_start) / (num_points - 1);
    double area = 0.0;

    for (int i = 0; i < num_points - 1; i++) 
    {
        double x_left = x_start + i * step;
        double x_right = x_start + (i + 1) * step;

        double y_left = sqrt(pow(r, 2) - pow(x_left, 2));
        double y_right = sqrt(pow(r, 2) - pow(x_right, 2));

        area += (y_left + y_right) * step / 2; // Trapezoidal area
    }

    return 2 * area;
}

