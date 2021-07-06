#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {

	int x, y, z;

	while (1) {
		int temp = 0;
		scanf("%d %d %d", &x, &y, &z);

		if (x == 0 && y == 0 && z == 0) {
			return 0;
		}

		if (x >= y) {
			temp = y;
			y = x;
			x = temp;
		}

		if (y >= z) {
			temp = z;
			z = y;
			y = temp;
		}

		if (x >= z) {
			temp = z;
			z = x;
			x = temp;
		}

		if (pow(x, 2) + pow(y, 2) == pow(z, 2)) {
			printf("right\n");
		}
		else
			printf("wrong\n");
	}
}
