#include <stdio.h>
#include <math.h>
#include "func.c"

int main() {
    double points[57][2]; // Array to store 57 points
    FILE *ptr;

    // Open the file to read points
    ptr = fopen("points.dat", "r");
    if (ptr == NULL) {
        fprintf(stderr, "Error opening points.dat\n");
        return 1;
    }

    // Read points from the file
    for (int i = 0; i < 57; i++) {
        if (fscanf(ptr, "%lf, %lf\n", &points[i][0], &points[i][1]) != 2) {
            fprintf(stderr, "Error reading points\n");
            fclose(ptr);
            return 1;
        }
    }
    fclose(ptr);

    // Define point1 and point2 based on the first two points read from the file
    double point1[2] = {points[0][0], points[0][1]}; // First point
    double point2[2] = {points[24][0], points[24][1]}; // 17th point

    // Write points to main.txt
    FILE *output;
    output = fopen("area_points.txt", "w");
    if (output == NULL) {
        fprintf(stderr, "Error opening area_points.txt\n");
        return 1;
    }

    // Print the points from the array to main.txt
    for (int i = 0; i < 57; i++) {
        fprintf(output, "%.3lf %.6lf\n", points[i][0], points[i][1]);
    }

    // Calculate and print the area based on point1 and point2
    //double calculated_area = area(point1[0], point2[0]);
    fprintf(output, "Area: %.2lf\n", area(point1[0], point2[0]));

    fclose(output);
    return 0;
}
