#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int main() {
	int a[9];
	int i, order;
	int max = 0;
	for (i = 0; i < 9; i++) {
		scanf("%d", &a[i]);
		if (max < a[i]) {
			max = a[i];
			order = i + 1;
		}
	}

	printf("%d\n%d", max, order);

	return 0;
}