#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main() {
	int t, k, n, i, x, y;
	int room[15][15] = { 0, };

	for (i = 0; i < 15; i++) {
		room[i][1] = 1;
	}
	for (i = 0; i < 15; i++) {
		room[0][i] = i;
	}
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d", &k);
		scanf("%d", &n);

		for (x = 1; x <= k; x++) {
			for (y = 1; y <= n; y++) {
				room[x][y] = room[x - 1][y] + room[x][y - 1];
			}
		}

		printf("%d\n", room[k][n]);
	}
}