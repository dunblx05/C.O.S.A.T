#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int a[101] = { 0, };
	int n, m, i, j, k;
	int sum = 0;
	int max = 0;
	scanf("%d %d", &n, &m);

	for (i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	for (i = 0; i < n; i++) {
		for (j = i + 1; j < n; j++) {
			for (k = j + 1; k < n; k++) {
				sum = a[i] + a[j] + a[k];
				if (max < sum && sum <= m) {
					max = sum;
				}
			}
		}
	}
	printf("%d", max);
}