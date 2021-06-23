#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int a[10];
	int i, j, count;
	int result = 0;
	for (i = 0; i < 10; i++) {
		scanf("%d", &a[i]);
		a[i] = a[i] % 42;
	}

	for (i = 0; i < 10; i++) {
		count = 0;
		for (j = i + 1; j < 10; j++) {
			if (a[i] == a[j])
				count++;
		}
		if (count == 0) {
			result++;
		}
	}

	printf("%d", result);

/*
	for (i = 0; i < 10; i++) {
		printf("%d\n", a[i]);
	}
*/
}