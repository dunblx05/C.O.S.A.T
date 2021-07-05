#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int a[1000001] = { 0 };

int main() {
	int n, m;
	scanf("%d", &m);
	scanf("%d", &n);

	for (int i = 0; i <= 1000000; i++) {
		a[i] = i;
	}
	a[1] = 0;
	for (int i = 2; i <= 1000000; i++) {
		if (a[i] != 0) {
			for (int j = 2 * i; j <= 1000000; j = j + i) {
				a[j] = 0;
			}
		}
	}
	for (int i = m; i <= n; i++) {
		if (a[i] != 0) {
			printf("%d\n", a[i]);
		}
	}
}
