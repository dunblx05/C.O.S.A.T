#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int t, i;
	double d;
	int x1, y1, x2, y2, r1, r2;
	scanf("%d", &t);

	for (i = 0; i < t; i++) {
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
		d = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
		if (r1 + r2 > d && abs(r2 - r1) < d) {
			printf("2\n");
		}
		else if (d == 0 && r1 == r2) {
			printf("-1\n");
		}
		else if (r1 + r2 == d) {
			printf("1\n");
		}
		else if (abs(r2 - r1) == d) {
			printf("1\n");
		}
		else if (r2 + r1 < d) {
			printf("0\n");
		}
		else if (abs(r2 - r1) > d) {
			printf("0\n");
		}
		else if (d == 0 && r1 != r2) {
			printf("0\n");
		}

	}
}