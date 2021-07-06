#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
	int x, y, x1, y1, x2, y2, x3, y3;
	
	scanf("%d %d", &x1, &y1);
	scanf("%d %d", &x2, &y2);
	scanf("%d %d", &x3, &y3);

	if (x1 == x2) {
		x = x3;
	}
	else if (x1 == x3) {
		x = x2;
	}
	else
		x = x1;

	if (y1 == y2) {
		y = y3;
	}
	else if (y1 == y3) {
		y = y2;
	}
	else
		y = y1;

	printf("%d %d", x, y);
}
