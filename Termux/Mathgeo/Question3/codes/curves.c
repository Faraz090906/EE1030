#include <stdio.h>
#include <math.h>
#include <stdlib.h>

typedef struct 
{
    double* x_values;
    double* y_values;
    int num_points;
    double a; 
    double x_min; 
    double x_max; 
} Parabola;

typedef struct 
{
    double* x_values;
    double* y_values;
    int num_points;
    double r; 
} Circle;

Parabola* create_parabola(int num_points, double a, double x_min, double x_max) 
{
    Parabola* parabola = (Parabola*)malloc(sizeof(Parabola));
    parabola->x_values = (double*)malloc(num_points * sizeof(double));
    parabola->y_values = (double*)malloc(num_points * sizeof(double));
    parabola->num_points = num_points;
    parabola->a = a;
    parabola->x_min = x_min;
    parabola->x_max = x_max;
    return parabola;
}

Circle* create_circle(int num_points, double r) 
{
    Circle* circle = (Circle*)malloc(sizeof(Circle));
    circle->x_values = (double*)malloc(num_points * sizeof(double));
    circle->y_values = (double*)malloc(num_points * sizeof(double));
    circle->num_points = num_points;
    circle->r = r;
    return circle;
}

void free_parabola(Parabola* parabola) 
{
    free(parabola->x_values);
    free(parabola->y_values);
    free(parabola);
}

void free_circle(Circle* circle) 
{
    free(circle->x_values);
    free(circle->y_values);
    free(circle);
}

// Generating points of parabola y^2 = 4ax
void gen_parab(Parabola* parabola) 
{
    double step = (parabola->x_max - parabola->x_min) / (parabola->num_points - 1);
    for (int i = 0; i < parabola->num_points; i++) 
    {
        parabola->x_values[i] = parabola->x_min + i * step;
        parabola->y_values[i] = sqrt(4 * parabola->a * parabola->x_values[i]);
    }
}

// Generating points of circle
void gen_circle(Circle* circle) 
{
    double inclination_step = (2 * M_PI) / circle->num_points;
    for (int i = 0; i < circle->num_points; i++) 
    {
        double inclination = inclination_step * i;
        circle->x_values[i] = circle->r * cos(inclination);
        circle->y_values[i] = circle->r * sin(inclination);
    }
}

// Function to find intersections between the parabola and circle
void find_intersections(double* intersection_points, Parabola* parabola, Circle* circle) 
{
    double x_p = 0;
    double y_p;
    double x_max = parabola->x_max;
    
    for (double i = 0; x_p <= x_max; i += 0.5) 
    {
        x_p = parabola->x_min + i;
        y_p = sqrt(4 * parabola->a * x_p);
        double y_c = sqrt(pow(circle->r, 2) - pow(x_p, 2));
        
        if (y_c == y_p) {
            intersection_points[0] = x_p; 
            intersection_points[1] = y_p;
            intersection_points[2] = x_p; 
            intersection_points[3] = -y_p;
            break;
        }
    }
}

// Calculating the area under the parabola using the trapezoidal rule
double area_parab(Parabola* parabola, double x_start, double x_end) 
{
    double step = (x_end - x_start) / (parabola->num_points - 1);
    double area = 0.0;

    for (int i = 0; i < parabola->num_points - 1; i++) 
    {
        double x_left = x_start + i * step;
        double x_right = x_start + (i + 1) * step;

        double y_left = sqrt(4 * parabola->a * x_left);
        double y_right = sqrt(4 * parabola->a * x_right);

        area += (y_left + y_right) * step / 2; 
    }

    return 2 * area; 
}

// Calculating the area under the circle using the trapezoidal rule
double area_circle(Circle* circle, double x_start, double x_end) 
{
    double step = (x_end - x_start) / (circle->num_points - 1);
    double area = 0.0;

    for (int i = 0; i < circle->num_points - 1; i++) 
    {
        double x_left = x_start + i * step;
        double x_right = x_start + (i + 1) * step;

        double y_left = sqrt(pow(circle->r, 2) - pow(x_left, 2));
        double y_right = sqrt(pow(circle->r, 2) - pow(x_right, 2));

        area += (y_left + y_right) * step / 2;
    }

    return 2 * area;
}

