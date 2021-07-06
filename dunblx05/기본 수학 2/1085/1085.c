#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
	int x, y, w, h;
	int a, b, c, d;
	int e[4];
	scanf("%d %d %d %d", &x, &y, &w, &h);

	a = x;
	b = y;
	c = w - x;
	d = h - y;

	e[0] = a;
	e[1] = b;
	e[2] = c;
	e[3] = d;

	int min = e[0];
	for (int i = 0; i < 4; i++) {
		if (min > e[i]) {
			min = e[i];
		}
	}
	printf("%d", min);
}
