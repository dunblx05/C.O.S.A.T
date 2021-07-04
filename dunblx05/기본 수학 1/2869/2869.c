#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main() {
	int a, b, v;
	double i;
	scanf("%d %d %d", &a, &b, &v);
	// (v-b)/(a-b)
	i = (double) (v - b) / (a - b);
	int result = ceil(i);
	printf("%d", result);
}