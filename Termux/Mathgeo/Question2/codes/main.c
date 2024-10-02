#include <stdio.h>
#include <math.h>
#include "func.c"

int main()
{
	double a = 0.25 ;
	double point1[2] = {1,1} ;
	double point2[2] = {-2,4} ;

	FILE *ptr ;
	ptr = fopen("main.txt", "w") ;
	for ( float t=-4; t<=10; t+=0.5 )
	{
		double x = a*t*2 ;
		double y = a*t*t ;
		fprintf(ptr, "%.2lf %lf\n", x, y) ;
	}
	fprintf(ptr, "%.2lf\n", area(point2[0], point1[0])) ;
	fclose(ptr) ;
	return 0;
}
