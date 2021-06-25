#define _CRT_SECURE_NO_WARNINGS
#define MAX 1000000
#include <stdio.h>
#include <stdlib.h>

int a[MAX];

int main() {
	int n;
	int max = 0;
	int min = 0;
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	min = a[0];
	max = a[0];
	for (int i = 0; i < n; i++) {
		if (max < a[i]) {
			max = a[i];
		}
		if (min > a[i]) {
			min = a[i];
		}
	}
	printf("%d %d", min, max);
}