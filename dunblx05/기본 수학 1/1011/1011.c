#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
	int t, i;
	long long x, y, a, d;
	scanf("%d", &t);

	for (i = 0; i < t; i++) {
		scanf("%lld %lld", &x, &y);
		d = y - x;
		a = sqrt(d);
		if (d == a * a) {
			printf("%lld\n", 2 * a - 1);
		}
		else if (d > a*a && d <= a * a + a) {
			printf("%lld\n", 2 * a);
		}
		else if (d > a*a + a && d <= (a + 1)*(a + 1)) {
			printf("%lld\n", 2 * a + 1);
		}
	}
}