#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int a[246913] = { 0 };

int main() {
	int n, i, j;
	int check = 0, count = 0;

	while (1) {
		scanf("%d", &n);
		if (n == 0) {
			break;
		}

		for (i = 0; i <= 2 * n; i++) {
			a[i] = i;
		}
		a[1] = 0;

		for (i = 2; i <= 2 * n; i++) {
			if (a[i] != 0) {
				for (j = 2 * i; j <= 2 * n; j = j + i) {
					a[j] = 0;
				}
			}
		}

		for (i = n + 1; i <= 2 * n; i++) {
			if (a[i] != 0) {
				count++;
			}
		}
		printf("%d\n", count);
		count = 0;
	}
}
