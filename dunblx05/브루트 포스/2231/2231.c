#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int n;
	int conduct = 0;
	int count = 0;
	scanf("%d", &n);

	for (int i = 1; i < n; i++) {
		int a, b, c, d, e, f, g;

		a = i / 1000000;
		b = (i % 1000000) / 100000;
		c = (i % 100000) / 10000;
		d = (i % 10000) / 1000;
		e = (i % 1000) / 100;
		f = (i % 100) / 10;
		g = (i % 10);

		conduct = i + a + b + c + d + e + f + g;
		
		if (conduct == n) {
			printf("%d", i);
			break;
		}
		count++;
	}
	if (count == n - 1) {
		printf("0");
	}
}