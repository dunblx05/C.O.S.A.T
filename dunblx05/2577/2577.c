#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int i, a, b, c;
	int mul = 0;
	int digit[10] = { 0, };
	scanf("%d %d %d", &a, &b, &c);
	mul = a * b * c;

	while (mul > 0) {
		digit[mul % 10]++;
		mul /= 10;
	}
	for (i = 0; i < 10; i++) {
		printf("%d\n", digit[i]);
	}
}