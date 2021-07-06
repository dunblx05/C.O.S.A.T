#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
	int a[10001] = { 0, };
	int t, n, i, j;
	scanf("%d", &t);

	//소수 판별
	for (i = 0; i < 10001; i++) {
		a[i] = 1;
	}
	a[0] = 0;
	a[1] = 0;
	for (i = 2; i < 10001; i++) {
		if (a[i] != 0) {
			for (j = 2 * i; j < 10001; j = j + i) {
				a[j] = 0;
			}
		}
	}

	//골드바흐 파티션 출력
	for (i = 0; i < t; i++) {
		scanf("%d", &n);
		
		for (j = n / 2; j > 0; j++) {
			if (a[j] != 0 && a[n - j] != 0) {
				printf("%d %d\n", n - j, j);
				break;
			}
		}
	}
}
