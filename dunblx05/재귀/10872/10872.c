#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int factorial(int a);

int main() {
	int n;
	int res = 0;
	scanf("%d", &n);
	res = factorial(n);
	printf("%d", res);
}

int factorial(int a) {
	if (a <= 0) {	//종료조건
		return 1;
	}
	else
		return a * factorial(a - 1);	//recursion
}