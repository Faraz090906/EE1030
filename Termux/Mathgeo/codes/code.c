#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

double **normal2Dto(double **a){
	double **normal = createMat(2,1);
	normal[0][0] = -a[1][0];
	normal[1][0] = a[0][1];
	freeMat(normal,2);
	return normal;
}

double valueofk(double ax1,double bx1,double ay1,double by1,double ax2,double bx2,double ay2,double by2,double ax3,double bx3,double ay3,double by3){
	// A = (ax1k+bx1, ay1k+by1), B = (ax2k+bx2, ay2k+by2), C = (ax3k+bx3, ay3k+by3)
	double A = ((ay1-ay2)*(ax2-ax3)-(ax1-ax2)*(ay2-ay3));
	double B = ((by1-by2)*(ax2-ax3)+(bx2-bx3)*(ay1-ay2)-(bx1-bx2)*(ay2-ay3)-(ax1-ax2)*(by2-by3));
	double C = ((by1-by2)*(bx2-bx3)-(bx1-bx2)*(by2-by3));
	double k = ((-B-sqrt(B*B-4*A*C))/(2*A));
	return k;
}

void point_gen(FILE *fptr, double **A, double **B, int no_rows, int no_cols, int num_points) {
    for (double i = 0; i <= num_points; i++) {
        double **output = Matadd(A, Matscale(Matsub(B,A,no_rows,no_cols),no_rows,no_cols,(double)i/num_points), no_rows, no_cols);
        fprintf(fptr, "%lf,%lf\n", output[0][0], output[1][0]);
        freeMat(output,no_rows);
    }
}

int main() {
    int m = 2; int n = 1;
    double **A = createMat(m, n);
    double **B = createMat(m, n);
    double **C = createMat(m, n);
    
    double ax1=1, bx1=1, ay1=2, by1=0, ax2=3, bx2=0, ay2=2, by2=3, ax3=5, bx3=-1, ay3=5, by3=0; 
    
    double k = valueofk(ax1, bx1, ay1, by1, ax2, bx2, ay2, by2, ax3, bx3, ay3, by3);
    
    double x1=ax1*k+bx1, y1=ay1*k+by1, x2=ax2*k+bx2, y2=ay2*k+by2, x3=ax3*k+bx3, y3=ay3*k+by3;

    A[0][0] = x1;
    A[1][0] = y1;
    B[0][0] = x2;
    B[1][0] = y2;
    C[0][0] = x3;
    C[1][0] = y3;

    FILE *fptr;
    fptr = fopen("points.dat", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    point_gen(fptr, A, B, m, n, 20);
    point_gen(fptr, B, C, m, n, 20);
    
    fprintf(fptr, "The value of k is %lf",k);
    
     // Free all allocated memory
    freeMat(A,m);
    freeMat(B,m);
    freeMat(C,m);
    fclose(fptr);
    return 0;
}
