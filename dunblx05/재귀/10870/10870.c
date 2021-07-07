#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int fibo(int a);

int main() {
	int n;
	int res = 0;
	scanf("%d", &n);
	res = fibo(n);
	printf("%d", res);
}

int fibo(int a) {
	if (a <= 1) {
		return a;
	}
	else
		return fibo(a - 1) + fibo(a - 2);
}