#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main() {
	int t, h, w, n, i;
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d %d %d", &h, &w, &n);
		if (n%h == 0) {
			printf("%d%02d\n", h, n / h);
		}
		else
			printf("%d%02d\n", n%h, n / h + 1);
	}
}