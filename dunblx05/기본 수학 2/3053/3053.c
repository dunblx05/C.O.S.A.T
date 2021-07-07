#define _CRT_SECURE_NO_WARNINGS
#define M_PI 3.14159265358979323846

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
	int r;
	scanf("%d", &r);

	printf("%lf %lf", M_PI *pow(r, 2), 2 * pow(r, 2));
	
}
