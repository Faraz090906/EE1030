#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    double **A, **B, **C;
    double k; // Declare k without initializing
    // Set k based on your logic; for example, you can set k = 2
    k = 2.0; // You may use a calculation to determine this value

    A = createMat(2, 1);
    B = createMat(2, 1);
    C = createMat(2, 1);
    
    A[0][0] = k + 1; // 3.0
    A[1][0] = 2 * k; // 4.0
    B[0][0] = 3 * k; // 6.0
    B[1][0] = 2 * k + 3; // 7.0
    C[0][0] = 5 * k - 1; // 9.0
    C[1][0] = 5 * k; // 10.0

    double **AB, **AC;
    AB = createMat(2, 1);
    AC = createMat(2, 1);
    AB = Matsub(B, A, 2, 1);
    AC = Matsub(C, A, 2, 1);

    double **Rank_mat = createMat(2, 2);
    Rank_mat[0][0] = AB[0][0];
    Rank_mat[1][0] = AC[0][0];
    Rank_mat[0][1] = AB[1][0];
    Rank_mat[1][1] = AC[1][0];

    // Example calculation for k to satisfy some condition
    // For example, if you want to make sure the second row equals zero
    double condition = Rank_mat[1][1] - 2 * Rank_mat[0][1];
    if (condition != 0) {
        // Adjust k based on your logic (not shown, for example purposes)
        // k = ... (implement your logic to compute k here)
    }
    printf("The value of k is %lf\n", k);

    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write coordinates and the value of k to the file
    fprintf(file, "x y\n");
    fprintf(file, "%.02lf %.02lf\n", A[0][0], A[1][0]);
    fprintf(file, "%.02lf %.02lf\n", B[0][0], B[1][0]);
    fprintf(file, "%.02lf %.02lf\n", C[0][0], C[1][0]);
    fclose(file);
    printf("Results have been written to values.dat\n");
    
    freeMat(A, 2);
    freeMat(B, 2);
    freeMat(C, 2);
    freeMat(AC, 2);
    freeMat(AB, 2);
    freeMat(Rank_mat, 2);

    return 0;
}

