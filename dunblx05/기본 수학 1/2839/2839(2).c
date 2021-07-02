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

	while (n > 0) {
		if (n % 5 == 0) {
			res = n / 5;
			printf("%d", res + count);
			break;
		}
		else {
			n = n - 3;
			count++;
			if (n < 0) {
				printf("-1");
				break;
			}
			else if (n == 0) {
				printf("%d", count);
				break;
			}
		}
	}
}