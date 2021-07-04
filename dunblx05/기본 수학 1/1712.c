#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	if (b >= c) {
		printf("-1");
		return 0;
	}
	printf("%d", a / (c - b) + 1);
}