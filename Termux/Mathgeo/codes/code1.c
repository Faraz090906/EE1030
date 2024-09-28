#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

// Function to compute the matrices based on k
void computeMatrices(double **A, double **B, double **C, double k) {
    A[0][0] = k + 1; // Example values
    A[1][0] = 2 * k; 
    B[0][0] = 3 * k; 
    B[1][0] = 2 * k + 3; 
    C[0][0] = 5 * k - 1; 
    C[1][0] = 5 * k; 
}

int main() {
    double **A, **B, **C;
    FILE *file;
    double k;

    // Open the file for reading
    file = fopen("solution.txt", "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    
    fscanf(file, "%lf", &k);
    fclose(file);

    // Create matrices
    A = createMat(2, 1);
    B = createMat(2, 1);
    C = createMat(2, 1);
    
    // Compute the matrices based on k
    computeMatrices(A, B, C, k);

    // Perform matrix subtraction
    double **AB = Matsub(B, A, 2, 1);
    double **AC = Matsub(C, A, 2, 1);

    double **Rank_mat = createMat(2, 2);
    Rank_mat[0][0] = AB[0][0];
    Rank_mat[1][0] = AC[0][0];
    Rank_mat[0][1] = AB[1][0];
    Rank_mat[1][1] = AC[1][0];

    // Calculate condition
    double condition = Rank_mat[1][1] - 2 * Rank_mat[0][1];

    if (condition != 0) {
        // Adjust k based on the condition
        k = Rank_mat[1][1] / 2; // Adjusting k directly
    }

    printf("The calculated value of k is %lf\n", k);

    // Write all values to values.dat
    file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "%.02lf %.02lf\n", A[0][0], A[1][0]);
    fprintf(file, "%.02lf %.02lf\n", B[0][0], B[1][0]);
    fprintf(file, "%.02lf %.02lf\n", C[0][0], C[1][0]);
    fprintf(file, "%.02lf\n", k); // Store the value of k

    fclose(file);
    printf("Results have been written to values.dat\n");

    // Free allocated memory
    freeMat(A, 2);
    freeMat(B, 2);
    freeMat(C, 2);
    freeMat(AC, 2);
    freeMat(AB, 2);
    freeMat(Rank_mat, 2);

    return 0;
}

