#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main() {
	int n;
	int res = 0;
	int count = 0;
	scanf("%d", &n);

	while (1) {
		if (n % 5 == 0) {
			count = count + n / 5;
			printf("%d", count);
			break;
		}
		n = n - 3;
		count++;
		if (n < 0) {
			printf("-1");
			break;
		}
	}
}