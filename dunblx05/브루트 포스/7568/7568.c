#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int n, i;
	int rank[50] = { 0, };
	int x[50] = { 0, }, y[50] = { 0, };
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%d %d", &x[i], &y[i]);
	}

	for (i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (x[i] < x[j] && y[i] < y[j]) {
				rank[i] = rank[i] + 1;
			}
		}
	}

	for (i = 0; i < n; i++) {
		printf("%d ", rank[i] + 1);
	}
}