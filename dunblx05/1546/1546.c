#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int n, i;
	int M = 0;
	double avg = 0;
	double sum = 0.0;
	double a[1000] = { 0, };
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%lf", &a[i]);
		if (M < a[i]) {
			M = a[i];
		}
	}
	
	for (i = 0; i < n; i++) {
		a[i] = (a[i] / M) * 100;
	}
	for (i = 0; i < n; i++) {
		sum = sum + a[i];
	}
	avg = sum / n;
	printf("%lf", avg);
}