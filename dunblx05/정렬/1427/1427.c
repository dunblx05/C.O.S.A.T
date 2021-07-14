#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int n;
	int a[11] = { 0, };
	int i = 0;
	int cnt = 0;
	scanf("%d", &n);

	while (n > 0) {
		a[i] = n % 10;
		n = n / 10;
		i++;
		cnt++;
	}

	for (i = 0; i < 10; i++) {
		for (int j = i + 1; j < 10; j++) {
			int temp;
			if (a[i] < a[j]) {
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
	}

	for (i = 0; i < cnt; i++) {
		printf("%d", a[i]);
	}
}